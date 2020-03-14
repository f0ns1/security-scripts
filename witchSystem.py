#!/usr/bin/python

import subprocess, re, sys

def return_ttl(address):
    proc = subprocess.Popen(["ping -c 1 %s" % address, ""], stdout=subprocess.PIPE, shell=True)
    (out,err) = proc.communicate()
    out = out.split()
    out = re.findall(r"\d{1,3}", out[12])
    return out[0]

def return_ttl_os_name(ttl_number):
    if ttl_number >= 0 and ttl_number <= 64:
        return "Linux"
    elif ttl_number >=65 and ttl_number <=128:
        return "Windows"
    elif ttl_number >=200 and ttl_number <=260:
        return "IOS"
    else:
        return "Unknown"

if len(sys.argv) != 2:
        print "Usage error : pythom "+ sys.argv[0] + " <ip address>"
        exit (1)

if __name__ == '__main__':
    address=sys.argv[1]
    print "\t [+] ttl scann for host :  "+address
    ttl= return_ttl(address)
    ttl_name= return_ttl_os_name(int(ttl))
    try:
        print "\n\t\t  [+] %s -> TTL = %s" % (address, int(ttl))
        print "\t\t  [+] %s -> %s" % (address, ttl_name)
    except:
        print "Exception ... print "
        pass
    print "\n\t [+] End process scann ttl "
