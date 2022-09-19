import pygame
import functions
import game
from functions import scale_image, get_font
from game import STREET_WIDTH, STREET_HEIGHT
import sys
from button import Button


def play():
    color = "RED"
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BACK = Button(image=None, pos=(150, 900),
                           text_input="BACK", font=functions.get_font(75), base_color="Black", hovering_color="Green")
        GO_BUTTON = Button(image=None, pos=(int(STREET_WIDTH) - 100, 900),
                           text_input="GO", font=functions.get_font(75), base_color="Black", hovering_color="Green")
        RED_BUTTON = Button(image=RED, pos=(int(STREET_WIDTH) / 4 * 1, 500),
                            text_input="", font=functions.get_font(75), base_color="Black", hovering_color="GREY")
        BLUE_BUTTON = Button(image=BLUE, pos=(int(STREET_WIDTH) / 4 * 2, 500),
                             text_input="", font=functions.get_font(75), base_color="Black", hovering_color="GREY")
        GREEN_BUTTON = Button(image=GREEN, pos=(int(STREET_WIDTH) / 4 * 3, 500),
                              text_input="", font=functions.get_font(75), base_color="Black", hovering_color="GREY")

        CAR_TEXT = functions.get_font(45).render("Choose a Car!", True, "BLACK")
        PLAY_RECT = CAR_TEXT.get_rect(center=(int(STREET_WIDTH) / 2, 100))
        # GREEN_CAR_RECT = GREEN_BUTTON.text_input.get_rect(center=(int(WIDTH) / 4 * 3, 500))
        # RED_CAR_RECT = RED_BUTTON.text_input.get_rect(center=(int(WIDTH) / 4 * 1, 500))
        # BLUE_CAR_RECT = BLUE_BUTTON.text_input.get_rect(center=(int(WIDTH) / 4 * 2, 500))
        SCREEN.blit(CAR_TEXT, PLAY_RECT)

        BLUE_BUTTON.changeColor(PLAY_MOUSE_POS)
        BLUE_BUTTON.update(SCREEN)
        GREEN_BUTTON.changeColor(PLAY_MOUSE_POS)
        GREEN_BUTTON.update(SCREEN)
        RED_BUTTON.changeColor(PLAY_MOUSE_POS)
        RED_BUTTON.update(SCREEN)
        GO_BUTTON.changeColor(PLAY_MOUSE_POS)
        GO_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if RED_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    color = "RED"
                    print("RED")
                    # SCREEN.blit(CAR_RECT, (int(WIDTH) / 4 * 1, 500))
                if BLUE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    color = "BLUE"
                    print("BLUE")
                    # SCREEN.blit(CAR_RECT, (int(WIDTH) / 4 * 3, 500))
                if GREEN_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    color = "GREEN"
                    print("GREEN")
                    # SCREEN.blit(CAR_RECT, (int(WIDTH) / 4 * 2, 500))
                if GO_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    game.start_game(color)

        pygame.display.update()


def scoreboard():
    score_pos = 700
    SCREEN.blit(BG, (0, 0))
    font_size = 40
    scoreboard_number = 5

    for x in scores:
        SCOREBOARD_NUMBER = get_font(font_size).render(str(scoreboard_number), True, "#96453e")
        SCOREBOARD_NUMBER.get_rect(center=(int(STREET_WIDTH) - 100 / 2, 150))
        SCREEN.blit(SCOREBOARD_NUMBER, (STREET_WIDTH / 2 - 150, score_pos))
        SCOREBOARD_TEXT = get_font(font_size).render(x, True, "#96453e")
        SCOREBOARD_TEXT.get_rect(center=(int(STREET_WIDTH)-100 / 2, 150))
        SCREEN.blit(SCOREBOARD_TEXT, (STREET_WIDTH/2-100, score_pos))
        print(score_pos)
        score_pos -= 100
        font_size +=10
        scoreboard_number -=1

    while True:
        SCORE_MOUSE_POS = pygame.mouse.get_pos()

        SCORE_TEXT = get_font(font_size).render("The Hall of Fame!", True, "white")

        SCORE_RECT = SCORE_TEXT.get_rect(center=(int(STREET_WIDTH) / 2, 60))
        SCREEN.blit(SCORE_TEXT, SCORE_RECT)

        SCORE_BACK = Button(image=None, pos=(150, 900),
                            text_input="BACK", font=functions.get_font(75), base_color="white", hovering_color="black")

        SCORE_BACK.changeColor(SCORE_MOUSE_POS)
        SCORE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SCORE_BACK.checkForInput(SCORE_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        score_test = True
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = functions.get_font(100).render("MAIN MENU", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(int(STREET_WIDTH) / 2, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("../resources/Play Rect.png"),
                             pos=(int(STREET_WIDTH) / 2, 350),
                             text_input="PLAY", font=functions.get_font(75), base_color="#96453e",
                             hovering_color="White")
        SCORE_BUTTON = Button(image=pygame.image.load("../resources/Options Rect.png"),
                              pos=(int(STREET_WIDTH) / 2, 500),
                              text_input="SCOREBOARD", font=functions.get_font(75), base_color="#96453e",
                              hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../resources/Quit Rect.png"),
                             pos=(int(STREET_WIDTH) / 2, 650),
                             text_input="QUIT", font=functions.get_font(75), base_color="#96453e",
                             hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, SCORE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if SCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    scoreboard()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()

    SCREEN = pygame.display.set_mode((STREET_WIDTH, STREET_HEIGHT))
    RED = scale_image(pygame.image.load("../resources/Car_red.png"), 4.0)
    GREEN = scale_image(pygame.image.load("../resources/Car_green.png"), 4.0)
    BLUE = scale_image(pygame.image.load("../resources/Car_blue.png"), 4.0)
    CAR_RECT = pygame.image.load("../resources/Play Rect.png")
    YASSIN = pygame.image.load("../resources/Yassin.jpeg")
    pygame.display.set_icon(YASSIN)
    pygame.display.set_caption("Menu")
    BG = pygame.image.load("../resources/sand.jpg")
    scores = ["Eric 700", "Yassin 800", "Tim 1000", "Mike 1050", "EricTest 1200"]

    main_menu()
