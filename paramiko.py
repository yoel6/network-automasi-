import paramiko
import time
import os
class automation():
    def pilihan(self):
        print("==================Aplikasi Automation==================")
        print("1.Pengalamatan IP")
        x = int(input("Masukkan Pilihan :"))
        if (x == 1):
            automation.pengalamanip(self)
    def pengalamanip(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        hostname = ['192.168.122.220','192.168.122.239']
        g = len(hostname)
        v = int(g)
        for h in range(v):
            c = hostname[h]
            print('{}.{}'.format(h+1,c))
        a = int(input("masukan Pilihan hostname :"))
        b = input("masukan Ip :")
        d = input("masukan subnetmask :")
        c = input("masukan interface :")
        x = hostname[a-1]
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
wiwin = automation()
wiwin.pilihan()
