# Python Web Server with SSL Support
There are times when you need a simple but working web server with SSL support.  
In my case I needed it for OTA (Over The Air) update support for my device I was working on, so here it is short and sweet!

## Step 1: Create Self Signed SSL certificate for your server including its key file  
Make sure you have openssl installed and accessible. Then type the following command
> openssl req -x509 -newkey rsa:2048 -keyout ca_key.pem -out ca_cert.pem -days 365 -nodes

Fill all the required things when prompted  
When asked for common name, use the IP address of your machine (eg. 192.168.1.100)

## Step 2: Paste the following webserver code in a webserver.py file

```python
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
    print("Web Server listening at => " + HOST + ":" + str(PORT))
    sslcontext = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    sslcontext.load_cert_chain(keyfile="ca_key.pem", certfile="ca_cert.pem")
    httpd.socket = sslcontext.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()
```
## Step 3:
Create a default.html file in the folder with some HTML content.

## Step 4:
Make sure you have installed python and it works from your command line. Then run the webserver.py file

## Step 5: 
Open a web browser and goto https://192.168.1.100:4443/default.html

> Keep in mind, your web browser will show warning since its a self-signed certificate, which you can ignore for this case.

