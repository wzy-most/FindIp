from scapy.all import *


def main():
    ip = "192.168.159.152"
    for port in range(1, 65535):
        req = sr1(IP(dst=ip)/TCP(sport=12345,dport=port,flags="S"),verbose=0)

        if str(type(req))=="<type 'NoneType'>" :
            print("this %s is not alive"%(ip))
        elif req.haslayer(TCP):
            if req.getlayer(TCP).flags == 0x12:
               resp1 = sr1(IP(dst=ip) / TCP(sport=12345, dport=port, flags="AR"), timeout=5,verbose=0)
               print("this %s --- %s  is alive"%(ip,port))
            elif req.getlayer(TCP).flags == 0x14:
               print("this %s is not alive"%(port))

pass

if __name__ == "__main__":
    main()