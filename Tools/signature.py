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
        # （
        # 各端的私密不一致，
        #
        # APP：48119cfa053bb95313b6c4aacbfcffb1728e4e3c
        #
        # H5：4c77e2945b5bd2cecf8dd983ee7531d98d9565f1
        #
        # wechat：29fcab89ba4e73a60b50402801070f33c3a3aa1a
        #
        # Manager：8f86e4afab8c60cdabf15d238e8f270f995b1c90
        #
        # wechat - app：263ae9332b1a36c8cd12f907174a016280b67f81
        # ）
        self.key = "56255fde5b5bd28dd983ee7531d98d9565f2"


    #组装签名字符串
    def str_url(self,token,data):
        print(type(data))
        str_url = str(self.time)+token+self.key+self.p(data)
        return str_url
    #生成签名
    def sign(url):
        m = hashlib.md5()
        m.update(url.encode('utf-8'))
        sign = m.hexdigest()
        return sign

    def s(self,token,data):
        s = signature()
        url = s.str_url(token,data)
        sign = signature.sign(url)
        return sign
    #参数组成字符串
    def p(self,data):
        # print(type(data))
        param = ''
        for key in data.keys():
            v = data[key]
            param = param+key+str(v)
        return param

if __name__ == '__main__':
    token = '53680117e00b483a323b8930a2379251'
    data = {
            "campDateId":"345718657178255935",
            "classId":"",
            "groupId":"",
            "pageNo":1,
            "pageSize":20,
            "tagType":"",
            "orderBy":"selfTag"
            }
    Si = signature()
    # ul = Si.str_url(token,param)
    s=Si.s(token,data)
    print(s)


#将timestamp和signature数据存入CSV文件中
# csv_file = open('E:\\params\\order.csv','w',newline='',encoding='utf-8')
# write = csv.writer(csv_file)
# write.writerow(['timestamp','token','signature'])
# write.writerow([signature.timestamp,signature.token,signature().s()])