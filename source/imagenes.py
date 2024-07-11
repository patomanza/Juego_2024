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

fondo = pygame.image.load("source/Recursos/fondos/Back.png")
fondo = pygame.transform.scale(fondo,SCREEN_SIZE)

mapa = pygame.image.load("source/Recursos/fondos/MAPA.png")
mapa = pygame.transform.scale(mapa,SCREEN_SIZE)

start_button = pygame.image.load("source/Recursos/Botones/Start_Button.png")
rect_start_button = start_button.get_rect()

options_button = pygame.image.load("source/Recursos/Botones/Options_Button.png")
rect_options_button = options_button.get_rect()

exit_button = pygame.image.load("source/Recursos/Botones/Exit_Button.png")
rect_exit_button = exit_button.get_rect()

muted_music = pygame.image.load("source/Recursos/Botones/Music_mute.png")
music_button = pygame.image.load("source/Recursos/Botones/Music_Button.png")

corazon_full = pygame.image.load("source/Recursos/GUI/Heart_full.png")

corazon_extra = pygame.image.load("source/Recursos/GUI/corazon_extra.png")

corazon_vacio = pygame.image.load("source/Recursos/GUI/Heart_vacio.png")



barra_vida = [pygame.image.load("source/Recursos/GUI/Vida_2.png"),
              pygame.image.load("source/Recursos/GUI/Vida_3.png"),
              pygame.image.load("source/Recursos/GUI/Vida_4.png"),
              pygame.image.load("source/Recursos/GUI/Vida_5.png")]


personaje_idle = [pygame.image.load("source/Recursos/Personaje/idle/idle_1.png"),
                  pygame.image.load("source/Recursos/Personaje/idle/idle_2.png"),
                  pygame.image.load("source/Recursos/Personaje/idle/idle_3.png"),
                  pygame.image.load("source/Recursos/Personaje/idle/idle_4.png"),
                  pygame.image.load("source/Recursos/Personaje/idle/idle_5.png"),
                  pygame.image.load("source/Recursos/Personaje/idle/idle_6.png"),]

personaje_idle_izq = girar_imagenes(personaje_idle, True, False)

personaje_corre = [pygame.image.load("source/Recursos/Personaje/run/Run_1.png"),
                   pygame.image.load("source/Recursos/Personaje/run/Run_2.png"),
                   pygame.image.load("source/Recursos/Personaje/run/Run_3.png"),
                   pygame.image.load("source/Recursos/Personaje/run/Run_4.png"),
                   pygame.image.load("source/Recursos/Personaje/run/Run_5.png"),
                   pygame.image.load("source/Recursos/Personaje/run/Run_6.png"),]

personaje_corre_izq = girar_imagenes(personaje_corre,True,False)

personaje_salta = [pygame.image.load("source/Recursos/Personaje/jump/jump_1.png"),
                   pygame.image.load("source/Recursos/Personaje/jump/jump_2.png")]

personaje_salta_izq = girar_imagenes(personaje_salta,True,False)

personaje_dispara = [pygame.image.load("source/Recursos/Personaje/shoot/shoot_1.png"),
                     pygame.image.load("source/Recursos/Personaje/shoot/shoot_2.png"),
                     pygame.image.load("source/Recursos/Personaje/shoot/shoot_3.png")]

personaje_dispara_izq = girar_imagenes(personaje_dispara,True,False)

dict_animaciones = {'quieto_der': personaje_idle,
                    'quieto_izq': personaje_idle_izq,
                    'corre_der': personaje_corre,
                    'corre_izq': personaje_corre_izq,
                    'salta_der': personaje_salta,
                    'salta_izq': personaje_salta_izq,
                    'dispara_der': personaje_dispara,
                    'dispara_izq': personaje_dispara_izq
                    }


balas = [pygame.image.load("source/Recursos/Personaje/shoot/bullet_1.png"),
         pygame.image.load("source/Recursos/Personaje/shoot/bullet_2.png"),
         pygame.image.load("source/Recursos/Personaje/shoot/bullet_3.png"),
         pygame.image.load("source/Recursos/Personaje/shoot/bullet_4.png")]

explosion_bala = [pygame.image.load("source/Recursos/Personaje/shoot/explosion_bala_1.png"),
                  pygame.image.load("source/Recursos/Personaje/shoot/explosion_bala_2.png"),
                  pygame.image.load("source/Recursos/Personaje/shoot/explosion_bala_3.png"),
                  pygame.image.load("source/Recursos/Personaje/shoot/explosion_bala_4.png")]



esqueleto_camina_der = [pygame.image.load("source/Recursos/Enemigos/Eskeleton/Skeleton-Walk/skeleton_camina_1.png"),
                        pygame.image.load("source/Recursos/Enemigos/Eskeleton/Skeleton-Walk/skeleton_camina_2.png"),
                        pygame.image.load("source/Recursos/Enemigos/Eskeleton/Skeleton-Walk/skeleton_camina_3.png"),
                        pygame.image.load("source/Recursos/Enemigos/Eskeleton/Skeleton-Walk/skeleton_camina_4.png"),
                        pygame.image.load("source/Recursos/Enemigos/Eskeleton/Skeleton-Walk/skeleton_camina_5.png"),
                        pygame.image.load("source/Recursos/Enemigos/Eskeleton/Skeleton-Walk/skeleton_camina_6.png"),
                        pygame.image.load("source/Recursos/Enemigos/Eskeleton/Skeleton-Walk/skeleton_camina_7.png"),
                        pygame.image.load("source/Recursos/Enemigos/Eskeleton/Skeleton-Walk/skeleton_camina_8.png")]


ojo_volador = [pygame.image.load("source/Recursos/Enemigos/Fliying_eye/flying_eye_1.png"),
               pygame.image.load("source/Recursos/Enemigos/Fliying_eye/flying_eye_2.png"),
               pygame.image.load("source/Recursos/Enemigos/Fliying_eye/flying_eye_3.png"),
               pygame.image.load("source/Recursos/Enemigos/Fliying_eye/flying_eye_4.png")]

lizard_dispara = [pygame.image.load("source/Recursos/Enemigos/lizard shoots/lizard_shoot_1.png"),
                      pygame.image.load("source/Recursos/Enemigos/lizard shoots/lizard_shoot_2.png"),
                      pygame.image.load("source/Recursos/Enemigos/lizard shoots/lizard_shoot_2.png"),
                      pygame.image.load("source/Recursos/Enemigos/lizard shoots/lizard_shoot_2.png"),
                      pygame.image.load("source/Recursos/Enemigos/lizard shoots/lizard_shoot_3.png"),
                      pygame.image.load("source/Recursos/Enemigos/lizard shoots/lizard_shoot_4.png")]

lizard_fireball = [pygame.image.load("source/Recursos/Enemigos/Fireball/fireball_1.png"),
                   pygame.image.load("source/Recursos/Enemigos/Fireball/fireball_2.png"),
                   pygame.image.load("source/Recursos/Enemigos/Fireball/fireball_3.png"),
                   pygame.image.load("source/Recursos/Enemigos/Fireball/fireball_4.png")]

fireball_explota = [pygame.image.load("source/Recursos/Enemigos/Fireball/explosion_fireball_1.png"),
                    pygame.image.load("source/Recursos/Enemigos/Fireball/explosion_fireball_2.png"),
                    pygame.image.load("source/Recursos/Enemigos/Fireball/explosion_fireball_3.png"),
                    pygame.image.load("source/Recursos/Enemigos/Fireball/explosion_fireball_4.png")]



spikes = [pygame.image.load("source/Recursos/Trampas/Spikes/spike_1.png"),
          pygame.image.load("source/Recursos/Trampas/Spikes/spike_2.png"),
          pygame.image.load("source/Recursos/Trampas/Spikes/spike_3.png"),
          pygame.image.load("source/Recursos/Trampas/Spikes/spike_4.png"),
          pygame.image.load("source/Recursos/Trampas/Spikes/spike_5.png"),
          pygame.image.load("source/Recursos/Trampas/Spikes/spike_6.png"),
          pygame.image.load("source/Recursos/Trampas/Spikes/spike_7.png"),
          pygame.image.load("source/Recursos/Trampas/Spikes/spike_8.png")]








