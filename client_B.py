import socket as soc
import time


class client_side:
    
    def __init__(self) :
        self.ip="127.0.0.1"
        self.port="2222"
    
    def first_connection(self):
        while True:
            time.sleep(2)
            tcpsoc_cleint=soc.socket(soc.AF_INET,soc.SOCK_STREAM)
            tcpsoc_cleint.connect((self.ip,int(self.port)))
            data=tcpsoc_cleint.recv(1024).decode()
            print(data)
            if data == "y":
                data2=tcpsoc_cleint.recv(1024).decode()
                time.sleep(int(data2))    
            tcpsoc_cleint.close()


client=client_side()
client.first_connection()
