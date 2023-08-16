import pygame
import random
from pygame import mixer

def check_collision(obj1_x, obj1_y, obj1_width, obj1_height, obj2_x, obj2_y, obj2_width, obj2_height):
    if obj1_x < obj2_x + obj2_width and obj1_x + obj1_width > obj2_x and obj1_y < obj2_y + obj2_height and obj1_y + obj1_height > obj2_y:
        return True
    return False
# Define colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
score = 0
def get_highest_score():
    try:
        with open("highest_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def update_highest_score(score):
    highest_score = get_highest_score()
    if score > highest_score:
        with open("highest_score.txt", "w") as file:
            file.write(str(score))
# Initialize Pygame
pygame.init()
# After initializing Pygame

# Set the window size
SIZE = (800, 600)
screen = pygame.display.set_mode(SIZE)
# sound
mixer.init()
collision_sound = pygame.mixer.Sound("pop.mp3")
game_over_sound = pygame.mixer.Sound("over.wav")
#Load audio file
mixer.music.load('flyBUZZING.mp3')

print("music started playing....")

#Set preferred volume
mixer.music.set_volume(0.4)

#Play the music
mixer.music.play(-1)
# Set the window title
pygame.display.set_caption("Fly vs. Garbage")

# Set up the game clock
clock = pygame.time.Clock()

# Load images
DEFAULT_IMAGE_SIZE = (50, 50)
garbage_list = []
arrow_list = []
heart_list = []
fly_image = pygame.image.load("fly.png")
fly_image = pygame.transform.scale(fly_image, (30, 30))
projectile_image = pygame.image.load("projectile.png")
projectile_image = pygame.transform.scale(projectile_image, (20, 20))
projectiles = []
garbage_image = pygame.image.load("garbage.png")
garbage_image = pygame.transform.scale(garbage_image, DEFAULT_IMAGE_SIZE)
arrow_image = pygame.image.load("arrow.png")
arrow_image = pygame.transform.scale(arrow_image, (20, 20))
heart_image = pygame.image.load("heart.png")
heart_image = pygame.transform.scale(heart_image, (20, 20))
# Set up the starting positions
fly_x = 400
fly_y = 450
#fly_x = random.randint(0, SIZE[0] - fly_image.get_width())
#fly_y = random.randint(0, SIZE[1] - fly_image.get_height())
font = pygame.font.Font(None, 36)
lives = 3
# Inside the game loop, before updating the screen
def_last = -200
def_ammo = 50
last_attack = def_last
ammo = def_ammo
#garbage_x = random.randint(0, SIZE[0] - garbage_image.get_width())
#garbage_y = random.randint(0, SIZE[1] - dinosaur_image.get_height())
#garbage_y =  0
# Set up the game loop
game_over = False
collision_sound_played = False
def game_over_screen():
    # Clear the screen

    game_over_sound.play(maxtime = 1000)

    screen.fill(WHITE)
    
    # Display "Game Over" text in the middle of the screen
    game_over_text = font.render("Game Over", True, BLACK)
    text_rect = game_over_text.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 - 50))
    screen.blit(game_over_text, text_rect)
    
    # Display "Play Again?" prompt
    play_again_text = font.render("Press Enter to play again or Esc to quit.", True, BLACK)
    play_again_rect = play_again_text.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 + 50))
    screen.blit(play_again_text, play_again_rect)
    
    # Update the display
    pygame.display.flip()
    
while not game_over:
    #INSIDE OF THE GAME LOOP
    score += 1
    if (score % 5000 == 0):
        ammo += 50
    if (score % 1500 == 0):
        heart ={"x": random.randint(0, SIZE[0] - heart_image.get_width()), "y": 0}
        #garbage_list.clear()
        #arrow_list.clear()
        heart_list.append(heart)
    # Handle events
    if random.random() < 0.025 + score / 1000000.0:  # Adjust the probability of creating new garbage
        new_garbage = {"x": random.randint(0, SIZE[0] - garbage_image.get_width()), "y": 0}
        garbage_list.append(new_garbage)
    if random.random() < 0.001:
        new_arrow ={"x": 0, "y": random.randint(0, SIZE[0] - arrow_image.get_width())}
        arrow_list.append(new_arrow)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and score > last_attack + 10 and ammo > 0:
        new_projectile = {"x": fly_x, "y": fly_y}
        projectiles.append(new_projectile)
        last_attack = score
        ammo = ammo - 1
    if keys[pygame.K_RIGHT]:
        mixer.music.unpause()
        fly_x += 4
        if fly_x > SIZE[0] - fly_image.get_width():
            fly_x = SIZE[0] - fly_image.get_width()
    if keys[pygame.K_LEFT]:
        mixer.music.unpause()
        fly_x -= 4
        if fly_x < 0:
            fly_x = 0
    if keys[pygame.K_DOWN]:
        mixer.music.unpause()
        fly_y += 4
        if fly_y > SIZE[1] - fly_image.get_height():
            fly_y = SIZE[1] - fly_image.get_height()
    if keys[pygame.K_UP]:
        mixer.music.unpause()
        fly_y -= 4
        if fly_y < 0:
            fly_y = 0
    if not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP]:
        mixer.music.pause()

    for projectile in projectiles:
        projectile["y"] -= 2
        if projectile["x"] < -5:
            projectiles.remove(projectile)
    for garbage in garbage_list:
        garbage["y"] += 2
        if garbage["y"] > 600:
            garbage_list.remove(garbage)
    for arrow in arrow_list:
        arrow["x"] += 2
        if arrow["x"] > 800:
            arrow_list.remove(arrow)

    for heart in heart_list:
        heart["y"] +=4
        if heart["y"] > 600:
            heart_list.remove(heart)
    # Draw the images
    play_again = None
    for garbage in garbage_list:
        for projectile in projectiles:
            if check_collision(projectile["x"], projectile["y"], projectile_image.get_width(), projectile_image.get_height(), garbage["x"], garbage["y"], garbage_image.get_width(), garbage_image.get_height()):
                garbage_list.remove(garbage)
                projectiles.remove(projectile)
                score += 10
        if check_collision(fly_x, fly_y, fly_image.get_width(), fly_image.get_height(), garbage["x"], garbage["y"], garbage_image.get_width(), garbage_image.get_height()):
            lives = lives - 1
            if lives != 0:
                collision_sound.play(maxtime= 1000)
            #collision_sound.stop()
            garbage_list.remove(garbage)
            if lives == 0:

                game_over_screen()
                mixer.music.pause()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:  # Player wants to play again
                                play_again = True
                            elif event.key == pygame.K_ESCAPE:  # Player wants to quit
                                play_again = False
                            game_over = False  # Reset game_over flag
                            break  # Exit the inner loop
                    if play_again is not None:
                        break  # Exit the outer loop if player's response received




    for heart in heart_list:
        if check_collision(fly_x, fly_y, fly_image.get_width(), fly_image.get_height(), heart["x"], heart["y"], heart_image.get_width(), heart_image.get_height()):
            lives += 1
            heart_list.remove(heart)

    for arrow in arrow_list:
        if check_collision(fly_x, fly_y, fly_image.get_width(), fly_image.get_height(), arrow["x"], arrow["y"], arrow_image.get_width(), arrow_image.get_height()):
            lives = 0
            if lives == 0:

                game_over_screen()
                mixer.music.pause()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:  # Player wants to play again
                                play_again = True
                            elif event.key == pygame.K_ESCAPE:  # Player wants to quit
                                play_again = False
                            game_over = False  # Reset game_over flag
                            break  # Exit the inner loop
                    if play_again is not None:
                        break  # Exit the outer loop if player's response received
                    
    if play_again is not None:
        update_highest_score(score)
        if play_again:
            # Reset the game state and variables for a new game
            last_attack = def_last
            ammo = def_ammo
            mixer.music.rewind()
            score = 0
            lives = 3
            garbage_list.clear()
            arrow_list.clear()
            heart_list.clear()
            projectiles.clear()
            fly_x = random.randint(0, SIZE[0] - fly_image.get_width())
            fly_y = random.randint(0, SIZE[1] - fly_image.get_height())
            fly_x = 400
            fly_y = 450 
        else:
            game_over = True  # Exit the game if player chooses not to play again

    if (pygame.mixer.music.get_pos() % 500 == 0):
        mixer.music.rewind()
    
    if (collision_sound_played):
        collision_sound_played = False
        collision_sound.stop
    screen.fill(WHITE)
    screen.blit(fly_image, (fly_x, fly_y))
    for projectile in projectiles:
        screen.blit(projectile_image, (projectile["x"], projectile["y"]))
    for garbage in garbage_list:
        screen.blit(garbage_image, (garbage["x"], garbage["y"]))
    for arrow in arrow_list:
        screen.blit(arrow_image, (arrow["x"], arrow["y"]))
    for heart in heart_list:
        screen.blit(heart_image, (heart["x"], heart["y"]))
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (20, 20))
    lives_text = font.render("Lives: " + str(lives), True, BLACK)
    screen.blit(lives_text, (650, 20))

    lives_text = font.render("Highest: " + str(get_highest_score()), True, BLACK)
    screen.blit(lives_text, (350, 20))
    lives_text = font.render(str(ammo), True, BLACK)
    screen.blit(lives_text, (650, 500))
    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
