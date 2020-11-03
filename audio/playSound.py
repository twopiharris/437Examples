""" playSound.py
    demonstrates playing an ogg sound
    on demand """

import pygame
pygame.init()
pygame.mixer.init()

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("play sound")
    
    #create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))
    
    #create label
    myFont = pygame.font.SysFont("Comic Sans MS", 30)
    label = myFont.render("Press SPACE to hear a sound", 1, (0, 0, 255))
    
    #create sound
    wooHoo = pygame.mixer.Sound("wooHoo.ogg")
    
    keepGoing = True
    clock = pygame.time.Clock()
    
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    wooHoo.play()
                elif event.key == pygame.K_ESCAPE:
                    keepGoing = False
    
        screen.blit(background, (0, 0))
        screen.blit(label, (100, 100))
        pygame.display.flip()
if __name__ == "__main__":
    main()
    
