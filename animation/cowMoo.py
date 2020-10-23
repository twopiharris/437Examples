""" cowMoo.py 
    illustrates a multi-frame animation
    Responding to input and adding state and sound
"""

import pygame
pygame.init()

class Cow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.STANDING = 0
        self.MOOING = 1
        
        self.loadImages()
        self.image = self.imageStand
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.frame = 0
        self.delay = 3
        self.pause = 0
        self.state = self.STANDING
        pygame.mixer.init()
        self.moo = pygame.mixer.Sound("moo.ogg")

    def update(self):
        if self.state == self.STANDING:
            self.image = self.imageStand
        else:
            self.pause += 1
            if self.pause > self.delay:
                #reset pause and advance animation
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.mooImages):
                    self.frame = 0
                    self.state = self.STANDING
                    self.image = self.imageStand
                else:
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
pygame.display.set_caption("Press Space to make cow moo")

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cow.state = cow.MOOING
                cow.moo.play()
 
    allSprites.clear(screen, background)
    allSprites.update()
    allSprites.draw(screen)
    
    pygame.display.flip()

