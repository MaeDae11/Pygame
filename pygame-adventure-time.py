import pygame
import random, math, time




def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    black_color = (0, 0, 0)
    # pygame.image.load(background.png)
    pygame.init()
    x = 250
    y = 250

    # everything done to screen, must be tuple otherwise python would read it as two separate things
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Adventure Time!!!')
    clock = pygame.time.Clock()
  
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png')
    # hero = Hero(250, 250)
    stop_game = False

    # speed_x = 300
    # speed_y = 300
    # giant loop for game
    # while not stop_game --> while stop_game is false)
    while not stop_game:
        # loops for all events of key up/down etc or mouse clicks. what are you looking for?
        for event in pygame.event.get():
        # check out slack if want continual press down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print "you pressed left"
                    x -= 10
                if event.key == pygame.K_RIGHT:
                    print "right"
                    x += 10
                # print 'key down %r' % event.key

            if event.type == pygame.KEYUP:
                pass

                

                
            if event.type == pygame.QUIT:
                stop_game = True


        ####### Game logic
          
        # Draw background
        screen.fill(blue_color)

        # (0, 0) and (250, 250) is corrdinates of where the image starts 
        screen.blit(background_image, (0, 0))
        # blit = drawing a thing to the screen
        # can put in render later if make class for monster
        screen.blit(hero_image, (x, y))
        # hero.render(screen)
        font = pygame.font.Font(None, 25)
        text = font.render("Click or type and see events in terminal", True, blue_color)
        screen.blit(text, (80, 80))


        ###### Game display


        # updates what you want to see
        pygame.display.update()

        clock.tick(60)


    # uninitializes pygame
    pygame.quit()

if __name__ == '__main__':
    main()
