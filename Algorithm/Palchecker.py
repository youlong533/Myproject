from pythonds.basic import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and  stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

if __name__ == '__main__':
    r1 = palchecker("toot")
    r2 = palchecker("123465")
    print(r1,r2)