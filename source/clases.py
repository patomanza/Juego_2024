import pygame
from pygame.locals import *
from rectangulos import obtener_rectangulos
from colisiones import detectar_colisiones
from imagenes import *



class Personaje:
    def __init__(self,posicion_inicial: tuple) -> None:
        self.posicion = pygame.Rect(posicion_inicial[0],posicion_inicial[1],35,45)
        self.hitbox_personaje = obtener_rectangulos(self.posicion)
        
        self.score = 0
        
        self.vidas = 3
        self.cooldown_colision_enemigo = 0
        self.anim_index = 0
        self.anim_idle_speed = 10  
        self.anim_correr_speed = 10
        self.anim_counter = 0
        
        self.anim_saltar_speed = 10
        self.anim_counter_salto = 0
        self.anim_index_salto = 0
        
        self.anim_counter_disparo = 0
        self.anim_disparo_speed = 20
        self.anim_index_disparo = 0
        
        self.velocidad_x = 2
        self.posicion_y = 470
        self.posicion_x = 50
        self.direccion = 'derecha'
        
        self.gravedad = 1
        self.potencia_salto = -15
        self.velocidad_caida = 15
        self.desplazamiento_y = 0
        self.is_jumping = False
        
        self.is_moving = False
        self.is_shooting = False
        self.colision_enemigo = False
        
        self.lista_balas = []
        self.puede_disparar = True
    
    
    def actualizar(self, keys, rectangulos_pantalla):
        self.is_moving = False
        self.is_shooting = False
        
        
        if keys[pygame.K_RIGHT] and self.hitbox_personaje["right"].x < rectangulos_pantalla["right"].right - self.velocidad_x:
            self.posicion.x += self.velocidad_x
            self.is_moving = True
            self.direccion = 'derecha'
        elif keys[pygame.K_LEFT] and self.hitbox_personaje["left"].x > rectangulos_pantalla["left"].left + self.velocidad_x:
            self.posicion.x -= self.velocidad_x
            self.is_moving = True
            self.direccion = 'izquierda'
        
        if keys[pygame.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.desplazamiento_y = self.potencia_salto
        if keys[pygame.K_p]:
            self.posicion = pygame.Rect(posicion_x,posicion_y,35,45)
        
        if keys[pygame.K_LCTRL] and self.puede_disparar:
            self.is_shooting = True
            self.disparar()
            self.puede_disparar = False
        
        
        self.hitbox_personaje = obtener_rectangulos(self.posicion)
        self.actualizar_balas()
    
    
    def disparar(self):
        if self.direccion == 'derecha':
            bala = Disparo(self.posicion.right, self.posicion.centery, 'derecha', balas)
        else:
            bala = Disparo(self.posicion.left, self.posicion.centery, 'izquierda', balas)
        self.lista_balas.append(bala)
    
    
    def actualizar_balas(self):
        for bala in self.lista_balas:
            bala.actualizar_balas()
            if bala.rect.x < 0 or bala.rect.x > 800: 
                self.lista_balas.remove(bala)
                self.puede_disparar = True
    
    
    def dibujar_balas(self, pantalla):
        for bala in self.lista_balas:
            bala.dibujar_bala(pantalla)
    
    
    def animar(self,pantalla):
        if self.is_shooting:
            self.anim_counter_disparo += 1
            if self.anim_counter_disparo >= self.anim_disparo_speed:
                self.anim_counter_disparo = 0
                self.anim_index_disparo = (self.anim_index_disparo + 1) % len(personaje_dispara)
            if self.direccion == 'derecha':
                pantalla.blit(personaje_dispara[2], self.posicion.topleft)
            else:
                pantalla.blit(personaje_dispara_izq[2], self.posicion.topleft)
        elif self.is_moving and not self.is_jumping:
            self.anim_counter += 1
            if self.anim_counter >= self.anim_correr_speed:
                self.anim_counter = 0
                self.anim_index = (self.anim_index + 1) % len(personaje_corre)
            if self.direccion == 'derecha':
                pantalla.blit(personaje_corre[self.anim_index], self.posicion.topleft)
            else:
                pantalla.blit(personaje_corre_izq[self.anim_index], self.posicion.topleft)
        elif self.is_jumping:
            self.anim_counter_salto += 1
            if self.anim_counter_salto >= self.anim_saltar_speed:
                self.anim_counter_salto = 0
                self.anim_index_salto = (self.anim_index_salto + 1) % len(personaje_salta)
            if self.direccion == 'derecha':
                pantalla.blit(personaje_salta[self.anim_index_salto], self.posicion.topleft)
            else:
                pantalla.blit(personaje_salta_izq[self.anim_index_salto], self.posicion.topleft)
        else:
            self.anim_counter += 1
            if self.anim_counter >= self.anim_idle_speed:
                self.anim_counter = 0
                self.anim_index = (self.anim_index + 1) % len(personaje_idle)
            if self.direccion == 'derecha':
                pantalla.blit(personaje_idle[self.anim_index], self.posicion.topleft)
            else:
                pantalla.blit(personaje_idle_izq[self.anim_index], self.posicion.topleft)
    
    
    def aplicar_gravedad(self, piso,lista_plataformas):
        
        if self.is_jumping:
            for lado in self.hitbox_personaje:
                self.hitbox_personaje[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        
        if detectar_colisiones(self.hitbox_personaje['main'], piso['top']):
            self.desplazamiento_y = 0
            self.gravedad = 1
            self.is_jumping = False
            self.hitbox_personaje['main'].bottom = piso['top'].bottom
        else:
            self.is_jumping = True
        
        self.detectar_colision_plataforma(lista_plataformas)
    
    
    def detectar_colision_plataforma(self, lista_plataformas):
        
        for plataforma in lista_plataformas:
            if detectar_colisiones(self.hitbox_personaje["bottom"],plataforma.hitbox_plataforma['top']):
                self.hitbox_personaje["main"].bottom = plataforma.hitbox_plataforma['top'].bottom
                self.esta_saltando = False
                if self.desplazamiento_y > 0:
                    self.desplazamiento_y = 0
                    self.esta_saltando = False
                    self.hitbox_personaje["main"].bottom = plataforma.hitbox_plataforma['top'].bottom
                self.is_jumping = False
    
    
    def actualizar_vida(self,pantalla):
        for lado in self.hitbox_personaje:
            if self.hitbox_personaje[lado].y > 600:
                self.vidas -= 1
                self.posicion = pygame.Rect(posicion_x,posicion_y,35,45)
                print(self.vidas)
        
        corazon_posiciones = [(10, 10), (50, 10), (90, 10)]
        for i in range(3):
            if i < self.vidas:
                pantalla.blit(corazon_full, corazon_posiciones[i])
            else:
                pantalla.blit(corazon_vacio, corazon_posiciones[i])
    
    
    # def detectar_colision_enemigo(self, lista_enemigos):
    #     for enemigo in lista_enemigos:
    #         if detectar_colisiones(self.hitbox_personaje['main'],enemigo.hitbox_enemigo['main']) and self.colision_enemigo == False:
    #             self.colision_enemigo = True
    #             self.vidas -= 1
    #         else:
    #             self.colision_enemigo = False
    #             print(self.vidas)
    def detectar_colision_enemigo(self, lista_enemigos):
        if self.cooldown_colision_enemigo > 0:
            self.cooldown_colision_enemigo -= 1
            return False  
        
        for enemigo in lista_enemigos:
            if detectar_colisiones(self.hitbox_personaje['main'],enemigo.hitbox_enemigo['main']):
                self.vidas -= 1
                self.cooldown_colision_enemigo = 120  
                self.score -= 100
                return True
        
        return False  
    
    def incrementar_score(self, puntos):
        self.score += puntos
    
    def restar_score(self, puntos):
        self.score -= puntos
    
    def dibujar_score(self, pantalla):
        font = pygame.font.Font(None, 36)
        texto_score = font.render(f"Puntuación: {self.score}", True, RED)
        pantalla.blit(texto_score, (320, 10))


class Disparo:
    def __init__(self, x, y, direccion, imagenes_bala):
        self.rect = pygame.Rect(x, y, 10, 5)   
        self.velocidad = 5
        self.direccion = direccion
        self.imagenes_bala = imagenes_bala
        self.anim_index = 0
        self.anim_speed = 20  
        self.anim_counter = 0
        
        

    def actualizar_balas(self):
        if self.direccion == 'derecha':
            self.rect.x += self.velocidad
        else:
            self.rect.x -= self.velocidad
        
        self.anim_counter += 1
        if self.anim_counter >= self.anim_speed:
            self.anim_counter = 0
            self.anim_index = (self.anim_index + 1) % len(self.imagenes_bala)

    def dibujar_bala(self, pantalla):
        pantalla.blit(self.imagenes_bala[self.anim_index], self.rect.topleft)



class Enemigo:
    def __init__(self,tamaño: tuple, posicion:tuple, tipo, imagenes_enemigo, limites_horizontales=(None, None), limites_verticales=(None, None)):
        self.posicion = pygame.Rect(posicion[0],posicion[1], tamaño[0],tamaño[1])  
        self.tipo = tipo  
        self.imagenes_enemigo = imagenes_enemigo 
        self.anim_index = 0
        self.anim_speed = 15  
        self.anim_counter = 0
        
        self.velocidad_x = 1  
        self.velocidad_y = 1
        self.direccion = 'derecha'  
        
        self.limites_horizontales = limites_horizontales
        self.limites_verticales = limites_verticales
        
        self.hitbox_enemigo = obtener_rectangulos(self.posicion)
    
    
    
    def actualizar(self):
        if self.tipo == 'caminante':
            self.mover_horizontalmente()
        elif self.tipo == "volador":
            self.mover_verticalmente()
        
        self.anim_counter += 1
        if self.anim_counter >= self.anim_speed:
            self.anim_counter = 0
            self.anim_index = (self.anim_index + 1) % len(self.imagenes_enemigo)
        
        self.hitbox_enemigo = obtener_rectangulos(self.posicion)
    
    
    def mover_horizontalmente(self):
        if self.direccion == 'derecha':
            self.posicion.x += self.velocidad_x
            if self.limites_horizontales[1] is not None and self.posicion.right >= self.limites_horizontales[1]:
                self.direccion = 'izquierda'
        else:
            self.posicion.x -= self.velocidad_x
            if self.limites_horizontales[0] is not None and self.posicion.left <= self.limites_horizontales[0]:
                self.direccion = 'derecha'
    
    def mover_verticalmente(self):
        if self.limites_verticales[0] is not None and self.posicion.top > self.limites_verticales[0]:
                self.posicion.y -= self.velocidad_y
        elif self.limites_verticales[1] is not None and self.posicion.bottom < self.limites_verticales[1]:
                self.posicion.y += self.velocidad_y
            
    
    
    def dibujar(self, pantalla):
        
        if self.direccion == 'derecha':
            pantalla.blit(self.imagenes_enemigo[self.anim_index], self.posicion.topleft)
        else:
            pantalla.blit(pygame.transform.flip(self.imagenes_enemigo[self.anim_index], True, False), self.posicion.topleft)




class Plataforma:
    def __init__(self,tamaño,posicion) -> None:
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        
        self.rectangulo_plataforma = pygame.Rect(posicion,tamaño)
        
        self.hitbox_plataforma = obtener_rectangulos(self.rectangulo_plataforma)
