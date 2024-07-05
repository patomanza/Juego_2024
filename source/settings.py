import pygame


WIDTH = 800
HEIGHT = 600
FPS = 60

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

personaje_pos = pygame.Rect(202,480,35,45)

is_moving = False
contador_pasos = 0
anim_index = 0
anim_idle_speed = 10  # Ajusta este valor para cambiar la velocidad de la animación (más alto es más lento)
anim_correr_speed = 5
anim_counter = 0
velocidad_x = 2

gravedad = 10
potencia_salto = 15
desplazamiento_y = potencia_salto

is_jumping = False


posicion_y = 480
posicion_x = 202

direccion = 'derecha'





button_width,button_height = 150,50
button_x = 325

start_button_y = 150
start_button_rect = pygame.Rect(button_x,start_button_y,button_width,button_height)

options_button_y = 250
options_button_rect = pygame.Rect(button_x,options_button_y,button_width,button_height)

exit_button_y = 350
exit_button_rect = pygame.Rect(button_x,exit_button_y,button_width,button_height)

