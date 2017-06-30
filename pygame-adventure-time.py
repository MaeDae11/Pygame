import pygame
import random

class Treasure(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.topleft = self.x, self.y
    


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        x = 30
        y = 350
        life = 3
        self.image = pygame.image.load('images/finn_resized.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.life = life
        
    def update(self):
        self.rect.topleft = self.x, self.y


# first row of monsters
class First_Row(pygame.sprite.Sprite):
    def __init__(self, image, y):
        pygame.sprite.Sprite.__init__(self)
        x = 100
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

        
# second row of monsters
class Second_Row(pygame.sprite.Sprite):
    def __init__(self, image, y):
        pygame.sprite.Sprite.__init__(self)
        x = 300
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

# third row of monsters / move fastes
class Third_Row(pygame.sprite.Sprite):
    def __init__(self, image, y):
        pygame.sprite.Sprite.__init__(self)
        x = 500
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.speed_y = 4
        self.speed_x = 4

    def update(self):
        self.y += self.speed_y
        if self.y >= 680:
            self.y = 10
        self.rect.topleft = self.x, self.y
    








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

# could not get health to collide
    # health_image = 'images/heart.png'
    # health = Treasure(random.randint(200, 500), random.randint(200, 500), health_image)
    # health_group = [health]
    # health_found = pygame.sprite.RenderPlain(health_group)

    treasure_image = 'images/treasure.png'
    treasure = Treasure(650, random.randint(200, 500), treasure_image)
    treasure_group = [treasure]
    treasure_found = pygame.sprite.RenderPlain(treasure_group)


    # hero image and setup of class
    hero = Hero()
    hero_player = [hero]
    hero_group = pygame.sprite.RenderPlain(hero_player)
    # first row of monsters and setup of class
    magic_man1 = First_Row(magic_man, random.randint(30, 100))
    lemon_man1 = First_Row(lemon_man, random.randint(280, 375))
    monsters_first_row = [magic_man1, lemon_man1]
    monsters_first_row_group = pygame.sprite.RenderPlain(monsters_first_row)
    
    # second row of monsters and setup of class
    death2 = Second_Row(death, 100)
    pepperment_butler2 = Second_Row(pepperment_butler, 300)
    monsters_second_row = [death2, pepperment_butler2]
    monsters_second_row_group = pygame.sprite.RenderPlain(monsters_second_row)

    # third row of monsters and setup of class
    ice_king3 = Third_Row(ice_king, 375)
    gunter3_1 = Third_Row(gunter_image, 40)
    gunter3_2 = Third_Row(gunter_image, 475)
    monsters_third_row = [ice_king3, gunter3_1, gunter3_2]
    monsters_third_row_group = pygame.sprite.RenderPlain(monsters_third_row)
    
    

    stop_game = False
    
    # giant loop for game
    # while not stop_game --> while stop_game is false)
    while not stop_game:
        # loops for all events of key up/down etc or mouse clicks. what are you looking for?
        hero.update()
        treasure.update()

        magic_man1.update()
        lemon_man1.update()

        death2.update()
        pepperment_butler2.update()

        ice_king3.update()
        gunter3_1.update()
        gunter3_2.update()

        # collide with monster and loose game
        collisions_1st_row = pygame.sprite.groupcollide(hero_group, monsters_first_row_group, False, False)
        collisions_2nd_row = pygame.sprite.groupcollide(hero_group, monsters_second_row_group, False, False)
        collisions_3rd_row = pygame.sprite.groupcollide(hero_group, monsters_third_row_group, False, False)
        # collision_health = pygame.sprite.groupcollide(hero_group, health_found, False, False)

        if hero.life > 0:
            if collisions_1st_row or collisions_2nd_row or collisions_3rd_row:
                hero.life = hero.life - 1
                hero.y = 350
                hero.x = 30
                print hero.life

        if hero.life == 0:
            hero.image = pygame.image.load('images/explosion.png')
            background_image = pygame.image.load('images/game_over.png')
            print "Game Over"
        
        # if collision_health:
        #     hero.life = hero.life + 1
        #     print hero.life

        # collide with treasure chest and win game
        collision_treausre_chest = pygame.sprite.groupcollide(hero_group, treasure_found, False, False)
        if collision_treausre_chest:
            background_image = pygame.image.load('images/adventure_time_background.png')
            print "You won!"
    
        

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
        

        # (0, 0) and (250, 250) is corrdinates of where the image starts 
        screen.blit(pygame.transform.scale(background_image, (700, 700)), (0, 0))
        screen.blit(pygame.transform.scale(treasure.image, (60, 60)), (treasure.x, treasure.y))
        # screen.blit(pygame.transform.scale(health.image, (40, 40)), (health.x, health.y))

        # blit = drawing a thing to the screen
        # can put in render later if make class for monster1
        screen.blit(pygame.transform.scale(hero.image, (45, 65)), (hero.x, hero.y))
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
