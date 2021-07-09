import telnetlib
import os
class telnet():
    def tampil(self):
        q = 'cisco'
        print "1. Masukkan Ip"
        print "2. Masukkan DHCP"
        print "3. Masukkan Routing"
        print "4. Masukkan IP dengan vlan"
        print "5. VLAN Switch"
        print "6. Tidak Ada"
        pilihan = raw_input("Masukkan Pilihan :")
        if(pilihan=="1"):
            host = raw_input("Masukkan ip telnet :")
            ip = raw_input("Masukkan IP :")
            subnet = raw_input("Masukkan subnetmask :")
            interface = raw_input("Masukkan Interface :")

            tn = telnetlib.Telnet(host)

            tn.read_until("Username:")
            tn.write(q + "\n")

            tn.read_until("Password:")
            tn.write(q + "\n")

            tn.write("conf t\n")
            tn.write("int {}\n".format(interface))
            tn.write("ip address {} {}\n".format(ip,subnet))
            tn.write("no sh\n")
            tn.write("end\n")
            tn.write("exit\n")
            print tn.read_all()
            v = raw_input("Masukkan Y untuk kembali")
            if(v == "Y"):
                os.system('clear')
                telnet.tampil(self)
        elif(pilihan=="2"):
            host = raw_input("Masukkan ip telnet :")
            ip = raw_input("Masukkan IP :")
            ip1 = raw_input("Masukkan IP network:")
            subnet = raw_input("Masukkan subnetmask :")
            interface = raw_input("Masukkan Interface :")
            dhcp = raw_input("nama dhcp pool :")

            tn = telnetlib.Telnet(host)

            tn.read_until("Username:")
            tn.write(q + "\n")

            tn.read_until("Password:")
            tn.write(q + "\n")

            tn.write("conf t\n")
            tn.write("int {}\n".format(interface))
            tn.write("ip dhcp pool {}\n".format(dhcp))
            tn.write("network {} {}\n".format(ip1,subnet))
            tn.write("default-router {}\n".format(ip))
            tn.write("end\n")
            tn.write("exit\n")
            print tn.read_all()
            v = raw_input("Masukkan Y untuk kembali")
            if (v == "Y"):
                os.system('clear')
                telnet.tampil(self)

        elif(pilihan=="3"):
            host = raw_input("Masukkan ip telnet :")
            ip1 = raw_input("Masukkan IP network yang di tuju :")
            subnet = raw_input("Masukkan subnetmask :")
            next_hop = raw_input("Next hop :")

            tn = telnetlib.Telnet(host)

            tn.read_until("Username:")
            tn.write(q + "\n")

            tn.read_until("Password:")
            tn.write(q + "\n")

            tn.write("conf t\n")
            tn.write("ip route {} {} {}\n".format(ip1,subnet,next_hop))
            tn.write("end\n")
            tn.write("exit\n")
            print tn.read_all()
            v = raw_input("Masukkan Y untuk kembali")
            if (v == "Y"):
                os.system('clear')
                telnet.tampil(self)
        elif (pilihan == "3"):
            host = raw_input("Masukkan ip telnet :")
            ip1 = raw_input("Masukkan IP network yang di tuju :")
            subnet = raw_input("Masukkan subnetmask :")
            next_hop = raw_input("Next hop :")

            tn = telnetlib.Telnet(host)

            tn.read_until("Username:")
            tn.write(q + "\n")

            tn.read_until("Password:")
            tn.write(q + "\n")

            tn.write("conf t\n")
            tn.write("ip route {} {} {}\n".format(ip1, subnet, next_hop))
            tn.write("end\n")
            tn.write("exit\n")
            print tn.read_all()
            v = raw_input("Masukkan Y untuk kembali")
            if (v == "Y"):
                os.system('clear')
                telnet.tampil(self)
        elif (pilihan == "4"):
            host = raw_input("Masukkan ip telnet :")
            Jumlah = raw_input("Masukkan Jumlah vlan :")
            g = int(Jumlah)
            for i in range(g):
                ip = raw_input("Masukkan IP :")
                subnet = raw_input("Masukkan subnetmask :")
                interface = raw_input("Masukkan Interface :")
                network = raw_input("Masukkan Network :")
                dhcp = raw_input("nama dhcp pool :")
                no_vlan = raw_input("Masukkan no vlan :")
                tn = telnetlib.Telnet(host)

                tn.read_until("Username:")
                tn.write(q + "\n")

                tn.read_until("Password:")
                tn.write(q + "\n")

                tn.write("conf t\n")
                tn.write("int {}\n".format(interface))
                tn.write("encapsulation dot1Q {}\n".format(no_vlan))
                tn.write("ip address {} {}\n".format(ip, subnet))
                tn.write("ip dhcp pool {}\n".format(dhcp))
                tn.write("network {} {}\n".format(network, subnet))
                tn.write("default-router {}\n".format(ip))
                tn.write("end\n")
                tn.write("exit\n")
                print tn.read_all()
            user = raw_input("Aktifkan vlan ya / tidak :")
            if user == "ya":
                host1 = raw_input("Masukkan ip telnet :")
                interface1 = raw_input("Masukkan Interface :")

                tn = telnetlib.Telnet(host1)

                tn.read_until("Username:")
                tn.write(q + "\n")

                tn.read_until("Password:")
                tn.write(q + "\n")

                tn.write("conf t\n")
                tn.write("int {}\n".format(interface1))
                tn.write("no sh\n")
                tn.write("end\n")
                tn.write("exit\n")
                print tn.read_all()
            else:
                f = raw_input("Masukkan Y untuk kembali")
                if (f == "Y"):
                    os.system('clear')
                    telnet.tampil(self)
            v = raw_input("Masukkan Y untuk kembali")
            if (v == "Y"):
                os.system('clear')
                telnet.tampil(self)
        elif(pilihan == "5"):
            host1 = raw_input("Masukkan ip telnet :")
            jumlah_vlan = raw_input("Masukkan jumlah vlan yang akan di buat :")
            k = int(jumlah_vlan)
            for d in range(k):
                vlan = raw_input("Masukkan no vlan:")
                vlan1 = raw_input("Masukkan nama vlan:")
                interface2 = raw_input("Masukkan Interface Yang Ada:")
                tn = telnetlib.Telnet(host1)

                tn.read_until("Username:")
                tn.write(q + "\n")

                tn.read_until("Password:")
                tn.write(q + "\n")

                tn.write("conf t\n")
                tn.write("vlan {}\n".format(vlan))
                tn.write("name {}\n".format(vlan1))
                tn.write("int {}\n".format(interface2))
                tn.write("sw mode access\n")
                tn.write("sw access vlan {}\n".format(vlan))
                tn.write("end\n")
                tn.write("exit\n")
                print tn.read_all()
            v = raw_input("Masukkan Y untuk kembali")
            if (v == "Y"):
                os.system('clear')
                telnet.tampil(self)
        elif(pilihan == "6"):
            os.system('clear')
            telnet.tampil(self)
        else:
            os.system('clear')
            telnet.tampil(self)

manusia = telnet()
manusia.tampil()
