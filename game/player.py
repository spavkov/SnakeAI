class PlayerDirection:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class PlayerMove:
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    NONE = 5

class Player:
    def __init__(self, game):
        self.cells = [[10,10]]
        self.direction = PlayerDirection.UP
        print ("Player created at " + str(self.cells[0][0]) + "," + str(self.cells[0][1]))

    def grow(self):
        if (self.direction == PlayerDirection.UP):
            currentY = self.cells[0][1]
            newHead = [self.cells[0][0], currentY - 1]
            self.cells.insert(0, newHead)
        elif (self.direction == PlayerDirection.DOWN):
            currentY = self.cells[0][1]
            newHead = [self.cells[0][0], currentY + 1]
            self.cells.insert(0, newHead)
        elif (self.direction ==  PlayerDirection.LEFT):
            currentX = self.cells[0][0]
            newHead = [currentX - 1,self.cells[0][1]]
            self.cells.insert(0, newHead)
        elif (self.direction ==  PlayerDirection.RIGHT):
            currentX = self.cells[0][0]
            newHead = [currentX + 1,self.cells[0][1]]
            self.cells.insert(0, newHead)