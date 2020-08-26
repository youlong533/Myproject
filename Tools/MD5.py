import hashlib

def md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf8'))
    print(m.hexdigest())
    return m.hexdigest()

def md5GBK(str):
    m = hashlib.md5(str.encode(encoding = 'gb2312'))
    print(m.hexdigest())
    return m.hexdigest()

md5('123456')
md5GBK("游龙")