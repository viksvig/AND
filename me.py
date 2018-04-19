import getpass
import sys
import telnetlib

HOST=("192.168.9.141","192.168.9.142","192.168.9.139")
user=raw_input("Enter your username:")
password=getpass.getpass()

for i in HOST:
    if i is "192.168.9.141":
        tn=telnetlib.Telnet(HOST[0],timeout=15)

        tn.read_until("login:")
        tn.write(user+"\n")

        if password:
            tn.read_until("Password:")
            tn.write(password+"\n")



        tn.write("configure\n")
        tn.write("set interfaces lo1 unit 0 family inet address 14.1.1.1/32\n")
        tn.write("set interfaces lo2 unit 0 family inet address 2.2.2.2/32\n")
        tn.write("set interfaces lo3 unit 0 family inet address 3.3.3.3/32\n")
        tn.write("set interfaces lo4 unit 0 family inet address 4.4.4.4/32\n")
        tn.write("set interfaces lo5 unit 0 family inet address 5.5.5.5/32\n")

        tn.write("commit and-quit\n")
        tn.write("exit\n")
        
        print tn.read_all()

    elif i is "192.168.9.142":
        tn=telnetlib.Telnet(HOST[1],timeout=5)

        tn.read_until("Username:")
        tn.write(user+"\n")

        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("en\n")
        tn.write("conf t\n")
        for l in range(1,6):
                ip= str(l)+"."+str(l)+"."+str(l)+"."+str(l)
                tn.write("interface loopback"+str(l)+"\n")
                tn.write (" ip address"+" " + ip +" 255.255.255.255\n")

       
        tn.write("end\n")
        tn.write("exit\n")

       

        print tn.read_all()

    elif i is "192.168.9.139":
        tn=telnetlib.Telnet(HOST[2],timeout=5)

        tn.read_until("Username:")
        tn.write(user+"\n")

        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
            
            

            tn.write("conf t\n")
            tn.write("int lo 1\n")
            

            for l in range(1,6):
                ip= str(l)+"."+str(l)+"."+str(l)+"."+str(l)
                tn.write("interface loopback"+str(l)+"\n")
                tn.write (" ip address"+" " + ip +" 255.255.255.255\n")
          
           
            tn.write("end\n")
            tn.write("exit\n")

            print tn.read_all()



