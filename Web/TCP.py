import socket as sc


def TCPserver(h, p, f, d=False):
    '''TODO:TCPsocket'''
    w = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
    w.bind((h, p))
    print('Server at host '+h+' port '+str(p) +' waiting for clients...'if d else '')
    w.listen(8)
    if w.accept():
        print('Server at host '+h+' port ' +str(p)+' found clients!'if d else '')
        while True:
            c, addr = w.accept()
            # Package(s) size limit:1mB
            c.sendall(f(c.recv(1048576).decode()).encode())
            c.close()
    else:
        print('Server at host '+h+' port '+str(p) +' hasn\'t found clients!Trying again...'if d else '')
        TCPserver(h, p, f)  # Trying again...


def TCPclient(h, p, f, d=False):
    '''TODO:TCPsocket'''
    while True:
        w = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        w.connect((h, p))
        print('Client at host '+h+' port '+str(p) +' waiting for servers...'if d else '')
        if w:
            print('Client at host '+h+' port ' +str(p)+' found servers!'if d else '')
            # Package(s) size limit:1mB
            w.send(f(w.recv(1048576).decode()).encode())
            w.close()
        else:
            print('Client at host '+h+' port '+str(p) +' hasn\'t found servers!Trying again...'if d else '')
