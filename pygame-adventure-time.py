import pygame
import random

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        x = 600
        y = 600
        self.image = pygame.image.load('images/finn_resized.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        
        # self.life = 3
    def update(self):
        self.rect.topleft = self.x, self.y
        

    # def collide_rect(self, monster):
    #     collide_hero = pygame.sprite.spritecollide(self, monster, True)


class First_Row(pygame.sprite.Sprite):
    def __init__(self, image, y):
        pygame.sprite.Sprite.__init__(self)
        x = 80
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.speed_y = 2
        self.speed_x = 2

    def update(self):
        self.y += self.speed_y
        if self.y >= 680:
            self.y = 10
        self.rect.topleft = self.x, self.y
    # def collide_rect(self, hero):
    #     collide_monster = pygame.sprite.spritecollide(self, hero, True)
        

class Second_Row(pygame.sprite.Sprite):
    def __init__(self, image, y):
        pygame.sprite.Sprite.__init__(self)
        x = 275
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed_y = 3
        self.speed_x = 3

    def update(self):
        self.y += self.speed_y
        if self.y >= 680:
            self.y = 10
        self.rect.topleft = self.x, self.y

class Third_Row(pygame.sprite.Sprite):
    def __init__(self, image, y):
        pygame.sprite.Sprite.__init__(self)
        x = 500
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        # self.collide = pygame.sprite.spritecollide()
        self.x = x
        self.y = y
        self.speed_y = 4
        self.speed_x = 4

    def update(self):
        self.y += self.speed_y
        if self.y >= 680:
            self.y = 10
        self.rect.topleft = self.x, self.y
    
    # def kill(self):








def main():

    width = 700
    height = 700
    blue_color = (97, 159, 182)
    
    pygame.init()

    

    # everything done to screen, must be tuple otherwise python would read it as two separate things
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Adventure Time!!!')
    clock = pygame.time.Clock()

    # background image of treese
    background_image = pygame.image.load('images/background.png').convert_alpha()

    # monster images
    magic_man = 'images/magic_man.png'
    lemon_man = 'images/lemon_man.png' 
    death = 'images/death.png'
    pepperment_butler = 'images/pepperment_butler.png'   # pepperment monster
    ice_king = 'images/ice_king.png'     # blue character
    gunter_image = 'images/gunter.png'    # penguin monster

    # hero image and setup of class
    hero = Hero()
    hero_player = [hero]
    hero_group = pygame.sprite.RenderPlain(hero_player)
    # first row of monsters and setup of class
    magic_man1 = First_Row(magic_man, 60)
    lemon_man1 = First_Row(lemon_man, 400)
    monsters_first_row = [magic_man1]
    monsters_first_row_group = pygame.sprite.RenderPlain(monsters_first_row)
    
    # second row of monsters and setup of class
    death2 = Second_Row(death, 100)
    pepperment_butler2 = Second_Row(pepperment_butler, 300)

    # third row of monsters and setup of class
    ice_king3 = Third_Row(ice_king, 375)
    gunter3_1 = Third_Row(gunter_image, 40)
    gunter3_2 = Third_Row(gunter_image, 475)
    
    

    stop_game = False
    
    # giant loop for game
    # while not stop_game --> while stop_game is false)
    while not stop_game:
        # loops for all events of key up/down etc or mouse clicks. what are you looking for?
        hero.update()

        magic_man1.update()
        lemon_man1.update()

        death2.update()
        pepperment_butler2.update()

        ice_king3.update()
        gunter3_1.update()
        gunter3_2.update()

        
        collisions = pygame.sprite.groupcollide(hero_group, monsters_first_row_group, False, False)
        # pygame.sprite.spritecollide(hero_group, monsters_first_row_group, True):
        if collisions:
            print collisions

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
        # screen.fill(blue_color)

        # (0, 0) and (250, 250) is corrdinates of where the image starts 
        screen.blit(pygame.transform.scale(background_image, (700, 700)), (0, 0))

        # blit = drawing a thing to the screen
        # can put in render later if make class for monster1
        screen.blit(pygame.transform.scale(hero.image, (40, 60)), (hero.x, hero.y))
        screen.blit(pygame.transform.scale(magic_man1.image, (40, 65)), (magic_man1.x, magic_man1.y))
        screen.blit(pygame.transform.scale(lemon_man1.image, (40, 60)), (lemon_man1.x, lemon_man1.y))

        # second_row monsters
        screen.blit(pygame.transform.scale(death2.image, (40, 65)), (death2.x, death2.y))
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
