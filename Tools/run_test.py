from Myproject.Tools import get_request
from Myproject.Tools import signature
import json,time


u = 'http://192.168.31.186:8081/api/v1/syncSaleBalance/doSync'   #销售额跑批
u_1= 'http://192.168.26.150:8081/api/v1/syncSaleBalance/syncBalanceConfigStatus'      #配置状态跑批  192.168.26.150
u_2 = 'http://192.168.31.186:8081/api/v1/syncRefundOrderController/syncRefund' #退款跑批
u_3 = 'http://192.168.26.150:8081/api/v1/syncSaleBalance/doSyncHistory' #历史期外数据跑批
u_4 = 'http://precbj.kakahui.net/liveBalance/balance' #销售结算job
data = {
    "beginTime" : "2020-09-01",
    "endTime" : "2020-09-30"
}
data1 =  {"dayTime":"2020-09-01"}
# data = json.dumps(data,ensure_ascii=False).encode('utf8').decode('latin1')
data = json.dumps(data)
# data1 = json.dumps(data1,ensure_ascii=False).encode('utf8').decode('latin1')
data1 = json.dumps(data1)
data4 = {"balanceMonth":"2021-05"}
data4= json.dumps(data4)
headers = {
        'Content-Type': 'application/json;charset=UTF-8'
}
# run = get_request.RunMain(headers,u,'post',data)
# print(run.res)
# run_1 = get_request.RunMain(headers,u_1,'get',None)
# print(run_1.res)
# run_2 = get_request.RunMain(headers,u_2,'post',data1)
# print(run_2.res)
# run_3 = get_request.RunMain(headers,u_3,'post',data)
# print(run_3.res)
run_4 = get_request.RunMain(headers,u_4,'post',data4)
print(run_4.res)
