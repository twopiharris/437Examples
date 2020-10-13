""" basicSprite.py
    works just like moveBox.py
    from chapter 4,
    but now uses a sprite """

import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image = self.image.convert()
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.centery = 200
        self.dx = 10
        self.dy = 0

    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.rect.left = 0

def main():
    pygame.display.set_caption("basic sprite demo")
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))
    screen.blit(background, (0,0))
    
    box = Box()
    allSprites = pygame.sprite.Group(box)
    
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
