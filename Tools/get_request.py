# _*_ coding:utf8 _*_
import  requests
import  json

class RunMain:
    # 实例初始化
    def __init__(self,headers,u,method,data=None):
        self.res = self.run_main(headers,u,method,data)

    # 封装一个get方法
    def send_get(self,headers,u,data):
        res = requests.get(headers=headers,url=u,data=data).json()
        return res

    # 封装一个post方法
    def send_post(self,headers,u,data=None):
        res = requests.post(headers=headers,url=u,data=data).json()
#        return json.dumps(res,indent=2,sort_keys=True)
        return res

    # 写一个方法，判断是get的话调用get请求，是post的话调用post请求
    def run_main(self,headers,u,method,data=None):
        res = None
        if method == 'get':
            res = self.send_get(headers,u,data)
        else:
            res = self.send_post(headers,u,data)
        return res


if __name__ == '__main__':
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    url = 'http://testsmart.kakahui.net/api/v1/copyWxName/reportCopyWxName'
    data = {'customerId':'19900328','wechatName':"游龙",'saleId':2,'kanbanType':1}
    data = json.dumps(data,ensure_ascii=False).encode('utf8').decode('latin1')
    run = RunMain(headers,url,'get',data)
#    res = RunMain.send_post(data,url)
#    print(res)
    print(run.res)