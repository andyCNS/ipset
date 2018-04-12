from IPy import IP
import sys, getopt
from optparse import OptionParser

# Get file input and other user defined options

use = "Usage: %prog [options] -i <IP Addres/netmask>"
parser = OptionParser(usage = use)

parser.add_option("-i", dest="ipnet", default="127.0.0.1/24", help="Set IP Address with netmask eg. 127.0.0.1/24")

options, args = parser.parse_args()

ipnet= options.ipnet

ip = IP(ipnet, make_net=True)
for x in ip:
	print(x)

