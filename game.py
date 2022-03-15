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
                    title = pygame.image.load(BoardPath + image)
                    title = pygame.transform.scale(title, (square, square))

                    # image of tile
                    screen.blit(title, (j * square, i * square, square, square))

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
            title = pygame.image.load(TextPath + textOneUp[index])
            title = pygame.transform.scale(title, (square, square))
            screen.blit(title, (i * square, 4, square, square))
            index += 1
        score = str(self.score)
        if score == "0":
            score = "00"
        index = 0
        for i in range(0, len(score)):
            digit = int(score[i])
            title = pygame.image.load(TextPath + "tile0" + str(32 + digit) + ".png")
            title = pygame.transform.scale(title, (square, square))
            screen.blit(title, ((scoreStart + 2 + index) * square, square + 4, square, square))
            index += 1

        index = 0
        for i in range(highScoreStart, highScoreStart+len(textHighScore)):
            title = pygame.image.load(TextPath + textHighScore[index])
            title = pygame.transform.scale(title, (square, square))
            screen.blit(title, (i * square, 4, square, square))
            index += 1

        highScore = str(self.highScore)
        if highScore == "0":
            highScore = "00"
        index = 0
        for i in range(0, len(highScore)):
            digit = int(highScore[i])
            title = pygame.image.load(TextPath + "tile0" + str(32 + digit) + ".png")
            title = pygame.transform.scale(title, (square, square))
            screen.blit(title, ((highScoreStart + 6 + index) * square, square + 4, square, square))
            index += 1

    def drawBerry(self):
        if self.levelTimer in range(self.berrystatus[0], self.berrystatus[1]) and not self.berrystatus[2]:
            berryImage = pygame.image.load(ElementPath + self.berries[(self.level - 1) % 8])
            berryImage = pygame.transform.scale(berryImage, (int(square * spriteRatio), int(square * spriteRatio)))
            screen.blit(berryImage, (self.berryLocation[1] * square, self.berryLocation[0] * square, square, square))


    def drawPoints(self, points, row, col):
        pointStr = str(points)
        index = 0
        for i in range(len(pointStr)):
            digit = int(pointStr[i])
            title = pygame.image.load(TextPath + "tile" + str(224 + digit) + ".png")
            title = pygame.transform.scale(title, (square//2, square//2))
            screen.blit(title, ((col) * square + (square//2 * index), row * square - 20, square//2, square//2))
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

 # Resets the screen around pacman
    self.drawTiles(self.pacman.row, self.pacman.col)

    # Draws new image
    pacman = pygame.image.load(ElementPath + "tile" + str(116 + self.gameOverCounter) + ".png")
    pacman = pygame.transform.scale(pacman, (int(square * spriteRatio), int(square * spriteRatio)))
    screen.blit(pacman, (self.pacman.col * square + spriteOffset, self.pacman.row * square + spriteOffset, square, square))
    pygame.display.update()
    pause(5000000)
    self.gameOverScore += 1

    def lives(self):
        lives = [[34, 3], [34, 1]]
        for i in range(self.lives - 1):
            life = pygame.image.load(ElementPath + "tile054.png")
            life = pygame.transform.scale(life, (int(square * spriteRatio), int(square * spriteRatio)))
            screen.blit(life, (lives[i][1] * square, lives[i][0] * square - spriteOffset, square, square))

    def berries(self):
        firstBerrie = [34, 26]
        for i in range(len(self.berriesCollected)):
            berrie = pygame.image.load(ElementPath + self.berriesCollected[i])
            berrie = pygame.transform.scale(berrie, (int(square * spriteRatio), int(square * spriteRatio)))
            screen.blit(berrie, ((firstBerrie[1] - (2*i)) * square, firstBerrie[0] * square + 5, square, square))

    def touchPacman(self, row, col):
        if row - 0.5 <= self.pacman.row and row >= self.pacman.row and col == self.pacman.col:
            return True
        elif row + 0.5 >= self.pacman.row and row <= self.pacman.row and col == self.pacman.col:
            return True
        elif row == self.pacman.row and col - 0.5 <= self.pacman.col and col >= self.pacman.col:
            return True
        elif row == self.pacman.row and col + 0.5 >= self.pacman.col and col <= self.pacman.col:
            return True
        elif row == self.pacman.row and col == self.pacman.col:
            return True
        return False

    def newLevel(self):
        reset()
        self.lives += 1
        self.collect = 0
        self.start = False
        self.berryStatus = [200, 400, False]
        self.levelTimer = 0
        self.lock = True
        for level in self.levels:
            level[0] = min((level[0] + level[1]) - 100, level[0] + 50)
            level[1] = max(100, level[1] - 50)
        random.shuffle(self.levels)
        index = 0
        for status in self.ghostStatus:
            status[0] = randrange(2)
            status[1] = randrange(self.levels[index][status[0]] + 1)
            index += 1
        global board
        board = copy.deepcopy(originalboard)
        self.render()

    def drawTiles(self, row, col):
        row = math.floor(row)
        col = math.floor(col)
        for i in range(row-2, row+3):
            for j in range(col-2, col+3):
                if i >= 3 and i < len(board) - 2 and j >= 0 and j < len(board[0]):
                    image = str(((i - 3) * len(board[0])) + j)
                    if len(image) == 1:
                        image = "00" + image
                    elif len(image) == 2:
                         image = "0" + image
                    # Get image of desired tile
                    image = "tile" + image + ".png"
                    title = pygame.image.load(BoardPath + image)
                    title = pygame.transform.scale(title, (square, square))
                    #Display image of tile
                    screen.blit(title, (j * square, i * square, square, square))

                    if board[i][j] == 2: # Draw Tic-Tak
                        pygame.draw.circle(screen, pelletColor,(j * square + square//2, i * square + square//2), square//4)
                    elif board[i][j] == 5: #Black Special Tic-Tak
                        pygame.draw.circle(screen, (0, 0, 0),(j * square + square//2, i * square + square//2), square//2)
                    elif board[i][j] == 6: #White Special Tic-Tak
                        pygame.draw.circle(screen, pelletColor,(j * square + square//2, i * square + square//2), square//2)

    # flip Color
    def flipColor(self):
        global board
        for i in range(3, len(board) - 2):
            for j in range(len(board[0])):
                if board[i][j] == 5:
                    board[i][j] = 6
                    pygame.draw.circle(screen, pelletColor,(j * square + square//2, i * square + square//2), square//2)
                elif board[i][j] == 6:
                    board[i][j] = 5
                    pygame.draw.circle(screen, (0, 0, 0),(j * square + square//2, i * square + square//2), square//2)

    def getCount(self):
        total = 0
        for i in range(3, len(board) - 2):
            for j in range(len(board[0])):
                if board[i][j] == 2 or board[i][j] == 5 or board[i][j] == 6:
                    total += 1
        return total

    def highScore(self):
        file = open(DataPath + "HighScore.txt", "r")
        highScore = int(file.read())
        file.close()
        return highScore

    def recordHighScore(self):
        file = open(DataPath + "HighScore.txt", "w").close()
        file = open(DataPath + "HighScore.txt", "w+")
        file.write(str(self.highScore))
        file.close()

# pacman
class Pacman:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mouthOpen = False
        self.pacSpeed = 1/4
        self.mouthDelay = 5
        self.mouthCount = 0
        self.dir = 0 # 0: North, 1: East, 2: South, 3: West
        self.newDir = 0

    def update(self):
        if self.newDir == 0:
            if canMove(math.floor(self.row - self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row -= self.pacSpeed
                self.dir = self.newDir
                return
        elif self.newDir == 1:
            if canMove(self.row, math.ceil(self.col + self.pacSpeed)) and self.row % 1.0 == 0:
                self.col += self.pacSpeed
                self.dir = self.newDir
                return
        elif self.newDir == 2:
            if canMove(math.ceil(self.row + self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row += self.pacSpeed
                self.dir = self.newDir
                return
        elif self.newDir == 3:
            if canMove(self.row, math.floor(self.col - self.pacSpeed)) and self.row % 1.0 == 0:
                self.col -= self.pacSpeed
                self.dir = self.newDir
                return

        if self.dir == 0:
            if canMove(math.floor(self.row - self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row -= self.pacSpeed
        elif self.dir == 1:
            if canMove(self.row, math.ceil(self.col + self.pacSpeed)) and self.row % 1.0 == 0:
                self.col += self.pacSpeed
        elif self.dir == 2:
            if canMove(math.ceil(self.row + self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row += self.pacSpeed
        elif self.dir == 3:
            if canMove(self.row, math.floor(self.col - self.pacSpeed)) and self.row % 1.0 == 0:
                self.col -= self.pacSpeed

