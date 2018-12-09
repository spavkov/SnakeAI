import pygame
from game.snake import SnakeGame

class SnakeGameRenderer:
    def __init__(self, game):
        self.game = game

    def initRendering(self):
        pygame.init()
        self.cellSizeInPixels = 32
        self.displayWidth = (self.game.boardWidth) * self.cellSizeInPixels
        self.displayHeight = (self.game.boardHeight) * self.cellSizeInPixels
        self.display = pygame.display.set_mode((self.displayWidth, self.displayHeight))
        self.backgroundColor = (200, 200, 200)
        self.wallColor = (0,0,200)
        self.playerColor = (100,0,200)
        self.appleColor = (0, 200, 0)


    def render(self):
        self.display.fill(self.backgroundColor)

        for cell in self.game.wallCells:
            x = cell[0]
            y = cell[1]
            screenX = x * self.cellSizeInPixels
            screenY = y * self.cellSizeInPixels
            pygame.draw.rect(self.display, self.wallColor, (screenX, screenY, screenX + self.cellSizeInPixels, self.cellSizeInPixels), 0)

        for cell in self.game.player.cells:
            x = cell[0]
            y = cell[1]
            screenX = x * self.cellSizeInPixels
            screenY = y * self.cellSizeInPixels
            pygame.draw.rect(self.display, self.playerColor, (screenX, screenY, self.cellSizeInPixels, self.cellSizeInPixels), 0)

        appleX = self.game.apple.x
        appleY = self.game.apple.y
        screenX = appleX * self.cellSizeInPixels
        screenY = appleY * self.cellSizeInPixels

        pygame.draw.rect(self.display, self.appleColor, (screenX, screenY, self.cellSizeInPixels, self.cellSizeInPixels), 0)
        pygame.display.flip()
        pygame.time.Clock().tick(30)

