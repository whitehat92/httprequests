import requests
import urllib.request

schemaprompt = str(input("With schema (http or https)?(y/n)  "))
host = input("Enter domain or IP: ")
headers = { 'user-agent': 'Mozilla/10.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Origin':,}
def codigos():
    if pedido == 200:
        print("200 OK")
        print(cabeca)
    if pedido == 404:
        print("404 NOT FOUND")
    if pedido == 403:
        print("403 FORBIDDEN")
    if pedido == 301:
        print ("301 FOUND")
    if pedido == 401:
        print ("401 UNAUTHORIZED")
        print(cabeca)
        # print(cabecaHTTPS)
    if pedido == 405:
        print ("405 METHOD NOT ALLOWED")
        print(cabeca)
    else:
        print(pedido)
        print(cabeca)
if schemaprompt == "n":
    send = requests.get(url = "https://" + host + "/", headers = headers)
    pedido = send.status_code
    cabeca = send.headers
    codigos()
if schemaprompt == "y" or schemaprompt == "":
    if "https" or "http" in str(host):
        send = requests.get(url = str(host), headers = headers)
        pedido = send.status_code
        cabeca = send.headers
        codigos()
    if not "https" or "http" in str(host):
        host = input("Enter without schema: ")
        send = requests.get(url=str(host), headers=headers)
        pedido = send.status_code
        cabeca = send.headers
        codigos()
