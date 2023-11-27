import socket

HOST = '172.20.10.3'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    conn, addr = s.accept()
    print('add connected by ' + str(addr))

    while True:
        indata = conn.recv(1024)
        if len(indata) == 0: # connection closed
            conn.close()
            print('client closed connection.')
            break
        print('recieved from ',addr,":", indata.decode())
        fib = [0,1]
        n = int(indata.decode())+1
        if n > 2:
            for i in range(2,n,1):
                sum = fib[i-2]+fib[i-1]
                fib.append(sum)
        output = str(fib[n-1])
        print('send to  ',addr,":",output)
        conn.send(output.encode())
s.close()
