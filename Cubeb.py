# In the first demo, I copy-pasted the Coding with Russ platformer tutorial Part 1, for learning purposes (youtube.com/watch?v=Ongc4EVqRjo)
# In this demo and moving forward, I will use Russ's Scrolling Shooter Game tutorial as a backbone for my game (youtube.com/playlist?list=PLjcN1EyupaQm20hlUE11y9y8EY2aXLpnv)

import pygame
import os
from pygame.locals import *

pygame.init()

screen_height = 720
screen_width = int(screen_height * 1.77777777778)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Cubeb (BETA)') # Cubeb, a PyGame group project made for Computer Science II (Python) @ Howard University [CSCI 136-02 Fall 2021, Group #14]

# Setting framerate here
clock = pygame.time.Clock()
FPS = 60

# Defining game variables
GRAVITY = 0.75

# Defining player action variables
moving_left = False
moving_right = False
jumped_up = False

#define colours
BG = (50, 50, 100)
RED = (255, 0, 0)

def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0, 300), (screen_width, 300))



class Character(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        
        #load all images for the players
        animation_types = ['Idle', 'Run', 'Jump']
        for animation in animation_types:
            #reset temporary list of images
            temp_list = []
            #count number of files in the folder
            num_of_frames = len(os.listdir(f'RussScrollingShooter/img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'RussScrollingShooter/img/{self.char_type}/{animation}/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def move(self, moving_left, moving_right):
        #reset movement variables
        dx = 0
        dy = 0

        #assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        #jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        #apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        #check collision with floor
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy


    def update_animation(self):
        #update animation
        ANIMATION_COOLDOWN = 100
        #update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0



    def update_action(self, new_action):
        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()



    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)



player = Character('player', 200, 200, 3, 5)
enemy = Character('enemy', 400, 200, 3, 5)



run = True
while run:

    clock.tick(FPS)

    draw_bg()

    player.update_animation()
    player.draw()
    enemy.draw()


    #update player actions
    if player.alive:
        if player.in_air:
            player.update_action(2)#2: jump
        elif moving_left or moving_right:
            player.update_action(1)#1: run
        else:
            player.update_action(0)#0: idle
        player.move(moving_left, moving_right)


    for event in pygame.event.get():
        # This allows me to press the X at the top right, to quit the game.
        if event.type == pygame.QUIT:
            run = False
        # This is for keyboard input for when the keys are pressed; currently using WASD.
        if event.type == pygame.KEYDOWN and player.alive:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                player.jump = True
            if event.key == pygame.K_ESCAPE:
                run = False


        # This is for keyboard input for when the keys are released; currently using WASD.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False




    pygame.display.update()

pygame.quit()

# #define game variables
# tile_size = 50

# #load images
# sun_img = pygame.image.load('img/sun.png')
# bg_img = pygame.image.load('img/sky.png')

# def draw_grid():
#     for line in range(0, 20):
#         pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
#         pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

# class World():
#     def __init__(self, data):
#         self.tile_list = []

#         #load images
#         dirt_img = pygame.image.load('img/dirt.png')
#         grass_img = pygame.image.load('img/grass.png')

#         row_count = 0
#         for row in data:
#             col_count = 0
#             for tile in row:
#                 if tile == 1:
#                     img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
#                     img_rect = img.get_rect()
#                     img_rect.x = col_count * tile_size
#                     img_rect.y = row_count * tile_size
#                     tile = (img, img_rect)
#                     self.tile_list.append(tile)
#                 if tile == 2:
#                     img = pygame.transform.scale(grass_img, (tile_size, tile_size))
#                     img_rect = img.get_rect()
#                     img_rect.x = col_count * tile_size
#                     img_rect.y = row_count * tile_size
#                     tile = (img, img_rect)
#                     self.tile_list.append(tile)
#                 col_count += 1
#             row_count += 1

#     def draw(self):
#         for tile in self.tile_list:
#             screen.blit(tile[0], tile[1])

# world_data = [
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
# [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
# [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
# [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
# [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
# [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

# world = World(world_data)

# run = True
# while run:

#     screen.blit(bg_img, (0, 0))
#     screen.blit(sun_img, (100, 100))

#     world.draw()

#     draw_grid()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     pygame.display.update()

# pygame.quit()