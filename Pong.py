
import pygame

from paddle import Paddle
from ball import Ball

pygame.init()

player1 = input('Enter name of player 1')
player2 = input('Enter name of player 2')

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)


# for displaying text on screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])


# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping_Pong_Smash")
font = pygame.font.SysFont(None, 55)


paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(GREEN, 15, 15)
ball.rect.x = 345
ball.rect.y = 195

# Background
background = pygame.image.load("/Users/yathaarthsuri/Desktop/Python 3/venv/Ping_Pong_Smash/Files/wallpaper.png")

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()


all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)


# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


scoreA = 0
scoreB = 0


carryOn = True
while carryOn:
    screen.blit(background, (0, 0))
    text_screen("Ping Pong Smash", RED, 200, 190)
    text_screen("Press Enter To Play", RED, 190, 240)
    text_screen("Made By - Yathaarth Suri", GOLD, 140, 450)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                carryOn = False
    pygame.display.update()
    clock.tick(60)

carryOn = True
# -------- Main Program Loop -----------
while carryOn and (scoreA < 11 and scoreB < 11):
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            while True:
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    pygame.quit()
                    quit()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    break
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                pygame.quit()
                quit()

    # Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    # Game Logic
    all_sprites_list.update()

    # Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 690:
        effect = pygame.mixer.Sound('/Users/yathaarthsuri/Desktop/Python 3/venv/Ping_Pong_Smash/Files/game.wav')
        effect.play()
        scoreA += 1
        ball.rect.x = 250
    if ball.rect.x <= 0:
        effect = pygame.mixer.Sound('/Users/yathaarthsuri/Desktop/Python 3/venv/Ping_Pong_Smash/Files/game.wav')
        effect.play()
        scoreB += 1
        ball.rect.x = 450
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    # Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        effect = pygame.mixer.Sound('/Users/yathaarthsuri/Desktop/Python 3/venv/Ping_Pong_Smash/Files/sound.wav')
        effect.play()
        ball.bounce()

    # Drawing code
    screen.fill(BLACK)
    screen.blit(background, (0, 0))

    # Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # Drawing all sprites
    all_sprites_list.draw(screen)

    # Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    # Updating the screen
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

carryOn = True
while carryOn:
    screen.blit(background, (0, 0))
    if scoreA == 11:
        effect = pygame.mixer.Sound('/Users/yathaarthsuri/Desktop/Python 3/venv/Ping_Pong_Smash/Files/cheer.wav')
        effect.play()
        text_screen(f'{player1} Wins', RED, 200, 190)
        text_screen("To Quit Press x", RED, 180, 240)
    else:
        effect = pygame.mixer.Sound('/Users/yathaarthsuri/Desktop/Python 3/venv/Ping_Pong_Smash/Files/cheer.wav')
        effect.play()
        text_screen(f'{player2} Wins', RED, 200, 190)
        text_screen("To Quit Press x", RED, 180, 240)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                pygame.quit()
    pygame.display.update()
    clock.tick(60)
    pygame.mixer.music.stop()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
