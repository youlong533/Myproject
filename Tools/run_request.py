import requests

url = 'http://precbj.kakahui.net/liveBalance/balance'
data = {"balanceMonth":"2021-05"}
res = requests.post(url,data).json()
print(res)