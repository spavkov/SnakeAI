from random import randint
import pygame
from game.player import Player
from game.player import PlayerDirection
from game.player import PlayerMove
from game.apple import Apple

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
            self.player.direction = PlayerDirection.LEFT
        elif (move == PlayerMove.RIGHT):
            self.player.direction = PlayerDirection.RIGHT
        elif (move == PlayerMove.UP):
            self.player.direction = PlayerDirection.UP
        elif (move == PlayerMove.DOWN):
            self.player.direction = PlayerDirection.DOWN

        self.lastCommandTime = pygame.time.get_ticks()
        self.stepCount += 1

        self.player.grow()

        if self.player.cells[0][0] == self.apple.x and self.player.cells[0][1] == self.apple.y:
            self.apple.findStartPos()
            self.score += 1
            self.player.grow()

        if len(self.player.cells) > 1:
            del (self.player.cells[0 - 1])

        self.gameOver = self.isCollidingWithWallOrPlayer(self.player.cells[0][0], self.player.cells[0][1], True)
        print("game step " + str(self.stepCount) + " score: " + str(self.score) + " blocks: " + str(len(self.player.cells)))
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