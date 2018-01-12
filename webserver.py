import socket

HOST, PORT = '0.0.0.0',8080

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST,PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s' % PORT

while True:
	c, a = listen_socket.accept()
	req = c.recv(1024)
	print req

	http_response = """\
HTTP/1.1 200 Ok
HELLO WORLD!"""
	c.sendall(bytes(http_response))
	c.close()	
