import pygame
import sys

def show_ranking(screen):
    clock = pygame.time.Clock()
    running = True

    # Leer los scores desde un archivo
    try:
        with open('scores.txt', 'r') as file:
            scores = [line.strip().split() for line in file.readlines()]
    except FileNotFoundError:
        scores = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((255, 255, 255))

        font = pygame.font.Font(None, 36)
        y_offset = 100
        for score in scores:
            score_text = font.render(f'{score[0]}: {score[1]}', True, (0, 0, 0))
            screen.blit(score_text, (100, y_offset))
            y_offset += 40

        pygame.display.flip()
        clock.tick(60)
