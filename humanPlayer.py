from game.snake import SnakeGame
from game.snake import PlayerMove
from game.renderer import SnakeGameRenderer
from random import randint
import pygame
from pygame.locals import *

if __name__ == "__main__":
    game = SnakeGame()
    renderer = SnakeGameRenderer(game)
    renderer.initRendering()
    game.start()
    while True:
        renderer.render()
        pygame.event.pump()


        if game.readyToMove():
            nextMove = PlayerMove.NONE
            keys = pygame.key.get_pressed()
            if (keys[K_RIGHT]):
                nextMove = PlayerMove.RIGHT
            elif (keys[K_LEFT]):
                nextMove = PlayerMove.LEFT
            elif (keys[K_UP]):
                nextMove = PlayerMove.UP
            elif (keys[K_DOWN]):
                nextMove = PlayerMove.DOWN
            elif (keys[K_ESCAPE]):
                break

            (gameOver, score) = game.step(nextMove)
            if gameOver:
                print ("Game over. Score: " + str(score))
                break
