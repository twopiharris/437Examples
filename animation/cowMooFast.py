""" cowMooFast.py 
    illustrates a multi-frame animation
    animates way too quickly
"""

import pygame
pygame.init()

class Cow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.loadImages()
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.frame = 0

    def update(self):
        self.frame += 1
        if self.frame >= len(self.mooImages):
            self.frame = 0
        self.image = self.mooImages[self.frame]
        

    def loadImages(self):
        self.imageStand = pygame.image.load("cowImages/stopped0002.bmp")
        self.imageStand = self.imageStand.convert()
        transColor = self.imageStand.get_at((1, 1))
        self.imageStand.set_colorkey(transColor)

        self.mooImages = []
        for i in range(10):
            imgName = "cowImages/muuuh e000%d.bmp" % i
            tmpImage = pygame.image.load(imgName)
            tmpImage = tmpImage.convert()
            transColor = tmpImage.get_at((1, 1))
            tmpImage.set_colorkey(transColor)
            self.mooImages.append(tmpImage)


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Fast Mooing")

background = pygame.Surface(screen.get_size())
background.fill((0, 0x99, 0))
screen.blit(background, (0, 0))

cow = Cow()
allSprites = pygame.sprite.Group(cow)

clock = pygame.time.Clock()
keepGoing = True

while keepGoing:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    
    allSprites.clear(screen, background)
    allSprites.update()
    allSprites.draw(screen)
    
    pygame.display.flip()

