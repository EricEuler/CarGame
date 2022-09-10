import multiprocessing
import random
import pygame
import _thread as thread
import functions
from functions import scale_image
import sys
import time
import math
import random
import street_movement
from multiprocessing import Process
import threading

STREET = pygame.image.load("Street2.png")
STREET2 = pygame.image.load("Street2.png")
CAR_BROKE_RED = scale_image(pygame.image.load("Car_broke_red.png"), 4.0)
TRUCK_BROKE = scale_image(pygame.image.load("Truck_broke.png"), 4.0)
YASSIN = pygame.image.load("Yassin.jpeg")
pygame.mixer.init()
STREET_WIDTH, STREET_HEIGHT = STREET.get_width(), STREET.get_height()
crashed = False


def spawn_obstacle():
    while True:
        time.sleep(2)
        print("Obstacle")
    while True:
        obstacle_x_1 = 100
        obstacle_y_1 = 100
        obstacle_x_2 = 0
        obstacle_y_2 = 0
        obstacle_x_3 = 0
        obstacle_y_3 = 0
        obstacle_x_4 = 0
        obstacle_y_4 = 0
        # WIN.blit(CAR_BROKE_RED, (obstacle_x_1, obstacle_y_1)) #spawn the obstacle

        random_int = random.randint(0, 3)
        if random_int == 0:  # Car Red Broke
            print("Random 0")


def game():
    color = "RED"
    WIN = pygame.display.set_mode((STREET_WIDTH, STREET_HEIGHT))
    pygame.display.set_caption("Yalla Yassin!")
    pygame.display.set_icon(YASSIN)
    WIN.blit(STREET, (0, 0))
    global Car  # Init
    car_x = 120  # 1: 120 #2: 345 3: 570 4:795
    car_y = 860  # 860

    if color == "RED":
        Car = scale_image(pygame.image.load("Car_red.png"), 4.0)
    if color == "GREEN":
        Car = scale_image(pygame.image.load("Car_green.png"), 4.0)  # choose Color
    if color == "BLUE":
        Car = scale_image(pygame.image.load("Car_blue.png"), 4.0)

    WIN.blit(Car, (car_x, car_y))

    pygame.mixer.music.load("Mario_soundtrack.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.06)  # Music
    run_game = True
    while run_game:
        pygame.display.update()

        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 25)  # FPS
        fps = str(int(clock.get_fps()))
        fps_t = font.render(fps, True, pygame.Color("Black"))
        WIN.blit(fps_t, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if not car_y < 10:
                        car_y -= 40
                elif event.key == pygame.K_s:
                    if not car_y > 860:
                        car_y += 40
                elif event.key == pygame.K_d:  # key inputs
                    if not car_x >= 795:
                        car_x += 225  # 40
                        time.sleep(0.02)
                elif event.key == pygame.K_a:
                    if not car_x <= 120:
                        car_x -= 225  # 40

            WIN.blit(STREET, (0, 0))
            WIN.blit(Car, (car_x, car_y))
            WIN.blit(TRUCK_BROKE, (120, 100))
        time.sleep(0.05)



def start_game(color):
    thr_game = threading.Thread(target=game)
    thr_obstacle = threading.Thread(target=spawn_obstacle)
    # thr_street_movement = threading.Thread(target=street_movement.movement, args=12)
    # thr_speed = threading.Thread(target=functions.speed_increase)
    thr_obstacle.start()
    thr_game.run()
# thr_street_movement.start()
# thr_speed.start()

# thr_street_movement = threading.Thread(target=street_movement.movement(functions.get_speed()), args=(1,))
# thr_speed = threading.Thread(target=functions.speed_increase(), args=(1,))


pygame.quit()
