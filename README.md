Fly Vs Garbage
#### Video Demo:  https://youtu.be/wZ9fwsB40Z4
#### Description:
This project is a game built using python especially a library called pygame.
The game is called Fly Vs. Garbage where a fly is trying to survive being hit by bags of garbage upon collision with a bag the fly will lose a life also there are arrows that run from the sides which immediately eliminate the fly.
some hearts can be collected increasing the lives of the fly and also the fly can fire shoots that can destroy the garbage bags but nothing else.

The Code in this game is all inside app.py; after some initializations and loading images there are multiple functions and multiple sounds that will be explained soon:

There are multiple objects in this game: the fly that is surviving and the arrows that can kill it and the garbage bags and the hearts and the shoots that the fly shoots to destroy the garbage bag and each of them has its own image and dimensions
the first one is a function that checks if two objects have collided using their coordinates it checks if two objects are touching each other using the dimensions of the first object's image and its coordinates and the dimensions of the second object and its coordinates then returns true if they are touching or false if they are not
the second one is a game over screen that prints for the user whether he wants to exit or continue playing first it fills the screen with white then prints "game over" then prints "Press Enter to play again or Esc to quit."
then there is the main loop in which all other logic of creating garbage bag and arrows using random variables then adding them to a list also it checks for collision with the fly with each of the garbage and arrows using the first function to decide whether to end the game or decrease a life
also there is the logic of the shoots that the fly can shoot to eliminate the garbage bags
First the score is incremented in the main loop and it is checked if a certain limit has been achieved so that a new heart can drop then a random number is generated to decide if a new garbage bag should drop or not then another random variable for the arrows.
all the arrows move right on the x axis and the garbage bags move down on the y axis.
the fly can move in all four directions and can shoot a projectile using the space button that goes upwards to destroy the garbage bag.
the main loop checks for collision with the fly and the garbage bags to decrease its lives and checks with collision with the hearts to increase the lives of the fly and checks for collision with the arrows to kill the fly.
the main loop also checks for collision with the projectiles and the garbage bag to be destroyed.
there are multiple sounds in the game: the first one is the fly buzzing when it moves the second one is the game over sound when the fly dies also there is a pop sound when the fly collides with a garbage bag.
