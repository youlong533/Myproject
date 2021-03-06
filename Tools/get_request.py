# _*_ coding:utf8 _*_
import  requests
import  json
from Myproject.Tools import signature

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
    param = "campDateId" + "345718657178255935" + "classId" + "" + "groupId" + "" + "pageNo" + "1" + "pageSize" + "20" + "tagType" + "" + "orderBy" + "selfTag"
    token = 'c673018d7ed9b1f6b96645c9158c9f40'
    S = signature.signature()
    sign = S.s(param,token)
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'token': token,
        'signature':sign
}
    url = 'https://presmartapi.kakahui.net/knowledge-smart-crm/api/v1/realTimeKanBan/queryHitKeyWordsList'
    data = {"campDateId":"345718657178255935","classId":"","groupId":"","pageNo":1,"pageSize":20,"tagType":"","orderBy":"selfTag"}
    data = json.dumps(data,ensure_ascii=False).encode('utf8').decode('latin1')
    run = RunMain(headers,url,'get',data)
#    res = RunMain.send_post(data,url)
#    print(res)
#     print(run.res)

    u_test = 'http://testsjob.kakahui.net/api/v1/fetchCampController/fetchRealTimeData'
    # data_test = {'type': '1',
    #              'packageId': '353254591846445079',
    #              'proCode': 'WM180F',
    #              'classId': '351404578921033923',
    #              'wechatType': '1',
    #              'scanQr': '1',
    #              'qrCodeType': '0'
    #              }
    data_test = {}
    run_test = RunMain(headers, u_test, 'post', data_test)
    print(run_test.res)