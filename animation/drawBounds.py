""" rotate.py 
    demonstrate rotating a sprite
    draw bounding rectangle to illustrate
    sprite size change
"""

import pygame
pygame.init()

class Ship(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.imageMaster = pygame.image.load("ship.bmp")
        self.imageMaster = self.imageMaster.convert()
        self.image = self.imageMaster
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.dir = 0

    def update(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.imageMaster, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter
        
    def turnLeft(self):
        self.dir += 45
        if self.dir > 360:
            self.dir = 45
    
    def turnRight(self):
        self.dir -= 45
        if self.dir < 0:
            self.dir = 315
        
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Show sprite bounding box")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    
    ship = Ship(background)
    allSprites = pygame.sprite.Group(ship)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship.turnLeft()
                elif event.key == pygame.K_RIGHT:
                    ship.turnRight()
        
        #do an old-fashioned background blit
        screen.blit(background, (0, 0))

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        #draw a rect on the screen
        pygame.draw.rect(screen, (255, 255, 255), ship.rect, 3)
        
        pygame.display.flip()
    
if __name__ == "__main__":
    main()
   
