import pygame
from settings import *
from rectangulos import obtener_rectangulos


class Personaje:
    def __init__(self,tamaño_rect:tuple, animaciones :dict,posicion_inicial : tuple,velocidad) -> None:
        
        #GRAVEDAD Y MOVIMIENTO
        self.gravedad = 0.5
        self.potencia_salto = 10
        self.limite_velocidad_caida = 1
        self.esta_saltando = False
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        
        #ANIMACIONES    
        self.contador_pasos = 0
        self.is_moving = False
        self.animaciones = animaciones
        self.donde_mira = 'derecha'
        self.anim_index = 0
        self.anim_correr_speed = 10
        self.anim_idle_speed = 15
        
        #RECTANGULO
        self.rectangulo = pygame.Rect(posicion_inicial[0],posicion_inicial[1],tamaño_rect[0],tamaño_rect[1])
        self.rectangulos_personaje = obtener_rectangulos(self.rectangulo)
        
        #DISPARO
    
    
    def animar(self, pantalla):
        if self.is_moving:
            self.contador_pasos += 1
            if self.contador_pasos >= self.anim_correr_speed:
                self.contador_pasos = 0
                self.anim_index = (self.anim_index + 1) % len(self.animaciones["corre_der"])
            if self.donde_mira == 'derecha':
                pantalla.blit(self.animaciones["corre_der"][self.anim_index], self.rectangulos_personaje["main"].topleft)
            else:
                pantalla.blit(self.animaciones["corre_izq"][self.anim_index], self.rectangulos_personaje["main"].topleft)
        else:
            self.contador_pasos += 1
            if self.contador_pasos >= self.anim_idle_speed:
                self.contador_pasos = 0
                self.anim_index = (self.anim_index + 1) % len(self.animaciones["quieto"])
            if self.donde_mira == 'derecha':
                pantalla.blit(self.animaciones["quieto"][self.anim_index], self.rectangulos_personaje["main"].topleft)
            else:
                pantalla.blit(self.animaciones["quieto_izq"][self.anim_index], self.rectangulos_personaje["main"].topleft)
                
    
    
    
    

