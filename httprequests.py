import requests

host = str(input("Enter domain or IP: "))
send = requests.get("http://" + host + "/")
pedido = send.status_code
#add "http://" prefix

if pedido == 200:
    print("200 OK")
if pedido == 400:
    print("400 NOT FOUND")
