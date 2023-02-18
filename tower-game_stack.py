# DATA STRUCTURE AND ALGORITHMS - FINAL PROJECT
import red as red

print("\nPROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")

import pygame

pygame.init()

width = 1000
height = 500
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

background = (0,0,0)
white = (236, 240, 241)

#====================== color codes =================
color = [(139, 0, 1), (158, 23, 17), (177, 46, 33), (195, 70, 50), (214, 93, 66), (233, 116, 82), (246, 129, 110),
         (255, 145, 126), (255, 175, 156 ), ( 255, 215, 196),
         (255, 189, 170), ( 255, 199, 180 ), (255, 209, 190), (255, 219, 200 ), (255, 229, 210), (255, 239, 220),
         (255, 242, 223 ), (246, 129, 110), (214, 93, 66), (139, 0, 1),
         (158, 23, 17), (177, 46, 33), (195, 70, 50), (214, 93, 66), (233, 116, 82), (246, 129, 110), (245, 176, 65),
         (248, 196, 113), (250, 215, 160), (253, 235, 208), (254, 245, 231),
         (232, 246, 243), (162, 217, 206), (162, 217, 206),
         (115, 198, 182), (69, 179, 157), (22, 160, 133),
         (19, 141, 117), (17, 122, 101), (14, 102, 85),
         (11, 83, 69),
         (21, 67, 96), (26, 82, 118), (31, 97, 141),
         (36, 113, 163), (41, 128, 185), (84, 153, 199),
         (127, 179, 213), (169, 204, 227), (212, 230, 241),
         (234, 242, 248),
         (251, 238, 230), (246, 221, 204), (237, 187, 153),
         (229, 152, 102), (220, 118, 51), (211, 84, 0),
         (186, 74, 0), (160, 64, 0), (135, 54, 0),
         (110, 44, 0)
         ]

colorIndex = 0

brickH = 25
brickW = 200
score = 0
speed = 3

#====================== single brick class =================
class Brick:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.w = brickW
        self.h = brickH
        self.color = color
        self.speed = speed

    def draw(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h))

    def move(self):
        self.x += self.speed
        if self.x > width:
            self.speed *= -1
        if self.x + self.w < 1:
            self.speed *= -1

#====================== complete stack =================
class Stack:
    def __init__(self):
        global colorIndex
        self.stack = []
        self.initSize = 25
        for i in range(self.initSize):
            newBrick = Brick(width / 2 - brickW / 2, height - (i + 1) * brickH, color[colorIndex], 0)
            colorIndex += 1
            self.stack.append(newBrick)

    def show(self):
        for i in range(self.initSize):
            self.stack[i].draw()

    def move(self):
        for i in range(self.initSize):
            self.stack[i].move()

    def addNewBrick(self):
        global colorIndex, speed

        if colorIndex >= len(color):
            colorIndex = 0

        y = self.peek().y
        if score > 50:
            speed += 3
        elif score % 5 == 0:
            speed += 1

        newBrick = Brick(width, y - brickH, color[colorIndex], speed)
        colorIndex += 1
        self.initSize += 1
        self.stack.append(newBrick)

    def peek(self):
        return self.stack[self.initSize - 1]

    def pushToStack(self):
        global brickW, score
        b = self.stack[self.initSize - 2]
        b2 = self.stack[self.initSize - 1]
        if b2.x <= b.x and not (b2.x + b2.w < b.x):
            self.stack[self.initSize - 1].w = self.stack[self.initSize - 1].x + self.stack[self.initSize - 1].w - b.x
            self.stack[self.initSize - 1].x = b.x
            if self.stack[self.initSize - 1].w > b.w:
                self.stack[self.initSize - 1].w = b.w
            self.stack[self.initSize - 1].speed = 0
            score += 1
        elif b.x <= b2.x <= b.x + b.w:
            self.stack[self.initSize - 1].w = b.x + b.w - b2.x
            self.stack[self.initSize - 1].speed = 0
            score += 1
        else:
            gameOver()
        for i in range(self.initSize):
            self.stack[i].y += brickH

        brickW = self.stack[self.initSize - 1].w

#====================== game over =================
def gameOver():
    loop = True

    font = pygame.font.SysFont("Agency FB", 60)
    text = font.render("You Missed ! Game Over", True, white)

    textRect = text.get_rect()
    textRect.center = (width / 2, height / 2 - 80)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameLoop()
        display.blit(text, textRect)

        pygame.display.update()
        clock.tick()


# Displaying the Score on Screen
def showScore():
    font = pygame.font.SysFont("Agency FB", 55)
    text = font.render("Score: " + str(score), True, white)
    display.blit(text, (10, 10))


# Close the Window
def close(sys=None):
    pygame.quit()
    sys.exit()


# The Main Game Loop
def gameLoop():
    global brickW, brickH, score, colorIndex, speed
    loop = True

    brickH = 10
    brickW = 100
    colorIndex = 0
    speed = 3

    score = 0

    stack = Stack()
    stack.addNewBrick()

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                stack.pushToStack()
                stack.addNewBrick()

        display.fill(background)

        stack.move()
        stack.show()

        showScore()

        pygame.display.update()
        clock.tick(60)


gameLoop()
