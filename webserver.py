# WEBSERVER with SSL support
# Create certificate files ca_key.pem and ca_cert.pem and they should be in the same folder

# Output when client connects:
# Web Server at => 192.168.1.100:4443
# 192.168.1.22 - - [12/Feb/2022 02:32:56] "GET /default.html HTTP/1.1" 200 -
import http.server
import ssl

HOST = '192.168.1.100'
PORT = 4443
Handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer((HOST, PORT), Handler) as httpd:
    print("Web Server at => " + HOST + ":" + str(PORT))
    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="ca_key.pem", certfile="ca_cert.pem", server_side=True)
    httpd.serve_forever()
    