import pygame


# class Character(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.x = x
#         self.y = y
#         self.rect = self.image.get_rect()

#     def __repr__(self):
#         pass


class Hero(object):
    def __init__(self, image):
        x = 10
        y = 250
        self.image = image
        self.x = x
        self.y = y


class First_Row(object):
    def __init__(self, image, y):
        x = 60
        self.image = image
        self.x = x
        self.y = y
        self.speed_y = 2
        self.speed_x = 2

    def update(self):
        self.y += self.speed_y
        if self.y == 480:
            self.y = 10

# class lemon_man(object):
#     def __init__(self, image):
#         x = 60
#         y = 100
#         self.image = image
#         self.x = x
#         self.y = y
#         self.speed_y = 2
#         self.speed_x = 2

#     def update(self):
#         self.y += self.speed_y
#         if self.y == 480:
#             self.y = 10

class Second_Row(object):
    def __init__(self, image):
        x = 200
        y = 100
        self.image = image
        self.x = x
        self.y = y
        self.speed_y = 3
        self.speed_x = 3

    def update(self):
        self.y += self.speed_y
        if self.y == 480:
            self.y = 10




def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    black_color = (0, 0, 0)
    # pygame.image.load(background.png)
    pygame.init()

    

    # everything done to screen, must be tuple otherwise python would read it as two separate things
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Adventure Time!!!')
    clock = pygame.time.Clock()
  

    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/finn.png')
    magic_man1 = pygame.image.load('images/magic_man.png')
    lemon_man1 = pygame.image.load('images/lemon_man.png')
    hero = Hero(hero_image)
    magic_man1 = First_Row(magic_man1, 175)
    lemon_man1 = First_Row(lemon_man1, 60)
    
    


    stop_game = False
    
    # speed_x = 300
    # speed_y = 300
    # giant loop for game
    # while not stop_game --> while stop_game is false)
    while not stop_game:
        # loops for all events of key up/down etc or mouse clicks. what are you looking for?
        magic_man1.update()
        lemon_man1.update()

        for event in pygame.event.get():
            

        # check out slack if want continual press down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print "left"
                    hero.x -= 15
                    
                if event.key == pygame.K_RIGHT:
                    print "right"
                    hero.x += 15
                    
                if event.key == pygame.K_DOWN:
                    print "down"
                    hero.y += 15
                    
                if event.key == pygame.K_UP:
                    print "up"
                    hero.y -= 15
                    


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
        # can put in render later if make class for monster1
        screen.blit(pygame.transform.scale(hero.image, (40, 60)), (hero.x, hero.y))
        screen.blit(pygame.transform.scale(magic_man1.image, (40, 60)), (magic_man1.x, magic_man1.y))
        screen.blit(pygame.transform.scale(lemon_man1.image, (40, 60)), (lemon_man1.x, lemon_man1.y))



        font = pygame.font.Font(None, 25)
        text = font.render("Click or type and see events in terminal", True, blue_color)
        

        ###### Game display


        # updates what you want to see
        pygame.display.update()

        clock.tick(60)


    # uninitializes pygame
    pygame.quit()

if __name__ == '__main__':
    main()
