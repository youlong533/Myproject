import requests

url = 'http://testsjob.kakahui.net/api/v1/fetchCampController/fetchRealTimeData'
res = requests.post(url).json()
print(res)