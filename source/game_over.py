from settings import *
from imagenes import *
from colisiones import punto_en_rectangulo
from pygame.locals import *



def pantalla_fin(pantalla,botones, puntuacion_final):
    continuar = True
    
    pantalla.blit(fondo, (0, 0))
    
    fuente_puntuacion = pygame.font.SysFont(None, 48)
    texto_puntuacion = fuente_puntuacion.render(f"Puntuación final: {puntuacion_final}", True, (255, 255, 255))
    texto_puntuacion_rect = texto_puntuacion.get_rect(center= (WIDTH// 2, HEIGHT // 3))
    
    while continuar:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                for boton, rect in botones:
                    if punto_en_rectangulo(evento.pos, rect):
                        if boton == "start":
                            #reiniciar_juego()
                            continuar = False
                        elif boton == "exit":
                            pygame.quit()
                            exit()
        
        
        
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(texto_puntuacion, texto_puntuacion_rect)
        pantalla.blit(start_button, (button_x, start_button_y))  # Botón para volver a jugar
        pantalla.blit(exit_button, (button_x, exit_button_y))    # Botón para salir del juego
        
        pygame.display.flip()
    
    pygame.mixer.music.stop()