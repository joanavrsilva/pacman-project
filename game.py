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
board = copy.deepcopy(originalboard)
spriteRatio = 3/2
square = 25
spriteOffset = square * (1 - spriteRatio) * (1/2)
(width, height) = (len(board[0]) * square, len(board) * square)
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
            self.drawTiles(20, 11)
            self.drawTiles(20, 12)
            self.drawTiles(20, 13)
            self.drawTiles(20, 14)
            self.drawTiles(20, 15)
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
        self.pacman.col %= len(board[0])
        if self.pacman.row % 1.0 == 0 and self.pacman.col % 1.0 == 0:
            if board[int(self.pacman.row)][int(self.pacman.col)] == 2:
                board[int(self.pacman.row)][int(self.pacman.col)] = 1
                self.score += 10
                self.collected += 1
                # black tile
                pygame.draw.rect(screen, (0, 0, 0), (self.pacman.col * square, self.pacman.row * square, square, square))
            elif board[int(self.pacman.row)][int(self.pacman.col)] == 5 or board[int(self.pacman.row)][int(self.pacman.col)] == 6:
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

    global running
    if self.collect == self.total:
        print("New Level")
        self.level += 1
        self.newLevel()

    if self.level - 1 == 6:
        print("You win", self.level, len(self.levels))
        running = False
    self.render()       

    # Render method
    def render(self):
        screen.fill((0, 0, 0))
        currentTile = 0
        self.displayLives()
        self.displayScore()
        for i in range(3, len(board) - 2):
            for j in range(len(board[0])):
                if board[i][j] == 3: # wall
                    image = str(currentTile)
                    if len(image) == 1:
                        image = "00" + image
                    elif len(image) == 2:
                         image = "0" + image
                    # get tile image
                    image = "tile" + image + ".png"
                    tileImage = pygame.image.load(BoardPath + image)
                    tileImage = pygame.transform.scale(tileImage, (square, square))

                    # image of tile
                    screen.blit(tileImage, (j * square, i * square, square, square))

                    # pygame.draw.rect(screen, (0, 0, 255),(j * square, i * square, square, square)) # (x, y, width, height)
                elif board[i][j] == 2: # draw timer
                    pygame.draw.circle(screen, pelletColor,(j * square + square//2, i * square + square//2), square//4)
                elif board[i][j] == 5: # black timer
                    pygame.draw.circle(screen, (0, 0, 0),(j * square + square//2, i * square + square//2), square//2)
                elif board[i][j] == 6: # white timer
                    pygame.draw.circle(screen, pelletColor,(j * square + square//2, i * square + square//2), square//2)

                currentTile += 1
        
        # sprites
        for ghost in self.ghosts:
            ghost.draw()
        self.pacman.draw()
        # screen updates
        pygame.display.update()


    def render(self):
        pointsDraw = []
        for point in self.points:
            if point[3] < self.pointsTimer:
                pointsDraw.append([point[2], point[0], point[1]])
                point[3] += 1
            else:
                self.points.remove(point)
                self.drawTiles(point[0], point[1])

        for point in pointsDraw:
            self.drawPoints(point[0], point[1], point[2]) 
      
        for ghost in self.ghosts:
            ghost.draw()
        self.pacman.draw()
        self.displayScore()
        self.displayBerries()
        self.displayLives()
        self.drawBerry()
        # screen updates
        pygame.display.update()

    def boardClear(self):
            # tiles around ghosts and pacman
            for ghost in self.ghosts:
                self.drawTiles(ghost.row, ghost.col)
            self.drawTiles(self.pacman.row, self.pacman.col)
            self.drawTiles(self.berryLocation[0], self.berryLocation[1])
            self.drawTiles(21, 12)
            self.drawTiles(21, 12)
            self.drawTiles(21, 13)
            self.drawTiles(21, 14)
            self.drawTiles(21, 15)

    # see pacman status
    def surroundings(self):
        for ghost in self.ghosts:
            if self.touchPacman(ghost.row, ghost.col) and not ghost.attack:
                if self.lives == 1:
                    print("Sorry...You lose")
                    self.gameOver = True
                    # ghosts remove from the screen
                    for ghost in self.ghosts:
                        self.drawTiles(ghost.row, ghost.col)
                    self.drawTiles(self.pacman.row, self.pacman.col)
                    self.pacman.draw()
                    pygame.display.update()
                    pause(10000000)
                    return
                self.started = False
                reset()

            elif self.touchPacman(ghost.row, ghost.col) and ghost.isAttac() and not ghost.isDead():
                ghost.setDead(True)
                ghost.setTarget()
                ghost.ghostSpeed = 1
                ghost.row = math.floor(ghost.row)
                ghost.col = math.floor(ghost.col)
                self.score += self.ghostScore
                self.points.append([ghost.row, ghost.col, self.ghostScore, 0])
                self.ghostScore *= 2
                pause(10000000)

        if self.touchPacman(self.berryLocation[0], self.berryLocation[1]) and not self.berryStatus[2] and self.levelTimer in range(self.berryStatus[0], self.berryStatus[1]):
            self.berryStatus[2] = True
            self.score += self.berryScore
            self.points.append([self.berryLocation[0], self.berryLocation[1], self.berryScore, 0])
            self.berriesCollect.append(self.berries[(self.level - 1) % 8])
    
    # current score
    def displayScore(self):
        textOneUp = ["tile033.png", "tile021.png", "tile016.png"]
        textHighScore = ["tile007.png", "tile008.png", "tile006.png", "tile007.png", "tile015.png", "tile019.png", "tile002.png", "tile014.png", "tile018.png", "tile004.png"]
        index = 0
        scoreStart = 5
        highScoreStart = 11
        for i in range(scoreStart, scoreStart+len(textOneUp)):
            tileImage = pygame.image.load(TextPath + textOneUp[index])
            tileImage = pygame.transform.scale(tileImage, (square, square))
            screen.blit(tileImage, (i * square, 4, square, square))
            index += 1
        score = str(self.score)
        if score == "0":
            score = "00"
        index = 0
        for i in range(0, len(score)):
            digit = int(score[i])
            tileImage = pygame.image.load(TextPath + "tile0" + str(32 + digit) + ".png")
            tileImage = pygame.transform.scale(tileImage, (square, square))
            screen.blit(tileImage, ((scoreStart + 2 + index) * square, square + 4, square, square))
            index += 1

        index = 0
        for i in range(highScoreStart, highScoreStart+len(textHighScore)):
            tileImage = pygame.image.load(TextPath + textHighScore[index])
            tileImage = pygame.transform.scale(tileImage, (square, square))
            screen.blit(tileImage, (i * square, 4, square, square))
            index += 1

        highScore = str(self.highScore)
        if highScore == "0":
            highScore = "00"
        index = 0
        for i in range(0, len(highScore)):
            digit = int(highScore[i])
            tileImage = pygame.image.load(TextPath + "tile0" + str(32 + digit) + ".png")
            tileImage = pygame.transform.scale(tileImage, (square, square))
            screen.blit(tileImage, ((highScoreStart + 6 + index) * square, square + 4, square, square))
            index += 1

    def drawBerry(self):
        if self.levelTimer in range(self.berryState[0], self.berryState[1]) and not self.berryState[2]:
            berryImage = pygame.image.load(ElementPath + self.berries[(self.level - 1) % 8])
            berryImage = pygame.transform.scale(berryImage, (int(square * spriteRatio), int(square * spriteRatio)))
            screen.blit(berryImage, (self.berryLocation[1] * square, self.berryLocation[0] * square, square, square))


    def drawPoints(self, points, row, col):
        pointStr = str(points)
        index = 0
        for i in range(len(pointStr)):
            digit = int(pointStr[i])
            tileImage = pygame.image.load(TextPath + "tile" + str(224 + digit) + ".png")
            tileImage = pygame.transform.scale(tileImage, (square//2, square//2))
            screen.blit(tileImage, ((col) * square + (square//2 * index), row * square - 20, square//2, square//2))
            index += 1

    def drawReady(self):
        ready = ["tile274.png", "tile260.png", "tile256.png", "tile259.png", "tile281.png", "tile283.png"]
        for i in range(len(ready)):
            letter = pygame.image.load(TextPath + ready[i])
            letter = pygame.transform.scale(letter, (int(square), int(square)))
            screen.blit(letter, ((11 + i) * square, 20 * square, square, square))

    def gameOverFunction(self):
        global running
        if self.gameOverCounter == 12:
            running = False
            self.recordHighScore()
            return

# pacman

# ghosts

# game over

# display lives

# new level

# score

