from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("Compito")
app.geometry('800x200')

ip1 = Entry(app, text = 'IP(1°num)')
ip1.grid(row = 0, column = 0,)

ip2 = Entry(app, text = 'IP(2°num)')
ip2.grid(row = 0, column = 1,)

ip3 = Entry(app, text = 'IP(3°num)')
ip3.grid(row = 0, column = 2,)

ip4 = Entry(app, text = 'IP(4°num)')
ip4.grid(row = 0, column = 3,)

res = Label(app, text = '')
res.grid(row = 0, column = 5)

def IsIPValid():
    ip1num = int(ip1.get().strip())
    ip2num = int(ip2.get().strip())
    ip3num = int(ip3.get().strip())
    ip4num = int(ip4.get().strip())

    if ip1num >=0 and ip1num < 256:
        if ip2num >=0 and ip2num < 256:
            if ip3num >=0 and ip3num < 256:
                if ip4num >=0 and ip4num < 256:
                    res.config(text = "IP valido")

def ClasseIP_E_Subnet_E_CIDR():
    ip1num = int(ip1.get().strip())
    ip2num = int(ip2.get().strip())
    ip3num = int(ip3.get().strip())
    ip4num = int(ip4.get().strip())

    if(ip1num>=0 and ip1num<128):
       messagebox.showinfo(title="Classe SBM e CIDR", message="Classe A. SubnetMask: 255.0.0.0 CIDR:/8")
       messagebox.showinfo(title="Rete", message=f'{ip1num & 255}.0.0.0')

    if(ip1num>=128 and ip1num<191):
       messagebox.showinfo(title="Classe SBM e CIDR", message="Classe B. SubnetMask: 255.255.0.0 CIDR:/16")
       messagebox.showinfo(title="Rete", message=f'{ip1num & 255}.{ip2num & 255}.0.0')

    if(ip1num>=191 and ip1num<224):
       messagebox.showinfo(title="Classe SBM e CIDR", message="Classe C. SubnetMask: 255.255.255.0 CIDR:/24")
       messagebox.showinfo(title="Rete", message=f'{ip1num & 255}.{ip2num & 255}.{ip3num & 255}.0')

    if(ip1num>=224 and ip1num<256):
       messagebox.showinfo(title="Classe SBM e CIDR", message="Classe D. Mi scoccio di chiedere i bit in prestito MA FORZA NAPOLI")


def Wildcard():
    ip1num = int(ip1.get().strip())
    ip2num = int(ip2.get().strip())
    ip3num = int(ip3.get().strip())
    ip4num = int(ip4.get().strip())

    if(ip1num>=0 and ip1num<128):
       messagebox.showinfo(title="WILDCARD", message="0.0.0.255")
       messagebox.showinfo(title="Broadcast", message=f'0.0.0.{ip4num | 255}')

    if(ip1num>=128 and ip1num<191):
       messagebox.showinfo(title="WILDCARD", message="0.0.255.255")
       messagebox.showinfo(title="Broadcast", message=f'0.0.{ip3num | 255}.{ip4num | 255}')

    if(ip1num>=191 and ip1num<224):
       messagebox.showinfo(title="WILDCARD", message="0.255.255.255")
       messagebox.showinfo(title="Broadcast", message=f'0.{ip2num & 255}.{ip3num & 255}.{ip4num & 255}')

    if(ip1num>=224 and ip1num<256):
       messagebox.showinfo(title="WLDCARD", message="Mi scoccio di chiedere i bit in prestito ma FORZA NAPOLI")


def Gateway():
    ip1num = int(ip1.get().strip())
    ip2num = int(ip2.get().strip())
    messagebox.showinfo(title="Gateway", message=f"{ip1num}.{ip2num}.0.1")


Button(app, text = 'Controllo IP', command = IsIPValid).grid(row = 1, column = 0)
Button(app, text = 'Controllo Classe-SBM-CIDR', command = ClasseIP_E_Subnet_E_CIDR).grid(row = 1, column = 1)
Button(app, text = 'Wildcard', command = Wildcard).grid(row = 1, column = 2)
Button(app, text = 'Gateway', command = Gateway).grid(row = 1, column = 3)

if __name__ == '__main__':
	app.mainloop()