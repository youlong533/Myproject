# _*_coding:utf8 _*_
#------------------------------------------------------
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box =pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key:
                print("found the key!")

def look_for_key1(box):
    for item in box:
        if item.is_a_box:
            look_for_key(item)
        elif item.is_a_key:
            print("found the key!")
#------------------------------------------------------
def countdown(i):
    print(i)
    if i<=1:
        return
    else:
        countdown(i - 1)
#------------------------------------------------------
def greet(name):
    print("hello,"+name+"!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("how are you,"+name+"!")
def bye():
    print("ok bye!")
#------------------------------------------------------
def sum(arr):
    total = 0
    for x in arr:
        total +=x
    return total

#求和
def sum1(arr):
    if arr == [] :
        return 0
    return arr[0] + sum1(arr[1:])
#元素数
def count(list):
    if  list == []:
        return 0
    return 1 +count(list[1:])
#最大数
def max(arr):
    if len(arr) ==2:
        return arr[0] if arr[0] >arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0]>sub_max else sub_max
#二分查找
def binary_search(list,num):
    i = int(len(list)/2)
    if len(list) == 1:
        return num
    elif list[i] > num:
        return binary_search(list[:i],num)
    elif list[i] == num:
        return num
    else:
        return binary_search(list[i:],num)
