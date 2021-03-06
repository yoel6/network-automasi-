import paramiko
import time
import os
class automation():

    def __init__(self):
        self.hostname=['192.168.1.1','192.168.1.3']

    def pilihan(self):
        print("==================Aplikasi Automation==================")
        print("1.Pengalamatan IP")
        print("2.Cek IP")
        print("3.Pengalamatan IP vlan")
        print("4.Masukkan Setting DHCP")
        print("5.switching")
        print("6.aktifkan interface")
        print("7.routing")
        print("8.Kembali")
        x = int(input("Masukkan Pilihan :"))
        if (x == 1):
            automation.pengalamanip(self)
        elif (x == 2):
            automation.cekip(self)
        elif (x == 3):
            automation.PengalamatanIPvlan(self)
        elif (x == 4):
            automation.dhcp(self)
        elif (x == 5):
            automation.swiitching(self)
        elif (x == 6):
            automation.aktif(self)
        elif (x == 7):
            automation.Routing(self)
        else:
            os.system('clear')
            automation.pilihan(self)
    def pengalamanip(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        g = len(self.hostname)
        v = int(g)
        for h in range(v):
            c = self.hostname[h]
            print('{}.{}'.format(h+1,c))
        a = int(input("masukan Pilihan hostname :"))
        b = input("masukan Ip :")
        d = input("masukan subnetmask :")
        c = input("masukan interface :")
        x = self.hostname[a-1]
        ssh_client.connect(hostname=x,username="cisco",password="cisco")
        conn = ssh_client.invoke_shell()
        conn.send("enable\n")
        conn.send("cisco\n")
        conn.send("conf t\n")
        conn.send("int {}\n".format(c))
        conn.send("ip address {} {}\n".format(b,d))
        conn.send("exit\n")
        conn.send("end\n")
        time.sleep(1)
        output = conn.recv(65535)
        print(output.decode("ascii"))
        ssh_client.close()
        q = input("Apakah Anda Ingin Mengulangnya :")
        if(q == "y"):
            os.system('clear')
            automation.pilihan(self)
    def cekip(self):
        x = []
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        g = len(self.hostname)
        v = int(g)
        for h in range(v):
            c = self.hostname[h]
            print('{}.{}'.format(h+1,c))
        a = input("masukan Pilihan hostname :")
        u = len(a)
        e = int(u)
        for q in range(e):
            t = a[q]
            x.append(t)
        for w in x:
            y = int(w)
            x = self.hostname[y-1]
            ssh_client.connect(hostname=x,username="cisco",password="cisco")
            conn = ssh_client.invoke_shell()
            conn.send("enable\n")
            conn.send("cisco\n")
            conn.send("show ip interface brief\n")
            conn.send("end\n")
            time.sleep(1)
            output = conn.recv(65535)
            print(output.decode("ascii"))
            ssh_client.close()
        q = input("Apakah Anda Ingin Mengulangnya :")
        if(q == "y"):
            input
            os.system('clear')
            automation.pilihan(self)
    def PengalamatanIPvlan(self):
        x = []
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        g = len(self.hostname)
        v = int(g)
        for h in range(v):
            c = self.hostname[h]
            print('{}.{}'.format(h + 1, c))
        a = input("masukan Pilihan hostname :")
        u = len(a)
        e = int(u)
        for q in range(e):
            t = a[q]
            x.append(t)
        print(x)
        for g in x:
            z =int(g)
            y = self.hostname[z-1]
            print("================={}=================".format(y))
            b = input("masukan Ip :")
            d = input("masukan subnetmask :")
            c = input("masukan interface :")
            e = input("masukkan no vlan :")
            ssh_client.connect(hostname=y, username="cisco", password="cisco")
            conn = ssh_client.invoke_shell()
            conn.send("enable\n")
            conn.send("cisco\n")
            conn.send("conf t\n")
            conn.send("int {}.{}\n".format(c,e))
            conn.send("encapsulation dot1Q {}\n".format(e))
            conn.send("ip address {} {}\n".format(b, d))
            conn.send("int {}\n".format(c))
            conn.send("no sh\n")
            conn.send("exit\n")
            conn.send("end\n")
            time.sleep(1)
            output = conn.recv(65535)
            print(output.decode("ascii"))
            ssh_client.close()
        q = input("Apakah Anda Ingin Mengulangnya :")
        if (q == "y"):
            os.system('clear')
            automation.pilihan(self)
    def dhcp(self):
        x = []
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        g = len(self.hostname)
        v = int(g)
        for h in range(v):
            c = self.hostname[h]
            print('{}.{}'.format(h + 1, c))
        a = input("masukan Pilihan hostname :")
        u = len(a)
        e = int(u)
        for q in range(e):
            t = a[q]
            x.append(t)
        print(x)
        for g in x:
            z = int(g)
            y = self.hostname[z - 1]
            print("================={}=================".format(y))
            print("1.Buat DHCP")
            print("2.tampilkan DHCP")
            q = int(input("Masukan Inputan : "))
            if(q == 1):
                ssh_client.connect(hostname=y, username="cisco", password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("show ip interface brief\n")
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
                b = input("masukan network :")
                f = input("masukan ip dhcp :")
                d = input("masukan subnetmask :")
                e = input("masukkan nama dhcp :")
                ssh_client.connect(hostname=y, username="cisco", password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("conf t\n")
                conn.send("ip dhcp pool {}\n".format(e))
                conn.send("network {} {}\n".format(b, d))
                conn.send("default-router {}\n".format(f))
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
            elif (q == 2):
                ssh_client.connect(hostname=y, username="cisco", password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("show ip dhcp pool\n")
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
        q = input("Apakah Anda Ingin Mengulangnya :")
        if (q == "y"):
            os.system('clear')
            automation.pilihan(self)
    def swiitching(self):
        x = []
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        g = len(self.hostname)
        v = int(g)
        for h in range(v):
            c = self.hostname[h]
            print('{}.{}'.format(h + 1, c))
        a = input("masukan Pilihan hostname :")
        u = len(a)
        e = int(u)
        for q in range(e):
            t = a[q]
            x.append(t)
        print(x)
        for g in x:
            z = int(g)
            y = self.hostname[z - 1]
            print("================={}=================".format(y))
            print("1.Buat switching")
            print("2.tampilkan hasil swiitching")
            q = int(input("Masukan Inputan : "))
            if(q==1):
                ssh_client.connect(hostname=y, username="cisco", password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("show vlan\n")
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
                b = input("masukan interface:")
                f = input("masukan no vlan :")
                ssh_client.connect(hostname=y, username="cisco", password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("conf t\n")
                conn.send("int {}\n".format(b))
                conn.send("sw mode access\n")
                conn.send("sw access vlan {}\n".format(f))
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
            if (q == 2):
                ssh_client.connect(hostname=y, username="cisco", password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("show vlan\n")
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
        q = input("Apakah Anda Ingin Mengulangnya :")
        if (q == "y"):
            os.system('clear')
            automation.pilihan(self)
    def aktif(self):
        x = []
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        g = len(self.hostname)
        v = int(g)
        for h in range(v):
            c = self.hostname[h]
            print('{}.{}'.format(h+1,c))
        a = input("masukan Pilihan hostname :")
        u = len(a)
        e = int(u)
        for q in range(e):
            t = a[q]
            x.append(t)
        for w in x:
            y = int(w)
            x = self.hostname[y-1]
            ssh_client.connect(hostname=x,username="cisco",password="cisco")
            conn = ssh_client.invoke_shell()
            conn.send("enable\n")
            conn.send("cisco\n")
            conn.send("show ip interface brief\n")
            conn.send("exit\n")
            conn.send("end\n")
            time.sleep(1)
            output = conn.recv(65535)
            print(output.decode("ascii"))
            ssh_client.close()
            r = input("masukan interface :")
            ssh_client.connect(hostname=x, username="cisco", password="cisco")
            conn = ssh_client.invoke_shell()
            conn.send("enable\n")
            conn.send("cisco\n")
            conn.send("conf t\n")
            conn.send("int {}".format(r))
            conn.send("no sh\n")
            conn.send("exit\n")
            conn.send("end\n")
            time.sleep(1)
            output = conn.recv(65535)
            print(output.decode("ascii"))
            ssh_client.close()
        q = input("Apakah Anda Ingin Mengulangnya :")
        if(q == "y"):
            input
            os.system('clear')
            automation.pilihan(self)
    def Routing(self):
        x = []
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        g = len(self.hostname)
        v = int(g)
        for h in range(v):
            c = self.hostname[h]
            print('{}.{}'.format(h+1,c))
        a = input("masukan Pilihan hostname :")
        u = len(a)
        e = int(u)
        for q in range(e):
            t = a[q]
            x.append(t)
        for w in x:
            print("Masukkan pilihan Routing")
            print("1.OSPF")
            print("2.RIP")
            print("3.EGRP")
            print("4.tampilkan routing")
            q =int(input("Masukkan Pilihan :"))
            if(q == 1):
                y = int(w)
                x = self.hostname[y-1]
                ssh_client.connect(hostname=x,username="cisco",password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("show ip interface brief\n")
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
                v = input("masukan id ospf :")
                z = int(input("Masukkan Total Routing :"))
                ssh_client.connect(hostname=x, username="cisco", password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("conf t\n")
                conn.send("router ospf {}\n".format(v))
                for c in range(z):
                    a = input("Masukkan ip network :")
                    b = input("Masukkan wildcard mask :")
                    c = input("Masukkan no area :")
                    conn.send("network {} {} area {}\n".format(a,b,c))
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
            elif(q == 2):
                y = int(w)
                x = self.hostname[y - 1]
                ssh_client.connect(hostname=x, username="cisco", password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("show ip interface brief\n")
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
                v = input("masukan id rip :")
                z = int(input("Masukkan Total Routing :"))
                ssh_client.connect(hostname=x, username="cisco", password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("conf t\n")
                conn.send("router rip\n")
                conn.send("version {}\n".format(v))
                for c in range(z):
                    a = input("Masukkan ip network :")
                    conn.send("network {}\n".format(a))
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
            elif (q == 3):
                y = int(w)
                x = self.hostname[y - 1]
                ssh_client.connect(hostname=x, username="cisco", password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("show ip interface brief\n")
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
                c = input("masukan id EIGRP :")
                j = int(input("Masukkan Total Routing :"))
                ssh_client.connect(hostname=x, username="cisco", password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("conf t\n")
                conn.send("router eigrp {}\n".format(c))
                for c in range(j):
                    a = input("Masukkan ip network :")
                    conn.send("network {}\n".format(a))
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
            elif (q == 4):
                y = int(w)
                x = self.hostname[y - 1]
                ssh_client.connect(hostname=x, username="cisco", password="cisco")
                conn = ssh_client.invoke_shell()
                conn.send("enable\n")
                conn.send("cisco\n")
                conn.send("show ip interface brief\n")
                conn.send("exit\n")
                conn.send("end\n")
                time.sleep(1)
                output = conn.recv(65535)
                print(output.decode("ascii"))
                ssh_client.close()
        q = input("Apakah Anda Ingin Mengulangnya :")
        if(q == "y"):
            input
            os.system('clear')
            automation.pilihan(self)
wiwin = automation()
wiwin.pilihan()
