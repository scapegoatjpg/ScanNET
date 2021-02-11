import dpkt, pcap       #pip install dpkt and pip intall pypcap (just use the requirements.txt)
import datetime
import time
import socket
from dpkt.compat import compat_ord
from dpkt.utils import mac_to_str, inet_to_str

def print_packets(pcap):
    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)

        #for ipv6 packets
        if isinstance(eth.data, dpkt.ip6.IP6):
            ipv6 = eth.data

            print('Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp)))
            print('Ethernet Frame: ', mac_to_str(eth.data.src), mac_to_str(eth.data.dst), eth.type)
            print('IPv6: %s -> %s' % (inet_to_str(ipv6.src), inet_to_str(ipv6.dst)))

            if isinstance(ipv6.data, dpkt.icmp6.ICMP6):
                icmp6 = ipv6.data
                print('ICMP6: type:%d code:%d checksum:%d data: %s' % (icmp6.type, icmp6.code, icmp6.sum, repr(icmp6.data)))

        #for ipv4 packets
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data

            #frag stuff
            do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
            more_fragments = bool(ip.off & dpkt.ip.IP_MF)
            fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

            #print first part of packet
            print('Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp)))
            print('Ethernet Frame: ', mac_to_str(eth.data.src), mac_to_str(eth.data.dst), eth.type)
            print('IPv4: %s -> %s (len=%d ttl=%d DF=%d MF=%d offset=%d)' % (inet_to_str(ip.src), inet_to_str(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments, fragment_offset))

            #for tcp packets
            if isinstance(ip.data, dpkt.tcp.TCP):
                tcp = ip.data
                print('Source Port: %d' % tcp.sport)
                print('Destination Port: %d' % tcp.dport)

            #for icmp packets
            if isinstance(ip.data, dpkt.icmp.ICMP):
                icmp = ip.data
                print('ICMP: type:%d code:%d checksum:%d data: %s' % (icmp.type, icmp.code, icmp.sum, repr(icmp.data)))

            #for udp packets
            if isinstance(ip.data, dpkt.udp.UDP):
                udp = ip.data
                print('Source Port: %d' % udp.sport)
                print('Destination Port: %d' % udp.dport)
    
        #for arp packets (currently skipped)
        if isinstance(eth.data, dpkt.arp.ARP):
            #print('Ignoring ARP packet %s\n' % eth.data.__class__.__name__)
            arp = eth.data
            print('ARP: %s\n' % arp.data)
            continue

        #prints protocols
        print('Internet Protocol version: %s' % eth.data.__class__.__name__)
        print('Protocol: %s(%d)' % (eth.data.get_proto(eth.data.p).__name__, eth.data.p))
        #print('Type: %s' % eth.data.type)
        print('\n')

def write_packets(writer):
    pc = pcap.pcap()
    counter = 0
    for timestamp, packet in pc:
        counter += 1
        writer.writepkt(packet, timestamp)
        #20 packets at a time
        if counter == 20:
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
