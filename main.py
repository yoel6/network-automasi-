import telnetlib
import os
def tampil():
    print "1. Masukkan Ip"
    print "2. Masukkan DHCP"
    print "3. Masukkan Routing"
    print "4. Tampilkan IP"
    print "5. Tidak Ada"

    pilihan = raw_input("Masukkan Pilihan :")

    if(pilihan=="1"):
        host = raw_input("Masukkan ip telnet :")
        user = raw_input("Masukkan Username :")
        password = raw_input("Masukkan Password :")
        ip = raw_input("Masukkan IP :")
        subnet = raw_input("Masukkan subnetmask :")
        interface = raw_input("Masukkan Interface :")

        tn = telnetlib.Telnet(host)

        tn.read_until("Username:")
        tn.write(user + "\n")

        tn.read_until("Password:")
        tn.write(password + "\n")

        tn.write("conf t\n")
        tn.write("int {}\n".format(interface))
        tn.write("ip address {} {}\n".format(ip,subnet))
        tn.write("no sh\n")
        tn.write("end\n")
        tn.write("exit\n")
        print tn.read_all()
        v = raw_input("Masukkan Y untuk kembali :")
        if(v == "Y"):
            os.system('clear')
            tampil()

    elif(pilihan=="2"):
        host = raw_input("Masukkan ip telnet :")
        user = raw_input("Masukkan Username :")
        password = raw_input("Masukkan Password :")
        ip = raw_input("Masukkan IP :")
        ip1 = raw_input("Masukkan IP network:")
        subnet = raw_input("Masukkan subnetmask :")
        interface = raw_input("Masukkan Interface :")
        dhcp = raw_input("nama dhcp pool :")

        tn = telnetlib.Telnet(host)

        tn.read_until("Username:")
        tn.write(user + "\n")

        tn.read_until("Password:")
        tn.write(password + "\n")

        tn.write("conf t\n")
        tn.write("int {}\n".format(interface))
        tn.write("ip dhcp pool {}\n".format(dhcp))
        tn.write("network {} {}\n".format(ip1,subnet))
        tn.write("default-router {}\n".format(ip))
        tn.write("end\n")
        tn.write("exit\n")
        print tn.read_all()
        v = raw_input("Masukkan Y untuk kembali :")
        if (v == "Y"):
            os.system('clear')
            tampil()

    elif(pilihan=="3"):
        host = raw_input("Masukkan ip telnet :")
        user = raw_input("Masukkan Username :")
        password = raw_input("Masukkan Password :")
        ip1 = raw_input("Masukkan IP network yang di tuju :")
        subnet = raw_input("Masukkan subnetmask :")
        next_hop = raw_input("Next hop :")

        tn = telnetlib.Telnet(host)

        tn.read_until("Username:")
        tn.write(user + "\n")

        tn.read_until("Password:")
        tn.write(password + "\n")

        tn.write("conf t\n")
        tn.write("ip route {} {} {}\n".format(ip1,subnet,next_hop))
        tn.write("end\n")
        tn.write("exit\n")
        print tn.read_all()
        v = raw_input("Masukkan Y untuk kembali :")
        if (v == "Y"):
            os.system('clear')
            tampil()
    elif (pilihan == "4"):
        show = ['192.168.1.1','192.168.1.3']
        user = raw_input("Masukkan Username :")
        password = raw_input("Masukkan Password :")
        for q in show:
            tn = telnetlib.Telnet(q)
            tn.read_until("Username:")
            tn.write(user + "\n")
            tn.read_until("Password:")
            tn.write(password + "\n")
            tn.write("conf t\n")
            tn.write("do show ip route\n")
            tn.write("end\n")
            tn.write("exit\n")
            print tn.read_all()
        v = raw_input("Masukkan Y untuk kembali :")
        if (v == "Y"):
            os.system('clear')
            tampil()
    elif (pilihan == "5"):
        os.system('clear')
        tampil()
tampil()
