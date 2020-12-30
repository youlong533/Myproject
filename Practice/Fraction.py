# _*_ coding:utf-8 _*_



def Num():
    n = input("请输入分数")
    s_l = n.split('/')
    s1 = abs(int(s_l[0]))
    s2 = abs(int(s_l[1]))
    if len(s_l) == 2:
        if str(s1).isdigit() is not True:
            raise ValueError("输入的分母不正确")
        elif str(s2).isdigit() is not True:
            raise ValueError("输入的分子不正确")
        else:
            return s_l
    else:
        raise ValueError("请输入正确的分数")

def getNum():
    return Num()[0]

def getDen():
    return Num()[1]

print(getNum())
print(getDen())