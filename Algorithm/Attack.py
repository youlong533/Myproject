import requests
#暴力破解登录

password_dict = []
#登录接口
login_url = ''
def attack(username):
    for password in password_dict:
        data = {'username':username,'password' : password}
        content = requests.post(login_url,data).content.decode('utf-8')
        if 'login success' in content:
            print('got it!password is: %s' %password)