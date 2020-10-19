# _*_coding:utf8 _*_
from collections import deque

#search_queue = deque()  #创建一个队列
#search_queue += graph["you"]    #将你的邻居都加入到这个搜索队列中
graph = {}
graph["you"] = ["I","me","my","he","him","his","she","her"]
graph["I"] = ["you"]
graph["me"] = ["you"]
graph["my"] = ["you"]
graph["he"] = ["you"]
graph["him"] = ["you"]
graph["his"] = ["you"]
graph["she"] = ["you"]
graph["her"] = ["you"]


def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    searched = []   #用于记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:  #仅当这个人没检查过时才检查
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person) #将这个人标记为检查过
    return False

def person_is_seller(name):
    return name[-1] == 'm'

search("you")