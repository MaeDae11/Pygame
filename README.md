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

Difficulties:

    1. Even starting was difficult. Understanding how the module of Pygame interacted with Python and what suffexs to use throughout the code. So in addition of combining all the concepts of the first two weeks of school - variables, modules, functions, classes, etc - we used Pygame features as well.

    2. My main difficulty was collision between the hero and monsters. While I scale how the images show up within the game, the actual image imported was much larger. This lead to collisions being triggered when the two objects did not look close to each other, but were indeed colliding. After help from my team debugging this issue, it was much easier to move forward.


Bugs to figure out later:

    1. How to offically end the game without quitting completely. Right now, the background changes to indicate wheather or not the user has won or lost, but you can still move around as an exploded image. 
    
    2. Condensing my code down. There is a lot of repedition at this time that I would like to condense either over the weekend or down the road. However, with not knowing what Python was a month ago, I'm pretty happy with the product as of right now.

    3. Adding a menu before the game. I'd love to add this feature at some point. Maybe pick which character you would want to play as. And even add more levels.

    4. I tried adding a health item, but for some reason the collision was not working so it is simply commented out at this time.