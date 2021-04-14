from pythonds.basic import Stack
from  turtle import *



# class Recursion:

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i

    return theSum

def listsum1(numList):
    if len(numList) == 1:
        return numList
    else:
        return numList[0] + listsum1(numList[1:])

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]

# print(toStr(10,2))

rStack = Stack()

def toStr1(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n % base])
        toStr1(n//base)

myTurtle = Turtle()
myWin = myTurtle.getscreen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen - 5)

# drawSpiral(myTurtle,100)
# myWin.exitonclick()

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15,t)
        t.left(40)
        tree(branchLen - 10,t)
        t.right(20)
        t.backward(branchLen)

def drawTree():
    t = Turtle()
    myWin = t.getscreen()
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.color('green')
    tree(100,t)
    myWin.exitonclick()

drawTree()