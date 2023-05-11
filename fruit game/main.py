import pygame
import sys
import os

width = 1366
height = 768

pygame.init()
screen = pygame.display.set_mode((width, height))
load_screen = pygame.image.load('images/load.png').convert()
Main = pygame.image.load('images/main.png').convert()


def loadingScreen(wait):
    loadCount = 0
    running = True
    screen.blit(load_screen, (0, 0))
    pygame.display.flip()
    while running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        loadCount += 1
        if loadCount >= wait:
            running = False
        pygame.display.flip()


class Button:
    def __init__(self, text, position, font_size=60):
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.position = position
        self.text_color = "#f5f5fd"  # Initial text color

    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.position)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.position)
        return text_rect.collidepoint(mouse_pos)

    def change_text_color(self, new_color):
        self.text_color = new_color


def Menu():
    screen.blit(Main, (0, 0))

    # Draw the menu interface
    start_button = Button("START", (width//2, height//2))
    start_button.draw(screen)

    # Main menu loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle mouse clicks
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.is_clicked(mouse_pos):
                    start_button.change_text_color("#FFD165")

                    # If the "START" button is clicked, start the game
                    start_button.draw(screen)
                    pygame.display.update()

                    game_path = "fruit_ninja.py"
                    os.system("python " + game_path)
                    running = False

        screen.blit(Main, (0, 0))
        start_button.draw(screen)
        # Update the game screen
        pygame.display.update()


# Main loop
load = True
main = True

if load:
    loadingScreen(1000)

if main:
    Menu()

# Quit the game
pygame.quit()
sys.exit()
