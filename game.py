import pygame
import math
from random import randrange
import random
import copy
import os

# paths
board = ".../assets/board/"
text = ".../assets/text/"
data = ".../assets/data/"
element = ".../assets/elements/"

# board

board = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,2,3],
    [3,6,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,6,3],
    [3,2,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,2,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3,2,3],
    [3,2,3,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3,2,3],
    [3,2,2,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,2,2,3],
    [3,3,3,3,3,3,2,3,3,3,3,3,1,3,3,1,3,3,3,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,3,3,3,1,3,3,1,3,3,3,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,1,1,1,1,1,1,1,1,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,3,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,4,4,4,4,4,4,3,1,3,3,2,3,3,3,3,3,3],
    [1,1,1,1,1,1,2,1,1,1,3,4,4,4,4,4,4,3,1,1,1,2,1,1,1,1,1,1], 
    [3,3,3,3,3,3,2,3,3,1,3,4,4,4,4,4,4,3,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,3,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,1,1,1,1,1,1,1,1,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,3,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,3,1,3,3,2,3,3,3,3,3,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,2,3],
    [3,2,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,2,3],
    [3,6,2,2,3,3,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,3,3,2,2,6,3],
    [3,3,3,2,3,3,2,3,3,2,3,3,3,3,3,3,3,3,2,3,3,2,3,3,2,3,3,3],
    [3,3,3,2,3,3,2,3,3,2,3,3,3,3,3,3,3,3,2,3,3,2,3,3,2,3,3,3],
    [3,2,2,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,2,2,3],
    [3,2,3,3,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,3,3,2,3],
    [3,2,3,3,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,3,3,2,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
]

# display game screen and size of each square
gameBoard = copy.deepcopy(originalGameBoard)
spriteRatio = 3/2
square = 25
spriteOffset = square * (1 - spriteRatio) * (1/2)
(width, height) = (len(gameBoard[0]) * square, len(gameBoard) * square)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()


# game
class game:
    def __init__(self, level, score):
        self.paused = True
        self.ghostsDelays = 1
        self.ghostsCount = 0
        self.pacmanDelays = 1
        self.pacmanCount = 0
        self.timerDelay = 10
        self.timerCount = 0
        self.ghostsAttack = False
        self.highScore = self.getHighScore()
        self.score = score
        self.level = level
        self.lives = 3
        self.ghosts = [Ghost(15.0, 14.5, "red", 0), Ghost(18.0, 12.5, "blue", 1), Ghost(18.0, 14.5, "pink", 2), Ghost(18.0, 16.5, "orange", 3)]
        self.pacman = Pacman(27.0, 14.5) # pacman starts in the of the board
        self.total = self.getCount()
        self.ghostScore = 150
        self.levels = [[300, 200], [100, 400], [100, 400], [0, 500]]
        random.shuffle(self.levels)


        # index and progress levels
        self.ghostStatus = [[1, 0], [0, 0], [1, 0], [0, 0]]
        index = 0
        for status in self.ghostStatus:
            status[0] = randrange(2)
            status[1] = randrange(self.levels[index][status[0]] + 1)
            index += 1
        self.collect = 0
        self.start = False
        self.gameOver = False
        self.gameOverRestartScore = 0
        self.points = []
        self.pointsTimer = 10

        # berries
        self.berryStatus = [150, 350, False]
        self.berryLocation = [21.0, 14.5]
        self.berries = ["tile080.png", "tile081.png", "tile082.png", "tile083.png", "tile084.png", "tile085.png", "tile086.png", "tile087.png"]
        self.berriesCollected = []
        self.levelTimer = 0
        self.berryScore = 100
        self.lockTimer = 100
        self.lockIn = True
        self.extraLife = False
    
    # update method
    def update(self):
        # pygame.image.unload()
        print(self.ghostStatus)
        if self.gameOver:
            self.gameOverFunction()
            return
        if self.paused or not self.started:
            self.drawTilesAround(20, 11)
            self.drawTilesAround(20, 12)
            self.drawTilesAround(20, 13)
            self.drawTilesAround(20, 14)
            self.drawTilesAround(20, 15)
            self.draw()
            pygame.display.update()
            return

        self.levelTimer += 1
        self.ghostsCount += 1
        self.pacmanCount += 1
        self.timerChangeCount += 1
        self.ghostsAttack = False

        if self.score >= 10000 and not self.extraLife:
            self.lives += 1
            self.extraLife = True
    
    # Draw tiles around ghosts and pacman
    self.clearBoard()
    for ghost in self.ghosts:
        if ghost.attack:
            self.ghostsAttack = True

    # Check if the ghost should case pacman
    index = 0
    for status in self.ghostStatus:
        status[1] += 1
        if status[1] >= self.levels[index][status[0]]:
            status[1] = 0
            status[0] += 1
            status[0] %= 2
        index += 1

    index = 0
    for ghost in self.ghosts:
        if not ghost.attack and not ghost.dead and self.ghostStatus[index][0] == 0:
            ghost.target = [self.pacman.row, self.pacman.col]
        index += 1

    if self.levelTimer == self.lockTimer:
        self.lock = False

    self.surroundings
    if self.ghostCount == self.ghostDelays:
        for ghost in self.ghosts:
            ghost.update()
        self.ghostCount = 0

    if self.timerCount == self.timerDelay:
        # color change
        self.flipColor()
        self.tictakChangeCount = 0

    if self.pacmanCount == self.pacmanDelay:
        self.pacmanCount = 0
        self.pacman.update()
        self.pacman.col %= len(gameBoard[0])
        if self.pacman.row % 1.0 == 0 and self.pacman.col % 1.0 == 0:
            if board[int(self.pacman.row)][int(self.pacman.col)] == 2:
                board[int(self.pacman.row)][int(self.pacman.col)] = 1
                self.score += 10
                self.collected += 1
                # black tile
                pygame.draw.rect(screen, (0, 0, 0), (self.pacman.col * square, self.pacman.row * square, square, square))
            elif board[int(self.pacman.row)][int(self.pacman.col)] == 5 or gameBoard[int(self.pacman.row)][int(self.pacman.col)] == 6:
                board[int(self.pacman.row)][int(self.pacman.col)] = 1
                self.collected += 1
                # Fill tile with black
                pygame.draw.rect(screen, (0, 0, 0), (self.pacman.col * square, self.pacman.row * square, square, square))
                self.score += 50
                self.ghostScore = 200
                for ghost in self.ghosts:
                    ghost.attackCount = 0
                    ghost.setAttack(True)
                    ghost.setTarget()
                    self.ghostsAttack = True
    self.surroundings()
    self.highScore = max(self.score, self.highScore)

            

# pacman

# ghosts

# game over

# display lives

# new level

# score

