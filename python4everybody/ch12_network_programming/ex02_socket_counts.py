import socket

url = input('Enter url: ')
url_lst = url.split('/')
host = url_lst[2]

# print(host)

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

    counts = 0
    while True:
        data = mysock.recv(1024)
        counts += len(data)
        if (len(data) < 1):
            break

        if counts < 3001:
            print(data.decode(), end='')

    mysock.close()
    print('\n')
    print('Counts:', counts)
except:
    print('Please input a correct url!')
    exit()
