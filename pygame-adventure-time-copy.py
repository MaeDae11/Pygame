


import pygame
import random, math, time

# KEY_UP = 273
# KEY_DOWN = 274
# KEY_LEFT = 276
# KEY_RIGHT = 275

# class Hero(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.speed_x = 0
#         self.speed_y = 0

#     def update(self):
#         self.x += self.speed_x
#         self.y += self.speed_y

    # def render(self, screen):
    #     pygame.image.load('images/hero.png')


def main():
    width = 500
    height = 500
    # link(src, background.png)
    blue_color = (97, 159, 182)
    # pygame.image.load(background.png)
    pygame.init()

    # everything done to screen, must be tuple otherwise python would read it as two separate things
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Adventure Time\n  -|-----')
    clock = pygame.time.Clock()
    # KEY_UP = 273
    # KEY_DOWN = 274
    # KEY_LEFT = 276
    # KEY_RIGHT = 275
    # Game initialization
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png')
    # hero = Hero(250, 250)
    stop_game = False

    speed_x = 300
    speed_y = 300
    # giant loop for game
    # while not stop_game --> while stop_game is false)
    while not stop_game:
        # loops for all events of key up/down etc or mouse clicks. what are you looking for?
        for event in pygame.event.get():

            ####### Event handling
            if event.type == pygame.K_DOWN:
                if event.key == KEY_LEFT:
                    # moves left
                    speed_x -= 10
                    
                if event.key == KEY_RIGHT:
                    #moves right
                    speed_x -= 10
                    
                if event.key == KEY_DOWN:
                    #moves down
                    speed_y -= 10
                    
                if event.KEY_UP == KEY_UP:
                    speed_y += 10
                    #moves up
                    


            if event.type == pygame.QUIT:
                stop_game = True


        ####### Game logic
            # for hero in Hero(width, height):
            #     hero.update(width, height)
        # Draw background
        screen.fill(blue_color)

        # (0, 0) and (250, 250) is corrdinates of where the image starts 
        screen.blit(background_image, (0, 0))
        screen.blit(hero_image, (speed_x, speed_y))
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
