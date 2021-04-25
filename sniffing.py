import dpkt, pcap, datetime, time, socket, nmap, who_is_on_my_wifi
from threading import Timer
from who_is_on_my_wifi import who
from dpkt.compat import compat_ord
from dpkt.utils import mac_to_str, inet_to_str
from dns import reversename, resolver

class Packet():
    def __init__(self):
        self.pack = ''
        self.hostname = ''
        self.num = 0
        self.ts = ''
        self.timing = ''
        self.macsrc = ''
        self.macdst = ''
        self.src = ''
        self.dst = ''
        self.sport = 0
        self.dport = 0
        self.ipv = ''
        self.prtcl = ''
        self.length = 0
        self.info = ''
class Devs():
    def __init__(self):
        self.hostname = ''
        self.timing = ''
        self.ipaddr = ''
        self.mac = ''
        self.activity = ''

#packet counters
class PktCount():
    def __init__(self):
        self.counter = 0
        self.ipcounter = 0
        self.nonipcounter = 0
        self.tcpcounter = 0
        self.udpcounter = 0
        self.arpcounter = 0
        self.httpcounter = 0
        self.httpscounter = 0
        self.smtpcounter = 0
        self.dhcpcounter = 0 
        self.ftpcounter = 0
        self.sshcounter = 0
        self.ntpcounter = 0 
        self.telnetcounter = 0
        self.whoiscounter = 0 
        self.rsynccounter = 0
        self.icmpcounter = 0 
        self.ipv6counter = 0

#list to update active devices in gui
recentdevs = []
ips = []
alldevs = []
track = []
WHO = who()
for i in range(0, len(WHO)):
    alldevs.append(WHO[i][1])
#list to send and update for the gui
pkt_list = []
#global counter to count every packet read
pktnum = 0

pktcounting = PktCount()

def print_packets(pcap):
    for timestamp, buf in pcap:
        global pktcounting
        pktcounting.counter += 1
        
        eth = dpkt.ethernet.Ethernet(buf)
        #assigned anything applicable right away
        pkt = Packet
        pkt.pack = eth.data
        global pktnum
        pkt.num = pktnum
        pkt.ts = str(datetime.datetime.utcfromtimestamp(timestamp))
        pkt.timing = (str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second))
        pkt.sport = 0
        pkt.dport = 0
        pkt.length = len(eth.data)
        pktnum += 1

        if eth.type != dpkt.ethernet.ETH_TYPE_IP and eth.type != dpkt.ethernet.ETH_TYPE_IP6:
            pktcounting.nonipcounter += 1

        #for ipv6 packets
        if isinstance(eth.data, dpkt.ip6.IP6):
            pktcounting.ipv6counter += 1
            ipv6 = eth.data
            
            pkt.macsrc = mac_to_str(ipv6.src)
            pkt.macdst = mac_to_str(ipv6.dst)
            pkt.src = inet_to_str(ipv6.src)
            pkt.dst = inet_to_str(ipv6.dst)

        #for ipv4 packets
        elif isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            
            pkt.macsrc = mac_to_str(ip.src)
            pkt.macdst = mac_to_str(ip.dst)
            pkt.src = inet_to_str(ip.src)
            pkt.dst = inet_to_str(ip.dst)
            
            pktcounting.ipcounter += 1
            if ip.p == dpkt.ip.IP_PROTO_ICMP:
                pktcounting.icmpcounter += 1

            #for tcp packets
            if isinstance(ip.data, dpkt.tcp.TCP):
                tcp = ip.data
                pkt.sport = tcp.sport
                pkt.dport = tcp.dport

                pktcounting.tcpcounter += 1
                if tcp.sport == 80 or tcp.dport == 80:
                    pktcounting.httpcounter += 1
                elif tcp.sport == 443 or tcp.dport == 443:
                    pktcounting.httpscounter += 1
                elif tcp.sport == 22 or tcp.dport == 22:
                    pktcounting.sshcounter += 1
                elif tcp.sport == 25 or tcp.dport == 25:
                    pktcounting.smtpcounter += 1
                elif tcp.sport == 23 or tcp.dport == 23:
                    pktcounting.smtpcounter += 1
                elif tcp.sport == 43 or tcp.dport == 43:
                    pktcounting.whoiscounter += 1
                elif tcp.sport == 873 or tcp.dport == 873:
                    pktcounting.rsynccounter += 1
                elif tcp.sport == 21 or tcp.dport == 21:
                    pktcounting.ftpcounter += 1

            #for udp packets
            if isinstance(ip.data, dpkt.udp.UDP):
                udp = ip.data
                pkt.sport = udp.sport
                pkt.dport = udp.dport

                pktcounting.udpcounter += 1
                if udp.sport == 67 or udp.dport == 67 or udp.sport == 68 or udp.dport == 68:
                    pktcounting.dhcpcounter += 1
                elif udp.sport == 123 or udp.dport == 123:
                    pktcounting.ntpcounter += 1

        #for arp packets (currently skipped)
        if isinstance(eth.data, dpkt.arp.ARP):
            pktcounting.arpcounter += 1
            pkt.prtcl = 'ARP'
            pkt_list.append(pkt)
            continue

        #print hostname (DNS for now)
        addr = pkt.src
        domain_address = reversename.from_address(addr)
        try:
            pkt.hostname = str(resolver.resolve(domain_address, "PTR")[0])
        except resolver.NXDOMAIN:
            pkt.hostname = str(socket.getnameinfo((pkt.src, 0), 0)[0])
        #prints protocols
        pkt.ipv = eth.data.__class__.__name__
        try:
            pkt.prtcl = eth.data.get_proto(eth.data.p).__name__
        except AttributeError:
            pass

        pkt_list.append(pkt)

def write_packets(writer):
    pc = pcap.pcap()
    counter = 0
    for timestamp, packet in pc:
        counter += 1
        writer.writepkt(packet, timestamp)
        #one packet at a time
        if counter == 1:
            writer.close()
            break

def net():
    #infinte loop to continously sniff packets
    while True:
        try:
            #creates a pcap file if not already made 
            with open('test.pcap', 'wb') as w:
                writer = dpkt.pcap.Writer(w)
                write_packets(writer)

            #reads from created pcap file and prints to terminal for now
            with open('test.pcap', 'rb') as f:
                pcap = dpkt.pcap.Reader(f)
                print_packets(pcap)
        except KeyboardInterrupt:
            break