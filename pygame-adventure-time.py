import pygame
import os, sys


def main():
    width = 500
    height = 500
    # link(src, background.png)
    blue_color = (97, 159, 182)
    # pygame.image.load(background.png)
    pygame.init()

    # everything done to screen, must be tuple otherwise python would read it as two separate things
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Adventure Time\n  -|-----')
    clock = pygame.time.Clock()

    # Game initialization
    hero_image = pygame.image.load('images/hero.png').convert_alpha()

    stop_game = False
    # giant loop for game
    # while not stop_game --> while stop_game is false)
    while not stop_game:
        # loops for all events of key up/down etc or mouse clicks. what are you looking for?
        for event in pygame.event.get():
            
            ####### Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        ####### Game logic

        # Draw background
        screen.fill(blue_color)
        screen.blit(hero_image, (250, 250))
        ###### Game display


        # updates what you want to see
        pygame.display.update()
        clock.tick(60)


    # uninitializes pygame
    pygame.quit()

if __name__ == '__main__':
    main()
