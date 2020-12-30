#关闭订单接口
from AutoTest.util.runmethod import RunMethod
import json

host = 'https://testcbai.kakahui.net'
link = '/api/v1/orderChange/orderClose'

url = host + link
data = {
"payOrderId":"421617412807942285"
}
p = json.dumps(data)

run = RunMethod()
re = run.run_method('post',url,data)
print(re)