import socket

HOST = '172.20.10.3'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("connect to",HOST)
while True:
    outdata = input('the fabonacci f(n) when n = ')
    if outdata == "exit":
        s.close()
        print("connection close.")
        break
    else:
        print('send: ' + outdata)
        s.send(outdata.encode())
        indata = s.recv(1024)
        if len(indata) == 0: # connection closed
            s.close()
            print('server closed connection.')
            break
        print('f(n) is ' + indata.decode())
    