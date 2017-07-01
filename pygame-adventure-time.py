import pygame
import random

# win the game / treasure class
class Treasure(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.topleft = self.x, self.y
    
# playable hero class
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

# monster class
class Monsters(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed_x, speed_y ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.speed_y = speed_x
        self.speed_x = speed_y

    def update(self):
        self.y += self.speed_y
        if self.y >= 680:
            self.y = 10
        self.rect.topleft = self.x, self.y


# main function to run game
def main():

    width = 700
    height = 700
    
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
    magic_man1 = Monsters(magic_man, 100, random.randint(30, 100), 2, 2)
    lemon_man1 = Monsters(lemon_man, 100, random.randint(280, 375), 2, 2)
    
    # second row of monsters and setup of class
    death2 = Monsters(death, 300, 100, 3, 3)
    pepperment_butler2 = Monsters(pepperment_butler, 300, 400, 3, 3)

    # third row of monsters and setup of class
    ice_king3 = Monsters(ice_king, 500, 375, 4, 4)
    gunter3_1 = Monsters(gunter_image, 500, 40, 4, 4)
    gunter3_2 = Monsters(gunter_image, 500, 475, 4, 4)

    # monster group for collosion
    monsters = [magic_man1, lemon_man1, death2, pepperment_butler2, ice_king3, gunter3_1, gunter3_2]
    monsters_group = pygame.sprite.RenderPlain(monsters)

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
        collisions_monsters = pygame.sprite.groupcollide(hero_group, monsters_group, False, False)


        if hero.life > 0:
            if collisions_monsters:
                hero.life = hero.life - 1
                hero.y = 350
                hero.x = 30
                print hero.life

        # game over title
        if hero.life == 0:
            hero.image = pygame.image.load('images/explosion.png')
            background_image = pygame.image.load('images/game_over.png')
            print "Game Over"
        
        # collision with treasure chest to win game
        collision_treausre_chest = pygame.sprite.groupcollide(hero_group, treasure_found, False, False)
    
        # win game title
        if collision_treausre_chest:
            background_image = pygame.image.load('images/adventure_time_background.png')
            print "You won!"
    

        for event in pygame.event.get():
            
        # movement for Hero character
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.x -= 20
                if event.key == pygame.K_RIGHT:
                    hero.x += 20
                if event.key == pygame.K_DOWN:
                    hero.y += 20
                if event.key == pygame.K_UP:
                    hero.y -= 20

            # incase would like to add more key features latere
            if event.type == pygame.KEYUP:
                pass
            
            # stops game
            if event.type == pygame.QUIT:
                stop_game = True
        

        ####### Game logic
          
        # Draw background
        # (0, 0) and (250, 250) is corrdinates of where the image starts 
        screen.blit(pygame.transform.scale(background_image, (700, 700)), (0, 0))
        screen.blit(pygame.transform.scale(treasure.image, (60, 60)), (treasure.x, treasure.y))

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
