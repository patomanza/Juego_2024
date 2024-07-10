import pygame
from pygame.locals import *
from settings import WIDTH,HEIGHT,button_x,exit_button_y
from imagenes import fondo,exit_button
from colisiones import punto_en_rectangulo




def salir_juego():
    pygame.quit()
    exit()


def pantalla_fin(pantalla,botones, score):
    
    continuar = True
    
    pantalla.blit(fondo, (0, 0))
    
    fuente_puntuacion = pygame.font.SysFont(None, 48)
    texto_puntuacion = fuente_puntuacion.render(f"Puntuación final: {score}", True, (255, 255, 255))
    texto_puntuacion_rect = texto_puntuacion.get_rect(center= (WIDTH// 2, HEIGHT // 2))
    
    nombre = input('Ingrese su nickname')
    with open('Scores.txt','a') as file:
        file.write(f"{nombre} {score}\n")
    
    while continuar:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                salir_juego()
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                for boton, rect in botones:
                    if punto_en_rectangulo(evento.pos, rect):
                        if boton == "exit":
                            salir_juego()
        
        
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(texto_puntuacion, texto_puntuacion_rect)
        pantalla.blit(exit_button, (button_x, exit_button_y))
        
        pygame.display.flip()
    
    pygame.mixer.music.stop()