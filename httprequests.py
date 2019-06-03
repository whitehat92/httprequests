import requests

host = str(input("Enter domain or IP: "))
send = requests.get("http://" + host + "/")
pedido = send.status_code
cabeca = send.headers
if pedido == 200:
    print("200 OK")
    print(cabeca)
if pedido == 400:
    print("400 NOT FOUND")
if pedido == 403:
    print("403 FORBIDDEN")
if pedido == 301:
    print ("301 FOUND")
