from pythonds.basic import Queue

def Killer(list, num):
    simqueue = Queue()
    for i in list:
        simqueue.enqueue(i)

    while simqueue.size() > 1:
        for n in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()
        # print(simqueue.dequeue())

    return simqueue.dequeue()

l = range(1,40)

re = Killer(l,7)
print(re)