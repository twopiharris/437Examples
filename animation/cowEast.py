""" cow.py 
    a fully animated cow sprite
    uses graphics from reiner's tile set
    cow walks towards the east
"""

import pygame
pygame.init()

class Cow(pygame.sprite.Sprite):

    EAST = 0
    
    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("cowImages/stopped0002.bmp")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1, 1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.img = []
        
        self.loadPics()
        self.frame = 0
        self.delay = 1
        self.pause = self.delay
        self.dx = 4       


    def update(self):
        
        self.pause -= 1
        if self.pause <= 0:
            self.pause = self.delay
            
            self.frame += 1
            if self.frame > 7:
                self.frame = 0
            
            self.image = self.img[self.frame]
            
            self.rect.centerx += self.dx
            if self.rect.centerx > self.screen.get_width():
                self.rect.centerx = 0
    
    def loadPics(self):
        for i in range(8):
            imgName = "cowImages/walking e000%d.bmp" % i
            tmpImg = pygame.image.load(imgName)
            tmpImg.convert()
            tranColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(tranColor)
            self.img.append(tmpImg)


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
        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
    
