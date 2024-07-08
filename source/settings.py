import pygame


WIDTH = 800
HEIGHT = 600
FPS = 45

SCREEN_SIZE = (WIDTH,HEIGHT)
SCREEN_CENTER = (WIDTH //2,HEIGHT//2)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
CUSTOM = (220,100,255)


contador_pasos = 0
anim_index = 0
anim_idle_speed = 10  
anim_correr_speed = 10
anim_saltar_speed = 15
anim_counter = 0

velocidad_x = 2
posicion_y = 480
posicion_x = 50
direccion = 'derecha'

gravedad = 0.5
potencia_salto = -15
velocidad_caida = 15
desplazamiento_y = 0
is_jumping = False

personaje_pos = pygame.Rect(posicion_x,posicion_y,35,45)



button_width,button_height = 150,50
button_x = 325

start_button_y = 150
start_button_rect = pygame.Rect(button_x,start_button_y,button_width,button_height)

options_button_y = 250
options_button_rect = pygame.Rect(button_x,options_button_y,button_width,button_height)

exit_button_y = 350
exit_button_rect = pygame.Rect(button_x,exit_button_y,button_width,button_height)

botones_inicio = [("start", start_button_rect), ("options", options_button_rect), ("exit", exit_button_rect)]
botones_fin = [("start", start_button_rect), ("exit", exit_button_rect)]