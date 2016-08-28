
# coding: utf-8

# In[1]:

# Wang Tile Random Background Generator
# Author: Lauren Ferrara

from graphics import *
import random

win = GraphWin('Wang Tiles', 1200, 660) # give title and dimensions

class Tile():

    def __init__(self, num):
        
        self.num = num
    
        if self.num == 0:
            self.left = "blue"
            self.top = "red"
            self.right = "blue"
            self.bottom = "red"

        elif self.num == 1:
            self.left = "yellow"
            self.top = "red"
            self.right = "blue"
            self.bottom = "red"

        elif self.num == 2:
            self.left = "blue"
            self.top = "red"
            self.right = "blue"
            self.bottom = "green"

        elif self.num == 3:
            self.left = "yellow"
            self.top = "red"
            self.right = "blue"
            self.bottom = "green"

        elif self.num == 4:
            self.left = "blue"
            self.top = "red"
            self.right = "yellow"
            self.bottom = "red"

        elif self.num == 5:
            self.left = "yellow"
            self.top = "red"
            self.right = "yellow"
            self.bottom = "red"

        elif self.num == 6:
            self.left = "blue"
            self.top = "red"
            self.right = "yellow"
            self.bottom = "green"

        elif self.num == 7:
            self.left = "yellow"
            self.top = "red"
            self.right = "yellow"
            self.bottom = "green"

        elif self.num == 8:
            self.left = "blue"
            self.top = "green"
            self.right = "blue"
            self.bottom = "red"

        elif self.num == 9:    
            self.left = "yellow"
            self.top = "green"
            self.right = "blue"
            self.bottom = "red"

        elif self.num == 10:
            self.left = "blue"
            self.top = "green"
            self.right = "blue"
            self.bottom = "green"

        elif self.num == 11:     
            self.left = "yellow"
            self.top = "green"
            self.right = "blue"
            self.bottom = "green"

        elif self.num == 12:
            self.left = "blue"
            self.top = "green"
            self.right = "yellow"
            self.bottom = "red"

        elif self.num == 13: 
            self.left = "yellow"
            self.top = "green"
            self.right = "yellow"
            self.bottom = "red"

        elif self.num == 14:
            self.left = "blue"
            self.top = "green"
            self.right = "yellow"
            self.bottom = "green"

        elif self.num == 15:
            self.left = "yellow"
            self.top = "green"
            self.right = "yellow"
            self.bottom = "green"
    
    def getLeft(self):
        return self.left
    
    def getTop(self):
        return self.top
    
    def getRight(self):
        return self.right
    
    def getBottom(self):
        return self.bottom
     
    def draw(self, leftSide, topSide):
        #left
        rect1 = Rectangle(Point(leftSide, topSide + 10), Point(leftSide + 10, topSide + 50))
        rect1.setFill(self.left)
        rect1.setOutline(self.left)
        rect1.draw(win)
        #top
        rect2 = Rectangle(Point(leftSide + 10, topSide), Point(leftSide + 50, topSide + 10))
        rect2.setFill(self.top)
        rect2.setOutline(self.top)
        rect2.draw(win)
        #bottom
        rect3 = Rectangle(Point(leftSide + 10, topSide + 50), Point(leftSide + 50, topSide + 60))
        rect3.setFill(self.bottom)
        rect3.setOutline(self.bottom)
        rect3.draw(win)
        #right
        rect4 = Rectangle(Point(leftSide + 50, topSide + 10), Point(leftSide + 60, topSide + 50))
        rect4.setFill(self.right)
        rect4.setOutline(self.right)
        rect4.draw(win)
    
tileRow = [[None for i in range(20)] for j in range(11)]      
        
first = random.randrange(0,16)
tile = Tile(first)
tile.draw(0,0)

tileRow[0][0] = tile

# display first row
for j in range(1, 20):   
    good = 0
    while not good:
        number = random.randrange(0,16)
        tile = Tile(number)
        if tile.getLeft() == tileRow[0][j - 1].getRight():
            good = 1
            tileRow[0][j] = tile
            tile.draw(j * 60, 0)

for i in range(1, 11):
    # new row, 1st col            
    good = 0  
    while not good:
        number = random.randrange(0,16)
        tile = Tile(number)
        if tile.getTop() == tileRow[i - 1][0].getBottom():
            good = 1
            tileRow[i][0] = tile
            tile.draw(0, i * 60)   

    # remainder of row
    for j in range(1, 20): 
        good = 0  
        while not good:
            number = random.randrange(0,16)
            tile = Tile(number)
            if tile.getLeft() == tileRow[i][j - 1].getRight() and tile.getTop() == tileRow[i - 1][j].getBottom():
                good = 1
                tileRow[i][j] = tile
                tile.draw(j * 60, i * 60)  


# In[2]:

# Wang Tiles to Simulate Turing Machine for Binary Complement
# Author: Lauren Ferrara

from graphics import *
import random

win = GraphWin('Wang Tiles', 1080, 660) # give title and dimensions

class Tile():

    def __init__(self, num):
        
        self.num = num
        self.left = ''
        self.right = ''
        self.top = ''
        self.bottom = ''

    def getLeft(self):
        return self.left
    
    def getTop(self):
        return self.top
    
    def getRight(self):
        return self.right
    
    def getBottom(self):
        return self.bottom
     
    def draw(self, leftSide, topSide):
        #left
        rect1 = Rectangle(Point(leftSide, topSide + 10), Point(leftSide + 10, topSide + 50))
        rect1.setFill(self.left)
        #rect1.setOutline(self.left)
        rect1.draw(win)
        #top
        rect2 = Rectangle(Point(leftSide + 10, topSide), Point(leftSide + 50, topSide + 10))
        rect2.setFill(self.top)
        #rect2.setOutline(self.top)
        rect2.draw(win)
        #bottom
        rect3 = Rectangle(Point(leftSide + 10, topSide + 50), Point(leftSide + 50, topSide + 60))
        rect3.setFill(self.bottom)
        #rect3.setOutline(self.bottom)
        rect3.draw(win)
        #right
        rect4 = Rectangle(Point(leftSide + 50, topSide + 10), Point(leftSide + 60, topSide + 50))
        rect4.setFill(self.right)
        #rect4.setOutline(self.right)
        rect4.draw(win)

class alphaTile(Tile):

    def __init__(self, num):
        Tile.__init__(self, num)
    
        if self.num == 0:
            self.left = "red"
            self.top = "black"
            self.right = "red"
            self.bottom = "black"

        elif self.num == 1:
            self.left = "blue"
            self.top = "black"
            self.right = "blue"
            self.bottom = "black"

        elif self.num == 2:
            self.left = "purple"
            self.top = "black"
            self.right = "purple"
            self.bottom = "black"            
            
class transitionTile(Tile):

    def __init__(self, num):
        
        Tile.__init__(self, num)
    
        # transition from A,0 to 1
        if self.num == 0:
            self.left = "orange"
            self.top = "black"
            self.right = "blue"
            self.bottom = "yellow"

        # transition from A,1 to 0
        elif self.num == 1:
            self.left = "green"
            self.top = "black"
            self.right = "red"
            self.bottom = "yellow"
        
        # transition out of start state
        if self.num == 2:
            self.left = "orange"
            self.top = "black"
            self.right = "black"
            self.bottom = "yellow"
        
class mergeTile(Tile):

    def __init__(self, num):
        Tile.__init__(self, num)        
        self.num = num
    
        if self.num == 0:
            self.left = "red"
            self.top = "yellow"
            self.right = "orange"
            self.bottom = "black"

        elif self.num == 1:
            self.left = "blue"
            self.top = "yellow"
            self.right = "green"
            self.bottom = "black"
            
        elif self.num == 2:
            self.left = "purple"
            self.top = "yellow"
            self.right = "pink"
            self.bottom = "black"
        
class startTile(Tile):

    def __init__(self, num):
        Tile.__init__(self, num)       
        self.num = num
    
        # start state
        if self.num == 0:
            self.left = "black"
            self.top = "brown"
            self.right = "orange"
            self.bottom = "brown"
        
        # below start state, 0
        elif self.num == 1:
            self.left = "black"
            self.top = "brown"
            self.right = "red"
            self.bottom = "brown"
    
        # below start state, 1
        elif self.num == 2:
            self.left = "black"
            self.top = "brown"
            self.right = "blue"
            self.bottom = "brown"
        
        # below start state, 0
        elif self.num == 3:
            self.left = "black"
            self.top = "brown"
            self.right = "red"
            self.bottom = "brown"
    
        # below start state, 1
        elif self.num == 4:
            self.left = "black"
            self.top = "brown"
            self.right = "blue"
            self.bottom = "brown"
            
        # below start state, blank symbol (end of input string)
        elif self.num == 5:
            self.left = "black"
            self.top = "brown"
            self.right = "purple"
            self.bottom = "brown" 
        
class acceptTile(Tile):

    def __init__(self, num):
        Tile.__init__(self, num)        
        self.num = num
    
        if self.num == 0:
            self.left = "pink"
            self.top = "black"
            self.right = "black"
            self.bottom = "black"
            
tileCol = [[None for i in range(18)] for j in range(11)]      

start = random.randrange(0,9) # where start state should be placed
tileCol[0][0] = startTile(0)
tileCol[0][0].draw(0,0)

end = 10
i = 1
# place tiles below start state
while i < 11:
    if i == 10:
        tileCol[i][0] = startTile(5)
        tileCol[i][0].draw(0, i * 60)
    else:
        start = random.randrange(1, 6)
        tileCol[i][0] = startTile(start)
        tileCol[i][0].draw(0, i * 60)
        if start == 5:
            end = i
            i = 11
    i = i + 1

halt = 0


for j in range(1, 18):
    
    if not halt:

        # place first tile in next column
        if j == 1:
            i = 0
            tileCol[0][j] = transitionTile(2)
            tileCol[0][j].draw(j * 60, 0)
        else:
            i = 1
            if tileCol[i][j - 1].getRight() == 'red':
                tileCol[i][j] = alphaTile(0)
                tileCol[i][j].draw(j * 60, i * 60)

            elif tileCol[i][j - 1].getRight() == 'blue':
                tileCol[i][j] = alphaTile(1)
                tileCol[i][j].draw(j * 60, i * 60)

            elif tileCol[i][j - 1].getRight() == 'orange':
                tileCol[i][j] = transitionTile(0)
                tileCol[i][j].draw(j * 60, i * 60)

            elif tileCol[i][j - 1].getRight() == 'green':
                tileCol[i][j] = transitionTile(1)
                tileCol[i][j].draw(j * 60, i * 60)

            elif tileCol[i][j - 1].getRight() == 'pink':
                tileCol[i][j] = acceptTile(0)
                tileCol[i][j].draw(j * 60, i * 60)
                halt = 1
                break

            elif tileCol[i][j - 1].getRight() == 'cyan':
                tileCol[i][j] = acceptTile(0)
                tileCol[i][j].draw(j * 60, i * 60)
            
   
        while i < end:    
            # place rest of column
            if tileCol[i + 1][j - 1].getRight() == 'red' and tileCol[i][j].getBottom() == 'black':
                tileCol[i + 1][j] = alphaTile(0)
                tileCol[i + 1][j].draw(j * 60, (i + 1) * 60)

            elif tileCol[i + 1][j - 1].getRight() == 'blue' and tileCol[i][j].getBottom() == 'black':
                tileCol[i + 1][j] = alphaTile(1)
                tileCol[i + 1][j].draw(j * 60, (i + 1) * 60)

            elif tileCol[i + 1][j - 1].getRight() == 'purple' and tileCol[i][j].getBottom() == 'black':
                tileCol[i + 1][j] = alphaTile(2)
                tileCol[i + 1][j].draw(j * 60, (i + 1) * 60)            

            elif tileCol[i + 1][j - 1].getRight() == 'orange':
                tileCol[i + 1][j] = transitionTile(0)
                tileCol[i + 1][j].draw(j * 60, (i + 1) * 60)

            elif tileCol[i + 1][j - 1].getRight() == 'green':
                tileCol[i + 1][j] = transitionTile(1)
                tileCol[i + 1][j].draw(j * 60, (i + 1) * 60)

            elif tileCol[i + 1][j - 1].getRight() == 'pink':
                tileCol[i + 1][j] = acceptTile(0)
                tileCol[i + 1][j].draw(j * 60, (i + 1) * 60)
                halt = 1
                break

            elif tileCol[i + 1][j - 1].getRight() == 'red' and tileCol[i][j].getBottom() == 'yellow':
                tileCol[i + 1][j] = mergeTile(0)
                tileCol[i + 1][j].draw(j * 60, (i + 1) * 60)

            elif tileCol[i + 1][j - 1].getRight() == 'blue' and tileCol[i][j].getBottom() == 'yellow':
                tileCol[i + 1][j] = mergeTile(1)
                tileCol[i + 1][j].draw(j * 60, (i + 1) * 60)

            elif tileCol[i + 1][j - 1].getRight() == 'purple':
                tileCol[i + 1][j] = mergeTile(2)
                tileCol[i + 1][j].draw(j * 60, (i + 1) * 60)

            i = i + 1
    
    else:
        break


# In[ ]:



