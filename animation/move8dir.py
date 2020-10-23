""" move8Dir.py 
    modify rotated sprite to handle
    moving in 8 directions"""
    
import pygame
pygame.init()

class Ship(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.imageMaster = pygame.image.load("ship.bmp")
        self.imageMaster = self.imageMaster.convert()
        self.imageMaster = pygame.transform.scale(self.imageMaster, (30, 30))
        
        self.image = self.imageMaster
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)

        self.x = self.rect.centerx
        self.y = self.rect.centery       
        self.dir = 0
        self.speed = 0
        self.dx = 0
        self.dy = 0

    def update(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.imageMaster, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter
        
        self.calcVector()
        self.x += self.dx
        self.y += self.dy
        self.checkBounds()
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def calcVector(self):
        if self.dir == 0:
            self.dx = 1
            self.dy = 0
        elif self.dir == 45:
            self.dx = .7
            self.dy = -.7
        elif self.dir == 90:
            self.dx = 0
            self.dy = -1
        elif self.dir == 135:
            self.dx = -.7
            self.dy = -.7
        elif self.dir == 180:
            self.dx = -1
            self.dy = 0
        elif self.dir == 225:
            self.dx = -.7
            self.dy = .7
        elif self.dir == 270:
            self.dx = 0
            self.dy = 1
        elif self.dir == 315:
            self.dx = .7
            self.dy = .7
        else:
            print "something went wrong here"
        
        self.dx *= self.speed
        self.dy *= self.speed

    def turnLeft(self):
        self.dir += 45
        if self.dir == 360:
            self.dir = 0
            
    def turnRight(self):
        self.dir -= 45
        if self.dir < 0:
            self.dir = 315
    
    def speedUp(self):
        self.speed += 1
        if self.speed > 8:
            self.speed = 8
    
    def slowDown(self):
        self.speed -= 1
        if self.speed < -3:
            self.speed = -3
        

    def checkBounds(self):
        screen = self.screen
        if self.y > screen.get_height():
            self.y = 0
        if self.y < 0:
            self.y = screen.get_height()
        if self.x > screen.get_width():
            self.x = 0
        if self.x < 0:
            self.x = screen.get_width()
        
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Rotate a sprite")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    
    ship = Ship(screen)
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
                elif event.key == pygame.K_UP:
                    ship.speedUp()
                elif event.key == pygame.K_DOWN:
                    ship.slowDown()
        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
if __name__ == "__main__":
    main()
    
