#importing
import pygame
import button
import sys
import random

#Initialize
pygame.init()
clock = pygame.time.Clock()

#Screen
screen_width = 800
screen_height = 600
font = pygame.font.SysFont('Palatino', 30)

#Displayer
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Final Fantasy VII')

#set framerate
clock = pygame.time.Clock()

#define player action variables
move_left = False
move_right = False

#Sprites
background_img = pygame.image.load('img/Background/background.png').convert_alpha()
potion_img = pygame.image.load('img/Icons/potion.png').convert_alpha()
sword_img = pygame.image.load('img/Icons/sword.png').convert_alpha()
restart_img = pygame.image.load('img/Icons/restart.png').convert_alpha()


#ColourDefine
WHITE = (255,255,255)

def draw_bg():
    screen.blit(background_img, (0, 0))

#displayering
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, potions, health):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.potions = potions
        self.health = health
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load('img/Knight/Idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
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

        self.rect.x += dx
        self.rect.y += dy


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


#button
potion_button = button.Button(370, 520, potion_img, 1)
attack_button = button.Button(500, 520, sword_img, 1)
restart_button = button.Button(250, 300, restart_img, 1)

#Variables
    #player
player = Soldier('Hero', 200, 400, 3, 5, 10, 100)
    #Enemy
enemy = Soldier('Villain', 400, 400, 3, 5, 10, 100)


run = True
while run:

    clock.tick(60)
    draw_bg()
    player.draw()
    enemy.draw()
    player.move(move_left, move_right)

    #Drawing buttons
    if potion_button.draw(screen):
        player.potions += 1
    if attack_button.draw(screen):
        enemy.health -= random.randint(10, 20)
    
    #Drawing Texts
    draw_text(f'Potions : {player.potions}', font, WHITE, 10, 10)
    draw_text(f'HP : {player.health}', font, WHITE, 10, 35)
    draw_text(f'Potions : {enemy.potions}', font, WHITE, 680, 10)
    draw_text(f'HP : {enemy.health}', font, WHITE, 680, 35)

    #GameLogic

        #health system
    if enemy.health <= 0:
        enemy.health = 0
    if player.health <= 0:
        player.health = 0

        #Death and Restart
    if enemy.health == 0:
        if restart_button.draw(screen):
            player.health = 100
            enemy.health = 100
            player.potions = 0
            enemy.potions = 0    
    if player.health == 0:
        if restart_button.draw(screen):
            player.health = 100
            enemy.health = 100
            player.potions = 0
            enemy.potions = 0

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("aaa")
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_ESCAPE:
                run = False


        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                print("A")
                move_left = False
            if event.key == pygame.K_d:
                move_right = False




    pygame.display.update()

pygame.quit()