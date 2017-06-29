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
        x = 80
        self.image = image
        self.y = y
        self.x = x
        self.speed_y = 2
        self.speed_x = 2

    def update(self):
        self.y += self.speed_y
        if self.y >= 680:
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
    def __init__(self, image, y):
        x = 275
        self.image = image
        self.x = x
        self.y = y
        self.speed_y = 3
        self.speed_x = 3

    def update(self):
        self.y += self.speed_y
        if self.y >= 680:
            self.y = 10


class Third_Row(object):
    def __init__(self, image, y):
        x = 500
        self.image = image
        self.x = x
        self.y = y
        self.speed_y = 4
        self.speed_x = 4

    def update(self):
        self.y += self.speed_y
        if self.y >= 680:
            self.y = 10





def main():
    width = 700
    height = 700
    blue_color = (97, 159, 182)
    black_color = (0, 0, 0)
    # pygame.image.load(background.png)
    pygame.init()

    

    # everything done to screen, must be tuple otherwise python would read it as two separate things
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Adventure Time!!!')
    clock = pygame.time.Clock()
    # background image of treese
    background_image = pygame.image.load('images/background.png').convert_alpha()

    # hero image and setup of class
    hero_image = pygame.image.load('images/finn.png')
    hero = Hero(hero_image)

    # first row of monsters and setup of class
    magic_man1 = pygame.image.load('images/magic_man.png')
    lemon_man1 = pygame.image.load('images/lemon_man.png') 
    magic_man1 = First_Row(magic_man1, 60)
    lemon_man1 = First_Row(lemon_man1, 300)
    
    # second row of monsters and setup of class
    death = pygame.image.load('images/death.png')
    death = Second_Row(death, 300)
    pepperment_butler2 = pygame.image.load('images/pepperment_butler.png')
    pepperment_butler2 = Second_Row(pepperment_butler2, 100)

    # third row of monsters and setup of class
    ice_king3 = pygame.image.load('images/ice_king.png')
    ice_king3 = Third_Row(ice_king3, 100)
    gunter3_1 = pygame.image.load('images/gunter.png')
    gunter3_1 = Third_Row(gunter3_1, 400)
    gunter3_2 = pygame.image.load('images/gunter.png')
    gunter3_2 = Third_Row(gunter3_2, 20)
    


    stop_game = False
    
    # speed_x = 300
    # speed_y = 300
    # giant loop for game
    # while not stop_game --> while stop_game is false)
    while not stop_game:
        # loops for all events of key up/down etc or mouse clicks. what are you looking for?
        magic_man1.update()
        lemon_man1.update()

        death.update()
        pepperment_butler2.update()

        ice_king3.update()
        gunter3_1.update()
        gunter3_2.update()

        for event in pygame.event.get():
            

        # check out slack if want continual press down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.x -= 20
                    
                if event.key == pygame.K_RIGHT:
                    hero.x += 20
                    
                if event.key == pygame.K_DOWN:
                    hero.y += 20
                    
                if event.key == pygame.K_UP:
                    hero.y -= 20
                    


            if event.type == pygame.KEYUP:
                pass

                

                
            if event.type == pygame.QUIT:
                stop_game = True


        ####### Game logic
          
        # Draw background
        screen.fill(blue_color)

        # (0, 0) and (250, 250) is corrdinates of where the image starts 
        screen.blit(pygame.transform.scale(background_image, (700, 700)), (0, 0))
        # blit = drawing a thing to the screen
        # can put in render later if make class for monster1
        screen.blit(pygame.transform.scale(hero.image, (40, 60)), (hero.x, hero.y))
        screen.blit(pygame.transform.scale(magic_man1.image, (40, 65)), (magic_man1.x, magic_man1.y))
        screen.blit(pygame.transform.scale(lemon_man1.image, (40, 60)), (lemon_man1.x, lemon_man1.y))

        # second_row monsters
        screen.blit(pygame.transform.scale(death.image, (40, 65)), (death.x, death.y))
        screen.blit(pygame.transform.scale(pepperment_butler2.image, (40, 40)), (pepperment_butler2.x, pepperment_butler2.y))

        # thrid_row monsters
        screen.blit(pygame.transform.scale(ice_king3.image, (40, 65)), (ice_king3.x, ice_king3.y))
        screen.blit(pygame.transform.scale(gunter3_1.image, (40, 40)), (gunter3_1.x, gunter3_1.y))
        screen.blit(pygame.transform.scale(gunter3_2.image, (40, 40)), (gunter3_2.x, gunter3_2.y))


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
