from random import randint

class Apple:
    def __init__(self, game):
        self.game = game
        self.findStartPos()
        print ("apple created at " + str(self.x) + "," + str(self.y))

    def findStartPos(self):
        needNewPosition = True
        while (needNewPosition):
            self.x = randint(1, self.game.boardWidth-2)
            self.y = randint(1, self.game.boardHeight-2)
            if not self.game.isCollidingWithWallOrPlayer(self.x, self.y, False):
                needNewPosition = False