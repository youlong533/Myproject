import requests

def get_long_url(url):
    res = requests.head(url)
    l_url = res.headers.get('location')
    return l_url

if __name__ == '__main__':
    url = input('请输入短连接地址：')
    long = get_long_url(url)
    print(long)