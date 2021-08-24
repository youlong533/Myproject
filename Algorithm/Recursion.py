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

# drawTree()

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def sierpinski(points, degree, myTurtle):
    colormap = ['blue','red','green','white','yellow','violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree in range(6):
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree - 1, myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree - 1, myTurtle)
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree - 1, myTurtle)

# myTurtle = Turtle()
# myWin = myTurtle.getscreen()
# myPoints = [(-500,-250),(0,500),(500,-250)]
# sierpinski(myPoints, 6 ,myTurtle)
# myWin.exitonclick()

def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height -1, fromPole, toPole, withPole)
        moveDisk(fromPole, toPole)
        moveTower(height -1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)

def searchFrom(maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)
    #检查基本请客
    #1.遇到墙
    if maze[startRow][startColumn] == OBSTACLE:
        return False
    #2.遇到已经走过的格子
    if maze[startRow][startColumn] == TRIED:
        return False
    #3.找到出口
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow,startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow,startColumn, TRIED)

    #否则，一次尝试四个方向移动
    found = searchFrom(maze, startRow - 1, startColumn) or \
            searchFrom(maze, startRow + 1, startColumn) or \
            searchFrom(maze, startRow, startColumn -1 ) or \
            searchFrom(maze, startRow, startColumn +1 )
    if found:
        maze.updatePosition(startRow,startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow,startColumn, DEAD_END)
    return found

class Maze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.starRow = rowsInMaze
                    self.starCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = Turtle(shape='turtle')
        setup(width = 600, height = 600)
        setworldcoordinates(-(columnsInMaze -1)/2-.5,-(rowsInMaze - 1)/2-.5,(columnsInMaze - 1)/2+.5,(rowsInMaze -1)/2+.5)

    def drawMaze(self):
        for y in range(self.rowsInMaze):
            for x in range (self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate, 'tan')
        self.t.color('black', 'blue')

    def drawCenteredBox(self, x, y, color):
        tracer(0)
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color('black',color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        update()
        tracer(1)

    def moveTurtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x +self.xTranslate,-y+self.yTranslate))
        self.t.goto(x +self.xTranslate, -y+self.yTranslate)

    def dropBreadcrumb(self, color):
        self.t.dor(color)

    def updatePosition(self, row, col, val = None):
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self, row, col):
        return (row == 0 or row == self.rowsInMaze-1 or col == 0 or col == self.columnsInMaze-1)

    def __getitem__(self, idx):
        return self.mazelist[idx]