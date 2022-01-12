# importing
import random

import pygame

import button

# Initialize
pygame.init()
clock = pygame.time.Clock()

# Screen
screen_width = 1920
screen_height = 1080
font = pygame.font.SysFont('Futura', 50)

# Displayer
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Final Fantasy VII')

# set framerate
clock = pygame.time.Clock()

# define player action variables
move_left = False
move_right = False
moveE_left = False
moveE_right = False
GRAVITY = 0.75

# Sprites
background_img = pygame.image.load('img/Background/bg.png').convert_alpha()
potion_img = pygame.image.load('img/Icons/potion.png').convert_alpha()
medium_potion_img = pygame.image.load('img/Icons/big_potion.png').convert_alpha()
high_potion_img = pygame.image.load('img/Icons/high_potion.png').convert_alpha()
sword_img = pygame.image.load('img/Icons/sword.png').convert_alpha()
restart_img = pygame.image.load('img/Icons/restart.png').convert_alpha()
victory_img = pygame.image.load('img/Icons/victory.png').convert_alpha()
exit_img = pygame.image.load('img/exit_btn.png').convert_alpha()

# ColourDefine
WHITE = (255, 255, 255)


def draw_bg():
    screen.blit(background_img, (0, 0))

# displayering

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, potions, health):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.score = 0
        self.char_type = char_type
        self.potions = potions
        self.health = health
        self.jump = False
        self.fire = False
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.flip = False
        self.animationlist = []
        self.action = 0
        self.index = 0
        self.update_time = pygame.time.get_ticks()
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            temp_list = []
            for i in range(5):
                img = pygame.image.load(f'img/{self.char_type}/Idle/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animationlist.append(temp_list)
            temp_list = []
            for i in range(6):
                img = pygame.image.load(f'img/{self.char_type}/Run/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animationlist.append(temp_list)
            temp_list = []
            for i in range(1):
                img = pygame.image.load(f'img/{self.char_type}/Jump/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animationlist.append(temp_list)
            temp_list = []
            for i in range(8):
                img = pygame.image.load(f'img/{self.char_type}/Death/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animationlist.append(temp_list)
        self.image = self.animationlist[self.action][self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, move_left, move_right):
        dx = 0
        dy = 0

        if move_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if move_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        if self.jump == True:
            self.vel_y = -15
            self.jump = False

        self.vel_y += GRAVITY
        if self.vel_y > 800:
            self.vel_y
        dy += self.vel_y

        if self.rect.bottom + dy > 850:
            dy = 850 - self.rect.bottom

        if self.fire:
            self.Fire(enemy)
            self.fire = False

        self.rect.x += dx
        self.rect.y += dy

    def animation(self):
        ANIMATION_COOLDOWN = 100
        self.image = self.animationlist[self.action][self.index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.index += 1
        if self.index >= len(self.animationlist[self.action]):
            self.index = 0

    def actions(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def moveE(self, moveE_left, moveE_right):
        dx = 0
        dy = 0
        if moveE_left:
            dx = -self.speed
            self.flip = False
            self.direction = 1
        if moveE_right:
            dx = self.speed
            self.flip = True
            self.direction = -1

        if self.jump == True:
            self.vel_y = -15
            self.jump = False

        self.vel_y += GRAVITY
        if self.vel_y > 800:
            self.vel_y
        dy += self.vel_y

        if self.rect.bottom + dy > 850:
            dy = 850 - self.rect.bottom

        if self.fire:
            self.Fire(player)
            self.fire = False

        self.rect.x += dx
        self.rect.y += dy

    def Fire(self, target):
        target.health -= random.randint(10, 20)


# button
potion_button = button.Button(260, 520, potion_img, 1)
mpotion_button = button.Button(330, 520, medium_potion_img, 1)
hpotion_button = button.Button(400, 520, high_potion_img, 1)
attack_button = button.Button(500, 520, sword_img, 1.5)
restart_button = button.Button(660, 300, restart_img, 2)
exit_button = button.Button(730, 600, exit_img, 2)

# Variables
# player
player = Soldier('Hero', 400, 800, 3, 5, 10, 100)
# Enemy
enemy = Soldier('Villian', 1450, 800, 3, 5, 10, 100)
run = True
while run:

    clock.tick(60)
    draw_bg()
    player.animation()
    enemy.animation()
    player.draw()
    enemy.draw()
    # GameLogic
    # health system
    if enemy.health <= 0:
        enemy.health = 0
    if player.health <= 0:
        player.health = 0

    # Death and Restart
    if enemy.health <= 0:
        enemy.health = 0
        enemy.alive = False
        enemy.actions(3)
        if restart_button.draw(screen):
            player.score += 1
            player.health = 100
            player.rect.x = 400
            enemy.rect.x = 1450
            enemy.health = 100
            player.potions = 10
            enemy.potions = 10
            enemy.alive = True
        if exit_button.draw(screen):
            run = False
        else:
            player.actions(3)
    if player.health <= 0:
        player.health = 0
        player.alive = False
        enemy.actions(3)
        if restart_button.draw(screen):
            enemy.score += 1
            player.health = 100
            player.rect.x = 400
            enemy.rect.x = 1450
            enemy.health = 100
            player.potions = 10
            enemy.potions = 10
            player.alive = True
        if exit_button.draw(screen):
            run = False
    # potions
    if player.potions <= 0:
        player.potions = 0

    # PlayerMovement
    if player.alive:
        if move_left or move_right:
            player.move(move_left, move_right)
            player.actions(1)
        else:
            player.actions(0)
    else:
        player.actions(3)

    # EnemyMovement
    if enemy.alive:
        if enemy.jump:
            enemy.actions(2)
        if moveE_left or moveE_right:
            enemy.actions(1)
        else:
            enemy.actions(0)
        enemy.move(moveE_left, moveE_right)
    else:
        enemy.actions(3)

    # Scoreboard
    if player.score != 0 or enemy.score != 0:
        if enemy.score + player.score == 5:
            if enemy.score > player.score:
                enemy.draw_text(f'Villian won againt the Hero', pygame.font.SysFont('Palatino', 80), WHITE, 600, 310)
            if enemy.score < player.score:
                enemy.draw_text(f'Hero won againt the Villian', pygame.font.SysFont('Palatino', 80), WHITE, 600, 310)
            if enemy.score == player.score:
                enemy.draw_text(f'Villian and Hero have a draw match', pygame.font.SysFont('Palatino', 80), WHITE, 600,
                                310)

    # Drawing buttons
    if potion_button.draw(screen):
        player.potions -= 1
        player.health += random.randint(5, 10)
    if mpotion_button.draw(screen):
        player.potions -= 1
        player.health += random.randint(10, 15)
    if hpotion_button.draw(screen):
        player.potions -= 1
        player.health += random.randint(15, 20)
    if attack_button.draw(screen):
        player.Fire(enemy)

    # Drawing Texts
    player.draw_text(f'Score : {player.score}', font, WHITE, 220, 265)
    player.draw_text(f'Potions : {player.potions}', font, WHITE, 220, 175)
    player.draw_text(f'HP : {player.health}', font, WHITE, 220, 220)
    player.draw_text(f'Name : {player.char_type}', font, WHITE, 220, 130)
    enemy.draw_text(f'Score : {enemy.score}', font, WHITE, 1450, 265)
    enemy.draw_text(f'Potions : {enemy.potions}', font, WHITE, 1450, 175)
    enemy.draw_text(f'HP : {enemy.health}', font, WHITE, 1450, 220)
    enemy.draw_text(f'Name : {enemy.char_type}', font, WHITE, 1450, 130)

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_LEFT:
                moveE_left = True
            if event.key == pygame.K_RIGHT:
                moveE_right = True
            if event.key == pygame.K_LCTRL:
                pygame.mouse.set_visible(True)
            if event.key == pygame.K_w and player.alive and player.jump == False and player.vel_y > 10:  # player jump
                player.jump = True
            if event.key == pygame.K_RETURN and enemy.alive:  # fire to player
                enemy.fire = True
            if event.key == pygame.K_UP and enemy.alive and enemy.jump == False and enemy.vel_y > 10: # enemy jump
                enemy.jump = True
            if event.key == pygame.MOUSEBUTTONDOWN:   # fire to enemy
                if event.button == 1:
                    if enemy.alive and player.alive: # fire to enemy
                        player.fire = True
        # keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w and player.jump == True:
                player.jump = False
            if event.key == pygame.K_UP and enemy.jump == True:  # enemy jump
                enemy.jump = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_LEFT:
                moveE_left = False
            if event.key == pygame.K_RIGHT:
                moveE_right = False
            if event.key == pygame.K_SPACE:
                player.jump = False
            if event.key == pygame.K_RETURN:
                enemy.fire = False
            if event.key == pygame.MOUSEBUTTONUP:  # fire to enemy
                if event.button == 1:
                    player.fire = False # fire to enemy

    pygame.display.update()

pygame.quit()
