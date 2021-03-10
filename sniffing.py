import dpkt, pcap       #pip install dpkt and pip intall pypcap (just use the requirements.txt)
import datetime
import time
from threading import Timer
import socket
import nmap
import who_is_on_my_wifi
from who_is_on_my_wifi import who
from dpkt.compat import compat_ord
from dpkt.utils import mac_to_str, inet_to_str

class Packet():
    pack = ''
    hostname = ''
    num = 0
    ts = ''
    timing = ''
    macsrc = ''
    macdst = ''
    src = ''
    dst = ''
    sport = 0
    dport = 0
    ipv = ''
    prtcl = ''
    length = 0
    info = ''
class Devs():
    hostname = ''
    timing = ''
    ipaddr = ''
    mac = ''
    activity = ''

#list to update active devices in gui
recentdevs = []
ips = []
alldevs = []
WHO = who()
for i in range(0, len(WHO)):
    alldevs.append(WHO[i][1])
#list to send and update for the gui
pkt_list = []
#global counter to count every packet read
pktnum = 0

def print_packets(pcap):
    for timestamp, buf in pcap:
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

        #for ipv6 packets
        if isinstance(eth.data, dpkt.ip6.IP6):
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
            
            #frag stuff
            #do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
            #more_fragments = bool(ip.off & dpkt.ip.IP_MF)
            #fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

            #for tcp packets
            if isinstance(ip.data, dpkt.tcp.TCP):
                tcp = ip.data
                pkt.sport = tcp.sport
                pkt.dport = tcp.dport

            #for udp packets
            if isinstance(ip.data, dpkt.udp.UDP):
                udp = ip.data
                pkt.sport = udp.sport
                pkt.dport = udp.dport

        #for arp packets (currently skipped)
        if isinstance(eth.data, dpkt.arp.ARP):
            pkt.prtcl = 'ARP'
            pkt_list.append(pkt)
            continue

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