# _*_coding:utf-8 _*_

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    i = 0
    while low <=high:
        mid = int((low + high) / 2)
        guess = list[mid]
        i = i+1
        if guess > item:
            high = mid - 1
        elif guess == item:
            return i
        else:
            low = mid + 1
    return None

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,29]
item = int(input("请输入要猜的数字："))
print("需要%s次猜对" %binary_search(list1,item))

