import pygame
import sys
from game import game_loop
from config import config_menu
from ranking import show_ranking
from game_over import game_over_screen

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Game')

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Fuente
font = pygame.font.Font(None, 74)

def main_menu():
    while True:
        screen.fill(BLUE)

        title = font.render('Space Game', True, (0, 0, 0))
        play_button = font.render('Play', True, (0, 0, 0))
        config_button = font.render('Config', True, (0, 0, 0))
        ranking_button = font.render('Ranking', True, (0, 0, 0))

        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        screen.blit(play_button, (SCREEN_WIDTH // 2 - play_button.get_width() // 2, 250))
        screen.blit(config_button, (SCREEN_WIDTH // 2 - config_button.get_width() // 2, 350))
        screen.blit(ranking_button, (SCREEN_WIDTH // 2 - ranking_button.get_width() // 2, 450))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 250 < event.pos[1] < 250 + play_button.get_height():
                    game_loop(screen)
                elif 350 < event.pos[1] < 350 + config_button.get_height():
                    config_menu(screen)
                elif 450 < event.pos[1] < 450 + ranking_button.get_height():
                    show_ranking(screen)

if __name__ == '__main__':
    main_menu()
