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
        # pygame.identity.unload()
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
                    identity = str(currentTile)
                    if len(identity) == 1:
                        identity = "00" + identity
                    elif len(identity) == 2:
                         identity = "0" + identity
                    # get tile identity
                    identity = "tile" + identity + ".png"
                    title = pygame.identity.load(BoardPath + identity)
                    title = pygame.transform.scale(title, (square, square))

                    # identity of tile
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
                ghost.speed = 1
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
            title = pygame.identity.load(text + textOneUp[index])
            title = pygame.transform.scale(title, (square, square))
            screen.blit(title, (i * square, 4, square, square))
            index += 1
        score = str(self.score)
        if score == "0":
            score = "00"
        index = 0
        for i in range(0, len(score)):
            digit = int(score[i])
            title = pygame.identity.load(text + "tile0" + str(32 + digit) + ".png")
            title = pygame.transform.scale(title, (square, square))
            screen.blit(title, ((scoreStart + 2 + index) * square, square + 4, square, square))
            index += 1

        index = 0
        for i in range(highScoreStart, highScoreStart+len(textHighScore)):
            title = pygame.identity.load(text + textHighScore[index])
            title = pygame.transform.scale(title, (square, square))
            screen.blit(title, (i * square, 4, square, square))
            index += 1

        highScore = str(self.highScore)
        if highScore == "0":
            highScore = "00"
        index = 0
        for i in range(0, len(highScore)):
            digit = int(highScore[i])
            title = pygame.identity.load(text + "tile0" + str(32 + digit) + ".png")
            title = pygame.transform.scale(title, (square, square))
            screen.blit(title, ((highScoreStart + 6 + index) * square, square + 4, square, square))
            index += 1

    def drawBerry(self):
        if self.levelTimer in range(self.berrystatus[0], self.berrystatus[1]) and not self.berrystatus[2]:
            berryidentity = pygame.identity.load(element + self.berries[(self.level - 1) % 8])
            berryidentity = pygame.transform.scale(berryidentity, (int(square * spriteRatio), int(square * spriteRatio)))
            screen.blit(berryidentity, (self.berryLocation[1] * square, self.berryLocation[0] * square, square, square))


    def drawPoints(self, points, row, col):
        pointStr = str(points)
        index = 0
        for i in range(len(pointStr)):
            digit = int(pointStr[i])
            title = pygame.identity.load(text + "tile" + str(224 + digit) + ".png")
            title = pygame.transform.scale(title, (square//2, square//2))
            screen.blit(title, ((col) * square + (square//2 * index), row * square - 20, square//2, square//2))
            index += 1

    def drawReady(self):
        ready = ["tile274.png", "tile260.png", "tile256.png", "tile259.png", "tile281.png", "tile283.png"]
        for i in range(len(ready)):
            symbol = pygame.identity.load(text + ready[i])
            symbol = pygame.transform.scale(symbol, (int(square), int(square)))
            screen.blit(symbol, ((11 + i) * square, 20 * square, square, square))

    def gameOverFunction(self):
        global running
        if self.gameOverCounter == 12:
            running = False
            self.recordHighScore()
            return

 # Resets the screen around pacman
    self.drawTiles(self.pacman.row, self.pacman.col)

    # Draws new identity
    pacman = pygame.identity.load(element + "tile" + str(116 + self.gameOverCounter) + ".png")
    pacman = pygame.transform.scale(pacman, (int(square * spriteRatio), int(square * spriteRatio)))
    screen.blit(pacman, (self.pacman.col * square + spriteOffset, self.pacman.row * square + spriteOffset, square, square))
    pygame.display.update()
    pause(5000000)
    self.gameOverScore += 1

    def lives(self):
        lives = [[34, 3], [34, 1]]
        for i in range(self.lives - 1):
            life = pygame.identity.load(element + "tile054.png")
            life = pygame.transform.scale(life, (int(square * spriteRatio), int(square * spriteRatio)))
            screen.blit(life, (lives[i][1] * square, lives[i][0] * square - spriteOffset, square, square))

    def berries(self):
        firstBerrie = [34, 26]
        for i in range(len(self.berriesCollected)):
            berrie = pygame.identity.load(element + self.berriesCollected[i])
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
                    identity = str(((i - 3) * len(board[0])) + j)
                    if len(identity) == 1:
                        identity = "00" + identity
                    elif len(identity) == 2:
                         identity = "0" + identity
                    # Get identity of desired tile
                    identity = "tile" + identity + ".png"
                    title = pygame.identity.load(BoardPath + identity)
                    title = pygame.transform.scale(title, (square, square))
                    #Display identity of tile
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

# pacman elements
class pacman:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.open = False
        self.speed = 1/4
        self.delay = 5
        self.count = 0
        self.dir = 0
        self.newDirectionection = 0

    def update(self):
        if self.newDirectionection == 0:
            if move(math.floor(self.row - self.speed), self.col) and self.col % 1.0 == 0:
                self.row -= self.speed
                self.dir = self.newDirectionection
                return
        elif self.newDirectionection == 1:
            if move(self.row, math.ceil(self.col + self.speed)) and self.row % 1.0 == 0:
                self.col += self.speed
                self.dir = self.newDirectionection
                return
        elif self.newDirectionection == 2:
            if move(math.ceil(self.row + self.speed), self.col) and self.col % 1.0 == 0:
                self.row += self.speed
                self.dir = self.newDirectionection
                return
        elif self.newDirectionection == 3:
            if move(self.row, math.floor(self.col - self.speed)) and self.row % 1.0 == 0:
                self.col -= self.speed
                self.dir = self.newDirectionection
                return

        if self.dir == 0:
            if move(math.floor(self.row - self.speed), self.col) and self.col % 1.0 == 0:
                self.row -= self.speed
        elif self.dir == 1:
            if move(self.row, math.ceil(self.col + self.speed)) and self.row % 1.0 == 0:
                self.col += self.speed
        elif self.dir == 2:
            if move(math.ceil(self.row + self.speed), self.col) and self.col % 1.0 == 0:
                self.row += self.speed
        elif self.dir == 3:
            if move(self.row, math.floor(self.col - self.speed)) and self.row % 1.0 == 0:
                self.col -= self.speed

    # pacman current status
    def draw(self):
        if not game.start:
            pacman = pygame.identity.load(element + "tile112.png")
            pacman = pygame.transform.scale(pacman, (int(square * spriteRatio), int(square * spriteRatio)))
            screen.blit(pacman, (self.col * square + spriteOffset, self.row * square + spriteOffset, square, square))
            return

        if self.count == self.delay:
            self.count = 0
            self.open = not self.open
        self.count += 1
        
        if self.dir == 0:
            if self.open:
                pacman = pygame.identity.load(element + "tile049.png")
            else:
                pacman = pygame.identity.load(element + "tile051.png")
        
        elif self.dir == 1:
            if self.open:
                pacman = pygame.identity.load(element + "tile052.png")
            else:
                pacman = pygame.identity.load(element + "tile054.png")
        
        elif self.dir == 2:
            if self.open:
                pacman = pygame.identity.load(element + "tile053.png")
            else:
                pacman = pygame.identity.load(element + "tile055.png")
        
        elif self.dir == 3:
            if self.open:
                pacman = pygame.identity.load(element + "tile048.png")
            else:
                pacman = pygame.identity.load(element + "tile050.png")

        pacman = pygame.transform.scale(pacman, (int(square * spriteRatio), int(square * spriteRatio)))
        screen.blit(pacman, (self.col * square + spriteOffset, self.row * square + spriteOffset, square, square))

# ghost elements
class Ghost:
    def __init__(self, row, col, color, changeCount):
        self.row = row
        self.col = col
        self.attack = False
        self.color = color
        self.dir = randrange(4)
        self.dead = False
        self.changeCount = change
        self.changeDelay = 5
        self.target = [-1, -1]
        self.speed = 1/4
        self.lastLoc = [-1, -1]
        self.attackTimer = 240
        self.attackCount = 0
        self.deathTimer = 120
        self.deathCount = 0

    def update(self):
        if self.target == [-1, -1] or (self.row == self.target[0] and self.col == self.target[1]) or board[int(self.row)][int(self.col)] == 4 or self.dead:
            self.setTarget()
        self.setDir()
        self.move()

        if self.attack:
            self.attackCount += 1

        if self.attack and not self.dead:
            self.speed = 1/8

        if self.attackCount == self.attackTimer and self.attack:
            if not self.dead:
                self.speed = 1/4
                self.row = math.floor(self.row)
                self.col = math.floor(self.col)

            self.attackCount = 0
            self.attack = False
            self.setTarget()

        if self.dead and board[self.row][self.col] == 4:
            self.deathCount += 1
            self.attack = False
            if self.deathCount == self.deathTimer:
                self.deathCount = 0
                self.dead = False
                self.speed = 1/4

    def draw(self):
        ghost = pygame.identity.load(element + "tile152.png")
        currentDirection = ((self.dir + 3) % 4) * 2
        if self.change == self.changeDelay:
            self.change = 0
            currentDirection += 1
        self.change += 1
        if self.dead:
            tile = 152 + currentDirection
            ghost = pygame.identity.load(element + "tile" + str(tile) + ".png")
        elif self.attack:
            if self.attackTimer - self.attackCount < self.attackTimer//3:
                if (self.attackTimer - self.attackCount) % 31 < 26:
                    ghost = pygame.identity.load(element + "tile0" + str(70 + (currentDirection - (((self.dir + 3) % 4) * 2))) + ".png")
                else:
                    ghost = pygame.identity.load(element + "tile0" + str(72 + (currentDirection - (((self.dir + 3) % 4) * 2))) + ".png")
            else:
                ghost = pygame.identity.load(element + "tile0" + str(72 + (currentDirection - (((self.dir + 3) % 4) * 2))) + ".png")
        else:
            if self.color == "blue":
                tile = 136 + currentDirection
                ghost = pygame.identity.load(element + "tile" + str(tile) + ".png")
            elif self.color == "pink":
                tile = 128 + currentDirection
                ghost = pygame.identity.load(element + "tile" + str(tile) + ".png")
            elif self.color == "orange":
                tile = 144 + currentDirection
                ghost = pygame.identity.load(element + "tile" + str(tile) + ".png")
            elif self.color == "red":
                tile = 96 + currentDirection
                if tile < 100:
                    ghost = pygame.identity.load(element + "tile0" + str(tile) + ".png")
                else:
                    ghost = pygame.identity.load(element + "tile" + str(tile) + ".png")

        ghost = pygame.transform.scale(ghost, (int(square * spriteRatio), int(square * spriteRatio)))
        screen.blit(ghost, (self.col * square + spriteOffset, self.row * square + spriteOffset, square, square))

    def isValidTwo(self, cRow, cCol, dist, visited):
        if cRow < 3 or cRow >= len(board) - 5 or cCol < 0 or cCol >= len(board[0]) or board[cRow][cCol] == 3:
            return False
        elif visited[cRow][cCol] <= dist:
            return False
        return True

    def isValid(self, cRow, cCol):
        if cCol < 0 or cCol > len(board[0]) - 1:
            return True
        for ghost in game.ghosts:
            if ghost.color == self.color:
                continue
            if ghost.row == cRow and ghost.col == cCol and not self.dead:
                return False
        if not ghostGate.count([cRow, cCol]) == 0:
            if self.dead and self.row < cRow:
                return True
            elif self.row > cRow and not self.dead and not self.attack and not game.lock:
                return True
            else:
                return False
        if board[cRow][cCol] == 3:
            return False
        return True

    def setDir(self):
        dirs = [[0, -self.speed, 0],
                [1, 0, self.speed],
                [2, self.speed, 0],
                [3, 0, -self.speed]
        ]
        random.shuffle(dirs)
        best = 10000
        bestDirection = -1
        for newDirectionection in dirs:
            if self.calculateDistance(self.target, [self.row + newDirectionection[1], self.col + newDirectionection[2]]) < best:
                if not (self.lastLoc[0] == self.row + newDirectionection[1] and self.lastLoc[1] == self.col + newDirectionection[2]):
                    if newDirectionection[0] == 0 and self.col % 1.0 == 0:
                        if self.isValid(math.floor(self.row + newDirectionection[1]), int(self.col + newDirectionection[2])):
                            bestDirection = newDirectionection[0]
                            best = self.calculateDistance(self.target, [self.row + newDirectionection[1], self.col + newDirectionection[2]])
                    elif newDirectionection[0] == 1 and self.row % 1.0 == 0:
                        if self.isValid(int(self.row + newDirectionection[1]), math.ceil(self.col + newDirectionection[2])):
                            bestDirection = newDirectionection[0]
                            best = self.calculateDistance(self.target, [self.row + newDirectionection[1], self.col + newDirectionection[2]])
                    elif newDirectionection[0] == 2 and self.col % 1.0 == 0:
                        if self.isValid(math.ceil(self.row + newDirectionection[1]), int(self.col + newDirectionection[2])):
                            bestDirection = newDirectionection[0]
                            best = self.calculateDistance(self.target, [self.row + newDirectionection[1], self.col + newDirectionection[2]])
                    elif newDirectionection[0] == 3 and self.row % 1.0 == 0:
                        if self.isValid(int(self.row + newDirectionection[1]), math.floor(self.col + newDirectionection[2])):
                            bestDirection = newDirectionection[0]
                            best = self.calculateDistance(self.target, [self.row + newDirectionection[1], self.col + newDirectionection[2]])
        self.dir = bestDirection

    def calculateDistance(self, a, b):
        dR = a[0] - b[0]
        dC = a[1] - b[1]
        return math.sqrt((dR * dR) + (dC * dC))

    def setTarget(self):
        if board[int(self.row)][int(self.col)] == 4 and not self.dead:
            self.target = [ghostGate[0][0] - 1, ghostGate[0][1]+1]
            return
        elif board[int(self.row)][int(self.col)] == 4 and self.dead:
            self.target = [self.row, self.col]
        elif self.dead:
            self.target = [14, 13]
            return

        quads = [0, 0, 0, 0]
        for ghost in game.ghosts:
            if ghost.target[0] <= 15 and ghost.target[1] >= 13:
                quads[0] += 1
            elif ghost.target[0] <= 15 and ghost.target[1] < 13:
                quads[1] += 1
            elif ghost.target[0] > 15 and ghost.target[1] < 13:
                quads[2] += 1
            elif ghost.target[0]> 15 and ghost.target[1] >= 13:
                quads[3] += 1

        # keep the ghosts dispersed
        while True:
            self.target = [randrange(31), randrange(28)]
            quad = 0
            if self.target[0] <= 15 and self.target[1] >= 13:
                quad = 0
            elif self.target[0] <= 15 and self.target[1] < 13:
                quad = 1
            elif self.target[0] > 15 and self.target[1] < 13:
                quad = 2
            elif self.target[0] > 15 and self.target[1] >= 13:
                quad = 3
            if not board[self.target[0]][self.target[1]] == 3 and not board[self.target[0]][self.target[1]] == 4:
                break
            elif quads[quad] == 0:
                break

    def move(self):
        self.lastLoc = [self.row, self.col]
        if self.dir == 0:
            self.row -= self.speed
        elif self.dir == 1:
            self.col += self.speed
        elif self.dir == 2:
            self.row += self.speed
        elif self.dir == 3:
            self.col -= self.speed

        # Incase they go through the middle tunnel
        self.col = self.col % len(board[0])
        if self.col < 0:
            self.col = len(board[0]) - 0.5



    def setattack(self, isattack):
        self.attack = isattack

    def isattack(self):
        return self.attack

    def setDead(self, isDead):
        self.dead = isDead

    def isDead(self):
        return self.dead

game = Game(1, 0)
ghostsafeArea = [16, 14] 
ghostGate = [[16, 14], [16, 15]]


def move(row, col):
    if col == -1 or col == len(board[0]):
        return True
    if board[int(row)][int(col)] != 4:
        return True
    return False

# death reset
def reset():
    global game
    game.ghosts = [Ghost(15.0, 14.5, "red", 0), Ghost(18.0, 12.5, "blue", 1), Ghost(18.0, 14.5, "pink", 2), Ghost(18.0, 16.5, "orange", 3)]
    for ghost in game.ghosts:
        ghost.setTarget()
    game.pacman = pacman(26.0, 13.5)
    game.lives -= 1
    game.paused = True
    game.render()

# pacman title
def displayLaunchScreen():
    
    pacmanTitle = ["tile016.png", "tile000.png", "tile448.png", "tile012.png", "tile000.png", "tile013.png"]
    for i in range(len(pacmanTitle)):
        symbol = pygame.identity.load(text + pacmanTitle[i])
        symbol = pygame.transform.scale(symbol, (int(square * 4), int(square * 4)))
        screen.blit(symbol, ((2 + 4 * i) * square, 2 * square, square, square))

    # figure amd nickname
    figureTitle = [
        # figure
        "tile002.png", "tile007.png", "tile000.png", "tile018.png", "tile000.png", "tile002.png", "tile020.png", "tile004.png", "tile018.png",
        # space
        "tile015.png", "tile042.png", "tile015.png",
        # nickname
        "tile013.png", "tile008.png", "tile002.png", "tile010.png", "tile013.png", "tile000.png", "tile012.png", "tile004.png"
    ]
    for i in range(len(figureTitle)):
        symbol = pygame.identity.load(text + figureTitle[i])
        symbol = pygame.transform.scale(symbol, (int(square), int(square)))
        screen.blit(symbol, ((4 + i) * square, 10 * square, square, square))

    # ghosts
    figures = [
        # red
        [
            "tile449.png", "tile015.png", "tile107.png", "tile015.png", "tile083.png", "tile071.png", "tile064.png", "tile067.png", "tile078.png", "tile087.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile108.png", "tile065.png", "tile075.png", "tile072.png", "tile077.png", "tile074.png", "tile089.png", "tile108.png"
        ],
        # pink
        [
            "tile450.png", "tile015.png", "tile363.png", "tile015.png", "tile339.png", "tile336.png", "tile324.png", "tile324.png", "tile323.png", "tile345.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile364.png", "tile336.png", "tile328.png", "tile333.png", "tile330.png", "tile345.png", "tile364.png"
        ],
        # blue
        [
            "tile452.png", "tile015.png", "tile363.png", "tile015.png", "tile193.png", "tile192.png", "tile211.png", "tile199.png", "tile197.png", "tile213.png", "tile203.png",
            "tile015.png", "tile015.png", "tile015.png",
            "tile236.png", "tile200.png", "tile205.png", "tile202.png", "tile217.png", "tile236.png"
        ],
        # orange
        [
            "tile451.png", "tile015.png", "tile363.png", "tile015.png", "tile272.png", "tile270.png", "tile266.png", "tile260.png", "tile281.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile300.png", "tile258.png", "tile267.png", "tile281.png", "tile259.png", "tile260.png", "tile300.png"
        ]
    ]
    for i in range(len(figures)):
        for j in range(len(figures[i])):
            if j == 0:
                    symbol = pygame.identity.load(text + figures[i][j])
                    symbol = pygame.transform.scale(symbol, (int(square * spriteRatio), int(square * spriteRatio)))
                    screen.blit(symbol, ((2 + j) * square - square//2, (12 + 2 * i) * square - square//3, square, square))
            else:
                symbol = pygame.identity.load(text + figures[i][j])
                symbol = pygame.transform.scale(symbol, (int(square), int(square)))
                screen.blit(symbol, ((2 + j) * square, (12 + 2 * i) * square, square, square))
    
    event = ["tile449.png", "tile015.png", "tile452.png", "tile015.png",  "tile015.png", "tile448.png", "tile453.png", "tile015.png", "tile015.png", "tile015.png",  "tile453.png"]
    for i in range(len(event)):
        figure = pygame.identity.load(text + event[i])
        figure = pygame.transform.scale(figure, (int(square * 2), int(square * 2)))
        screen.blit(figure, ((4 + i * 2) * square, 24 * square, square, square))
    
    wall = ["tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png"]
    for i in range(len(wall)):
        programme = pygame.identity.load(text + wall[i])
        programme = pygame.transform.scale(programme, (int(square * 2), int(square * 2)))
        screen.blit(programme, ((i * 2) * square, 26 * square, square, square))
    
     # Press Space to Play
    instructions = ["tile016.png", "tile018.png", "tile004.png", "tile019.png", "tile019.png", "tile015.png", "tile019.png", "tile016.png", "tile000.png", "tile002.png", "tile004.png", "tile015.png", "tile020.png", "tile014.png", "tile015.png", "tile016.png", "tile011.png", "tile000.png", "tile025.png"]
    for i in range(len(instructions)):
        letter = pygame.image.load(TextPath + instructions[i])
        letter = pygame.transform.scale(letter, (int(square), int(square)))
        screen.blit(letter, ((4.5 + i) * square, 35 * square - 10, square, square))

    pygame.display.update()

running = True
screen = True
displayScreen()

def pause(time):
    cur = 0
    while not cur == time:
        cur += 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            game.recordHighScore()
        elif event.type == pygame.KEYDOWN:
            game.paus = False
            game.start = True
            if event.key == pygame.K_w:
                if not screen:
                    game.pacman.newDirection = 0
            elif event.key == pygame.K_d:
                if not screen:
                    game.pacman.newDirection = 1
            elif event.key == pygame.K_s:
                if not screen:
                    game.pacman.newDirection = 2
            elif event.key == pygame.K_a:
                if not screen:
                    game.pacman.newDirection = 3
            elif event.key == pygame.K_SPACE:
                if screen:
                    screen = False
                    game.pause = True
                    game.start = False
                    game.render()
            elif event.key == pygame.K_q:
                running = False
                game.record()

    if not screen:
        game.update()