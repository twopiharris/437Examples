""" cow.py 
    a fully animated cow sprite
    uses graphics from reiner's tile set
    cow walks in eight directions 
"""

import pygame
pygame.init()

#direction constants
EAST = 0
NORTHEAST = 1
NORTH = 2
NORTHWEST = 3
WEST = 4
SOUTHWEST = 5
SOUTH = 6
SOUTHEAST = 7

class Cow(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("cowImages/stopped0002.bmp")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1, 1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)

        self.imgList = []
        self.loadPics()
        
        self.dir = EAST
        self.frame = 0
        self.delay = 1
        self.pause = self.delay
        self.speed = 3       

        self.dxVals = (1,  .7,  0, -.7, -1, -.7, 0, .7)
        self.dyVals = (0, -.7, -1, -.7,  0,  .7, 1, .7)

    
    def checkBounds(self):
        if self.rect.centerx > self.screen.get_width():
            self.rect.centerx = 0
        if self.rect.centerx < 0:
            self.rect.centerx = self.screen.get_width()
        if self.rect.centery > self.screen.get_height():
            self.rect.centery = 0
        if self.rect.centery < 0:
            self.rect.centery = self.screen.get_height()

    def loadPics(self):
       fileBase = [
            "cowImages/walking e000",
            "cowImages/walking ne000",
            "cowImages/walking n000",
            "cowImages/walking nw000",
            "cowImages/walking w000",
            "cowImages/walking sw000",
            "cowImages/walking s000",
            "cowImages/walking se000"
        ]
 
       for dir in range(8):
            tempList = []
            tempFile = fileBase[dir]
            for frame in range(8):
                imgName = "%s%d.bmp" % (tempFile, frame)
                tmpImg = pygame.image.load(imgName)
                tmpImg.convert()
                tranColor = tmpImg.get_at((0, 0))
                tmpImg.set_colorkey(tranColor)
                tempList.append(tmpImg)
            self.imgList.append(tempList)

    def update(self):
        
        self.pause -= 1
        if self.pause <= 0:
            self.pause = self.delay
        
            self.frame += 1
            if self.frame > 7:
                self.frame = 0
            
            self.calcVector()
            self.image = self.imgList[self.dir][self.frame]

            self.rect.centerx += self.dx
            self.rect.centery += self.dy

            self.checkBounds()

    def calcVector(self):
        self.dx = self.dxVals[self.dir]
        self.dy = self.dyVals[self.dir]
        
        self.dx *= self.speed
        self.dy *= self.speed
    
    def turnLeft(self):
        self.dir += 1
        if self.dir > SOUTHEAST:
            self.dir = EAST

    def turnRight(self):
        self.dir -= 1
        if self.dir < EAST:
            self.dir = SOUTHEAST

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("cow animation")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0x66, 0))
    screen.blit(background, (0, 0))
    
    cow = Cow(screen)
    allSprites = pygame.sprite.Group(cow)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cow.turnLeft()
                elif event.key == pygame.K_RIGHT:
                    cow.turnRight()
        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
