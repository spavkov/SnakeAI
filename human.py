from game.snake import SnakeGame
from game.renderer import SnakeGameRenderer
from random import randint

if __name__ == "__main__":
    game = SnakeGame()
    renderer = SnakeGameRenderer(game)
    renderer.initRendering()
    game.start()
    for _ in range(20000):
        renderer.render()
        if game.readyToMove():
            (gameOver, score) = game.step(randint(1,2))
            if gameOver:
                print ("Game over. Score: " + str(score))
                break