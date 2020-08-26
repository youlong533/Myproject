import base64,hashlib
import time

# 生成签名
# 签名规则如下： str = 请求参数进行顺序排列再进行拼接
# sign = md5(base64(timestamp) + token + 私密 + str)
#
# @ param
# request
# HTTP请求
# @ return 签名
class signature:
    def __init__(self):
        self.timestamp = str(int(time.time()))
        self.time = base64.b64encode(bytes(self.timestamp.encode('utf-8')))
        # 私密
        self.key = "56255fde5b5bd28dd983ee7531d98d9565f2"


    #组装签名字符串
    def str_url(self,token,param):
        str_url = str(self.time)+token+self.key+param
        return str_url
    #生成签名
    def sign(url):
        m = hashlib.md5()
        m.update(url.encode('utf-8'))
        sign = m.hexdigest()
        return sign

    def s(self,token,param):
        s = signature()
        url = s.str_url(token,param)
        sign = signature.sign(url)
        return sign

if __name__ == '__main__':
    token = '53680117e00b483a323b8930a2379251'
    param = "campDateId" + "345718657178255935" + "classId" + "" + "groupId" + "" + "pageNo" + "1" + "pageSize" + "20" + "tagType" + "" + "orderBy" + "selfTag"
    Si = signature()
    # ul = Si.str_url(token,param)
    s=Si.s(token,param)
    print(s)


#将timestamp和signature数据存入CSV文件中
# csv_file = open('E:\\params\\order.csv','w',newline='',encoding='utf-8')
# write = csv.writer(csv_file)
# write.writerow(['timestamp','token','signature'])
# write.writerow([signature.timestamp,signature.token,signature().s()])