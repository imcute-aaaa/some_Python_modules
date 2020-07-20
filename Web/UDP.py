import socket as sc


def UDPserver(h, p, f, d=False):
    '''TODO:UDPsocket'''
    while True:
        w = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)
        w.bind((h, p))
        print('Server at host '+h+' port '+str(p) +
              ' waiting for clients...'if d else '')
        data, addr = w.recvfrom(1048576)
        print(('Server at host '+h+' port ' + str(p) +
               ' found clients!Client address %s:%s.' % addr)if d else '')
        c.sendto(f(data.decode()), addr)
        c.close()


def UDPclient(h, p, f, d=False):
    '''TODO:UDPsocket'''
    w = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)
    w.sendto('\u0006', (h, p))  # Wants your message...
    while True:
        l = f(w.recv(1024).decode())
        w = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)
        w.sendto(l, (h, p))
