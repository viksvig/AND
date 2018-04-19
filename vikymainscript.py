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
        tn.write("set interfaces lo1 unit 0 family inet address 6.6.6.6/32\n")
        
               
        

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
        tn.write("int lo 1\n")
        tn.write("ip add 15.1.1.1 255.255.255.255\n")
        tn.write("int lo 2\n")
        tn.write("ip add 2.2.2.2 255.255.255.255\n")
        tn.write("int lo 3\n")
        tn.write("ip add 3.3.3.3 255.255.255.255\n")
        tn.write("int lo 4\n")
        tn.write("ip add 4.4.4.4 255.255.255.255\n")
        tn.write("int lo 5\n")
        tn.write("ip add 5.5.5.5 255.255.255.255\n")
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
            tn.write("ip add 12.1.1.1 255.255.255.255\n")
            tn.write("int lo 2\n")
          
            tn.write("ip add 2.2.2.2 255.255.255.255\n")
            tn.write("int lo 3\n")
            tn.write("ip add 3.3.3.3 255.255.255.255\n")
            tn.write("int lo 4\n")
            tn.write("ip add 4.4.4.4 255.255.255.255\n")
            tn.write("int lo 5\n")
            tn.write("ip add 5.5.5.5 255.255.255.255\n")
            tn.write("end\n")
            tn.write("exit\n")

            print tn.read_all()



