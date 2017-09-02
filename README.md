# Pygame

Pygame is created from an imported module from Python and is completed with only Python code.

The game is structured around the same concept of Frogger. In this game you don't want to touch the monsters rolling down on the screen. Each row goes a bit faster as you get closer to the right side. 

You start with Life = 3. If you touch a monster, you are transported back to the start with a life gone. 

All along, the goal is to reach the treasure chest on the other side. (basically move left to right).


The project began with a rough outline:
    1. defined function main()
    2. pygame.init()
    3. stop_game = False
    4. while not stop_game:
    4. pygame.quit()
     <!--finally calling the main function to start the game-->
    5. if __name__ == '__main__':
           main()


From there, the addition of hero and one monster was made. This lead to using classes, additional functions and building on top of the outline.

<b>Difficulties:</b>

    1. Even starting was difficult. Understanding how the module of Pygame interacted with Python and what suffexs to use throughout the code. So in addition of combining all the concepts of the first two weeks of school - variables, modules, functions, classes, etc - we used Pygame features as well.

    2. My main difficulty was collision between the hero and monsters. While I scale how the images show up within the game, the actual image imported was much larger. This lead to collisions being triggered when the two objects did not look close to each other, but were indeed colliding. After help from my team debugging this issue, it was much easier to move forward.


<b>Bugs to figure out later:</b>

    1. How to offically end the game without quitting completely. Right now, the background changes to indicate wheather or not the user has won or lost, but you can still move around as an exploded image. 
    
    2. Condensing my code down. There is a lot of repedition at this time that I would like to condense. However, with not knowing what Python was a month ago, I'm pretty happy with the product as of right now.

    3. Adding a menu before the game. I'd love to add this feature at some point. Maybe pick which character you would want to play as. And even add more levels.


<b>Images</b>
<img src="images/Pygame-Play-Screen.png" alt="screen shot of pygame demo with forest background. displays monsters, Hero, heath heart and treasure chest">
<h4>Game play is structured like the game Frogger. You start on one side of the screen and avoid the monsters as you try and reach the treasure chest to win</h4>
<h4>The user Hero out with 3 lives. Each time the Hero runs into a monster, 1 life is lost. If the Hero obtains a heart, the Hero gains 1 life.</h4>
<br />

<img src="images/Pygame-Win-Screen.png" alt="screen shot of pygame demo when Hero wins">
<h4>This is the screen that shows when the Hero crosses the monsters path and reaches the treasure chest</h4>
<br />

<img src="images/Pygame-GameOver-Screen.png" alt="screen show ot pygame demo when Hero looses">
<h4>Unfortunatly, if the Hero is unable to avoid the monsters and lives reach zero, the Hero has lost his quest for the treasure chest.</h4>
<br />

<h2>Code snipits</h2>
<h4>Below establishes the different classes of Hero and Mosters</h4>

```
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
        self.life_stage = "Life: "
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

```
