import pygame
import sys

def game_loop(screen):
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                running = False
        

        # Lógica del juego aquí

        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)

    # Llamar a la pantalla de game over
    from game_over import game_over_screen
    game_over_screen(screen, 100)