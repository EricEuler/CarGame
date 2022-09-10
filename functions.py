import pygame
import time

global speed


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("D:/PyCharm-Projects/CarGame/Small Print.ttf", size)


def speed_increase():
    time.sleep(2)
    speed += 3


def get_speed():
    return speed
