import pygame as pg
import pygame.time
from classes import Player, Missile, Lives, Enemy, Enemy2, EnemyMissile
import random



# Constants & game values
BACKGROUND_COLOR = '#141A26'
WHITE = (255, 255, 255)
score = 0
level = 1


# initialize pygame
pg.init()


# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 900

display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption('Space Invaders')
display_surface.fill(BACKGROUND_COLOR)

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()


# Create player group
player = Player(WINDOW_WIDTH//2, 880)
player_group = pygame.sprite.Group()
player_group.add(player)

# Create missile group
missile_group = pg.sprite.Group()

# Create enemy group and enemies
enemies_group = pygame.sprite.Group()
for row in range(90, 330, 80):
    for i in range(30, 460, 75):
        enemy = Enemy(i, row)
        enemies_group.add(enemy)
    for i in range(30, 460, 75):
        enemy = Enemy2(i, row+40)
        enemies_group.add(enemy)

# create enemy missile group
enemy_missile_group = pygame.sprite.Group()


# ======= HUD ===== #
# Set fonts
font = pygame.font.Font('assets/Tvcd-d92gK.ttf', 25)

# Set Text
score_text = font.render(f'Score: {score}', True, WHITE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)
#
# Create lives
# lives_group = pygame.sprite.Group()
# for i in range(500, 620, 40):
#     life = Lives(i, 35)
#     lives_group.add(life)
lives = 3
lives_text = font.render(f'Lives: {lives}', True, WHITE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (580, 10)


game_over_text = font.render('Final Score: ' + str(score), True, WHITE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render('Press any key to play again', True, WHITE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

# Main game loop
running = True

# load and play background music
pygame.mixer.music.load('assets/bg_music.mp3')
pygame.mixer.music.play(-1, 0.0)


while running:
    #Loop through a list of Event objects that have occured
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Missile launch
        if event.type == pygame.KEYDOWN and len(missile_group) == 0:
            if event.key == pg.K_SPACE:
                missile = Missile(player.rect.centerx, 870)
                missile_group.add(missile)


    # Check for collisions
    if pygame.sprite.groupcollide(missile_group, enemies_group, True, True):
        score += 10


    if pygame.sprite.groupcollide(enemy_missile_group, player_group, True, False):
        player.rect.x = WINDOW_WIDTH // 2
        lives -= 1


    # Update HUD
    score_text = font.render(f'Score: {score}', True, WHITE)
    lives_text = font.render(f'Lives: {lives}', True, WHITE)

    # Check for Game Over
    if lives == 0:
        game_over_text = font.render('Final Score: ' + str(score), True, WHITE)
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        #Pause the ga,e until the player presses the key
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    lives = 3
                    player.rect.x = WINDOW_WIDTH // 2
                    pygame.mixer.music.play()
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False






    #Fill display surface
    display_surface.fill(BACKGROUND_COLOR)

    #Update and draw assets
    player_group.update()
    player_group.draw(display_surface)

    missile_group.update()
    missile_group.draw(display_surface)

    # lives_group.update()
    # lives_group.draw(display_surface)


    if any(e for e in enemies_group if e.rect.left < 10 or e.rect.right > 590):
        for e in enemies_group:
            e.change_direction()

    enemies_group.update()
    enemies_group.draw(display_surface)

    # Fire enemy missle
    for e in enemies_group:
        num = random.randint(1,4500)
        if num == 1:
            enemy_missile = EnemyMissile(e.rect.x, e.rect.y)
            enemy_missile_group.add(enemy_missile)

    enemy_missile_group.update()
    enemy_missile_group.draw(display_surface)

    # Blit HUD
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)

    # Update the display
    pg.display.update()



    # Tic the clock
    clock.tick(FPS)

# End the Game
pg.quit()