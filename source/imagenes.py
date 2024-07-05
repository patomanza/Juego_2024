from settings import *
import pygame

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    
    return lista_girada

def reescalar_imagen(lista_imagenes, tamaño):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i],tamaño)

fondo = pygame.image.load("source\Recursos\Back.png")
fondo = pygame.transform.scale(fondo,SCREEN_SIZE)

mapa = pygame.image.load("source\Recursos\map3.png")
mapa = pygame.transform.scale(mapa,SCREEN_SIZE)

start_button = pygame.image.load("source\Recursos\Botones\Start_Button.png")
rect_start_button = start_button.get_rect()

options_button = pygame.image.load("source\Recursos\Botones\Options_Button.png")
rect_options_button = options_button.get_rect()

exit_button = pygame.image.load("source\Recursos\Botones\Exit_Button.png")
rect_exit_button = exit_button.get_rect()

muted_music = pygame.image.load("source\Recursos\Botones\Music_mute.png")
music_button = pygame.image.load("source\Recursos\Botones\Music_Button.png")


barra_vida = [pygame.image.load("source\Recursos\GUI\Vida_2.png"),
              pygame.image.load("source\Recursos\GUI\Vida_3.png"),
              pygame.image.load("source\Recursos\GUI\Vida_4.png"),
              pygame.image.load("source\Recursos\GUI\Vida_5.png")]


personaje_idle = [pygame.image.load("source\Recursos\Personaje\idle_1.png"),
                  pygame.image.load("source\Recursos\Personaje\idle_2.png"),
                  pygame.image.load("source\Recursos\Personaje\idle_3.png"),
                  pygame.image.load("source\Recursos\Personaje\idle_4.png"),
                  pygame.image.load("source\Recursos\Personaje\idle_5.png"),
                  pygame.image.load("source\Recursos\Personaje\idle_6.png"),]

personaje_idle_izq = girar_imagenes(personaje_idle, True, False)

personaje_corre = [pygame.image.load("source\Recursos\Personaje\Run_1.png"),
                   pygame.image.load("source\Recursos\Personaje\Run_2.png"),
                   pygame.image.load("source\Recursos\Personaje\Run_3.png"),
                   pygame.image.load("source\Recursos\Personaje\Run_4.png"),
                   pygame.image.load("source\Recursos\Personaje\Run_5.png"),
                   pygame.image.load("source\Recursos\Personaje\Run_6.png"),]

personaje_corre_izq = girar_imagenes(personaje_corre,True,False)

personaje_salta = [pygame.image.load("source\Recursos\Personaje\jump_1.png"),
                   pygame.image.load("source\Recursos\Personaje\jump_2.png")]

personaje_salta_izq = girar_imagenes(personaje_salta,True,False)



dict_animaciones = {'quieto_der': personaje_idle,
                    'quieto_izq': personaje_idle_izq,
                    'corre_der': personaje_corre,
                    'corre_izq': personaje_corre_izq,
                    'salta_der': personaje_salta,
                    'salta_izq': personaje_salta_izq
                    }