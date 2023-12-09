import requests as rq

url = "http://192.168.1.109:5000/logon"  # 將 "你的主機地址" 替換為實際的主機地址

def sing_up():
    payload = {
    "username": "Testere",
    "email": "teste.e@gmail.com",
    "password": "test11223"
    }

    response = rq.post(url, json=payload)

    # 處理回應
    print(response.text)


def logon():
    payload = {
        "username": "Tester",
        "password": "test11223"
    }

    response = rq.post(url, data=payload)

    # 處理回應
    print(response.text)

logon()
