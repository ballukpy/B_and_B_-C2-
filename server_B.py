import socket as soc
import time
from colorama import Fore, Back, Style

class server_side:
    
    def __init__(self) :
        self.ip="127.0.0.1"
        self.port=2222
        # self.timeout=20
    
    
    
    def first_connection(self):
        tcpsoc=soc.socket(soc.AF_INET,soc.SOCK_STREAM)
        tcpsoc.bind(("",self.port)) #"" tamami ip haro daryaft mikone
        tcpsoc.listen(1)
        print(Fore.RED+"Starting Server ... ")
        print(Fore.RED+"Host Created ...")
        while True:
            client , address = tcpsoc.accept()
            client_id = address[0] + ":" + str(address[1])
            # client.settimeout(self.timeout)
            print(f"{client_id} connected to our server")    
            input_data=input("wanna time out? y/n ")  #agar bekhaym time out be client bedim y ro type mikonim va zaman ro be client midim
            inout_byts=input_data.encode()
            client.sendall(inout_byts)
            if input_data == "y":          
                input_data2=input("How many seconds?  ")
                inout_byts2=input_data2.encode()
                client.sendall(inout_byts2)          
            client.close()

server=server_side()
server.first_connection()

