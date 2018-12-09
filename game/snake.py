from random import randint
import pygame

class PlayerDirection:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class PlayerMove:
    LEFT = 1
    RIGHT = 2

class Player:
    def __init__(self, game):
        self.cells = [[10,10]]
        self.direction = PlayerDirection.UP
        print ("Player created at " + str(self.cells[0][0]) + "," + str(self.cells[0][1]))

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

class SnakeGame:
    def __init__(self, boardWidth = 16, boardHeight = 16):
        self.score = 0
        self.gameOver = False
        self.minDelayBetweenCommandsInMilliseconds = 100
        self.wallCells = []
        for x in range(0, boardWidth):
            self.wallCells.append([x, 0])
            self.wallCells.append([x, boardHeight-1])
        for y in range(0, boardHeight):
            self.wallCells.append([0, y])
            self.wallCells.append([boardWidth-1, y])
        self.cellSizeInPixels = 32
        self.stepCount = 0
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        self.player = Player(self)
        self.apple = Apple(self)
        print("game init done")

    def start(self):
        self.lastCommandTime = pygame.time.get_ticks()
        print("game started")

    def readyToMove(self):
        millisecondsSinceLastCommand = pygame.time.get_ticks() - self.lastCommandTime
        return millisecondsSinceLastCommand >= self.minDelayBetweenCommandsInMilliseconds

    def step(self, move):
        if not self.readyToMove():
            print ("not ready to move yet")
            return

        if self.gameOver:
            return

        if (move == PlayerMove.LEFT):
            if self.player.direction == PlayerDirection.UP:
                self.player.direction = PlayerDirection.LEFT
            elif self.player.direction == PlayerDirection.DOWN:
                self.player.direction = PlayerDirection.RIGHT
            elif self.player.direction == PlayerDirection.LEFT:
                self.player.direction = PlayerDirection.DOWN
            else:
                self.player.direction = PlayerDirection.UP


        if (move == PlayerMove.RIGHT):
            if self.player.direction == PlayerDirection.UP:
                self.player.direction = PlayerDirection.RIGHT
            elif self.player.direction == PlayerDirection.DOWN:
                self.player.direction = PlayerDirection.LEFT
            elif self.player.direction == PlayerDirection.LEFT:
                self.player.direction = PlayerDirection.UP
            else:
                self.player.direction = PlayerDirection.DOWN

        self.lastCommandTime = pygame.time.get_ticks()
        self.stepCount += 1

        if (self.player.direction == PlayerDirection.UP):
            currentY = self.player.cells[0][1]
            newHead = [self.player.cells[0][0], currentY - 1]
            self.player.cells.insert(0, newHead)
        elif (self.player.direction == PlayerDirection.DOWN):
            currentY = self.player.cells[0][1]
            newHead = [self.player.cells[0][0], currentY + 1]
            self.player.cells.insert(0, newHead)
        elif (self.player.direction ==  PlayerDirection.LEFT):
            currentX = self.player.cells[0][0]
            newHead = [currentX - 1,self.player.cells[0][1]]
            self.player.cells.insert(0, newHead)
        elif (self.player.direction ==  PlayerDirection.RIGHT):
            currentX = self.player.cells[0][0]
            newHead = [currentX + 1,self.player.cells[0][1]]
            self.player.cells.insert(0, newHead)

        if len(self.player.cells) > 1:
            del(self.player.cells[0-1])


        self.gameOver = self.isCollidingWithWallOrPlayer(self.player.cells[0][0], self.player.cells[0][1], True)
        print("game step " + str(self.stepCount) + " command: " + str(move) + " Game Over: " + str(self.gameOver))
        return (self.gameOver, self.score)

    def isCollidingWithWallOrPlayer(self, x, y, ignoreHead):
        for idx, playerCell in enumerate(self.player.cells):
            if ignoreHead and idx == 0:
                continue
            if playerCell[0] == x and playerCell[1] == y:
                return True
        for wallCell in self.wallCells:
            if wallCell[0] == x and wallCell[1] == y:
                return True
        return False