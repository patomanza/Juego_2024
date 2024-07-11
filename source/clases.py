import pygame
from pygame.locals import *
from rectangulos import obtener_rectangulos
from colisiones import detectar_colisiones
from imagenes import *
import time



class Personaje:
    def __init__(self,posicion_inicial: tuple) -> None:
        self.posicion = pygame.Rect(posicion_inicial[0],posicion_inicial[1],35,45)
        self.hitbox_personaje = obtener_rectangulos(self.posicion)
        
        self.score = 0
        
        self.vidas = 3
        self.vidas_maximas = 4
        self.corazon_extra = False
        
        
        self.cooldown_colision_enemigo = 0
        self.anim_index = 0
        self.anim_idle_speed = 10  
        self.anim_correr_speed = 10
        self.anim_counter = 0
        
        self.anim_saltar_speed = 10
        self.anim_counter_salto = 0
        self.anim_index_salto = 0
        
        self.anim_counter_disparo = 0
        self.anim_disparo_speed = 30
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
        self.sonido_disparo = pygame.mixer.Sound("source/Recursos/musica/zap_shot_1.wav")
        self.sonido_explosion_disparo = pygame.mixer.Sound("source/Recursos/musica/explosion_bala.wav")
    
    
    def actualizar(self, keys, rectangulos_pantalla,lista_enemigos,lista_plataformas):
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
            self.disparar()
            self.is_shooting = True
            self.puede_disparar = False
        
        
        self.hitbox_personaje = obtener_rectangulos(self.posicion)
        self.actualizar_balas(lista_enemigos,lista_plataformas)
    
    
    def disparar(self):
        if self.direccion == 'derecha':
            bala = Disparo(self.posicion.right, self.posicion.centery, 'derecha', balas,explosion_bala)
        else:
            bala = Disparo(self.posicion.left, self.posicion.centery, 'izquierda', balas,explosion_bala)
        self.lista_balas.append(bala)
        
        self.sonido_disparo.set_volume(0.1)
        self.sonido_disparo.play()
    
    
    def actualizar_balas(self,lista_enemigos,lista_plataformas):
        for bala in self.lista_balas:
                if bala.actualizar_balas():
                    self.lista_balas.remove(bala)
                    self.puede_disparar = True
                    continue
                
                for enemigo in lista_enemigos:
                    if detectar_colisiones(bala.rect, enemigo.hitbox_enemigo['main']):
                        lista_enemigos.remove(enemigo)
                        bala.explota = True
                        self.incrementar_score(500)
                        
                        self.sonido_explosion_disparo.set_volume(0.05)
                        self.sonido_explosion_disparo.play()
                        break
                
                for plataforma in lista_plataformas:
                    if detectar_colisiones(bala.rect, plataforma.hitbox_plataforma['main']):
                        if not bala.explota:  
                            bala.explota = True  
                            self.sonido_explosion_disparo.set_volume(0.05)
                            self.sonido_explosion_disparo.play()
                
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
                pantalla.blit(personaje_dispara[self.anim_index_disparo], self.posicion.topleft)
            else:
                pantalla.blit(personaje_dispara_izq[self.anim_index_disparo], self.posicion.topleft)
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
                self.is_jumping = False
                if self.desplazamiento_y > 0:
                    self.desplazamiento_y = 0
                    self.is_jumping = False
                    self.hitbox_personaje["bottom"].bottom = plataforma.hitbox_plataforma['top'].bottom
                self.is_jumping = False
    
    
    
    def actualizar_vida(self,pantalla):
        for lado in self.hitbox_personaje:
            if self.hitbox_personaje[lado].y > 600:
                self.vidas -= 1
                self.posicion = pygame.Rect(posicion_x,posicion_y,35,45)
                self.restar_score(100)
        
        corazon_posiciones = [(10, 10), (50, 10), (90, 10),(130,10)]
        
        for i in range(self.vidas_maximas):
            if i < self.vidas:
                pantalla.blit(corazon_full, corazon_posiciones[i])
            else:
                pantalla.blit(corazon_vacio, corazon_posiciones[i])
    
    
    def recoger_corazon_extra(self):
        if not self.corazon_extra:
            self.corazon_extra = True
            self.vidas += 1
    
    
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
    def __init__(self, x, y, direccion, imagenes_bala,imagenes_explosion):
        self.rect = pygame.Rect(x, y, 10, 5)   
        self.velocidad = 5
        self.direccion = direccion
        self.imagenes_bala = imagenes_bala
        self.anim_index = 0
        self.anim_speed = 15  
        self.anim_counter = 0
        self.explota = False
        self.imagenes_explosion = imagenes_explosion
        

    def actualizar_balas(self):
        if not self.explota:
            if self.direccion == 'derecha':
                self.rect.x += self.velocidad
            else:
                self.rect.x -= self.velocidad
        
        self.anim_counter += 1
        if self.anim_counter >= self.anim_speed:
            self.anim_counter = 0
            if not self.explota:
                self.anim_index = (self.anim_index + 1) % len(self.imagenes_bala)
            else:
                self.anim_index += 1
                if self.anim_index >= len(self.imagenes_explosion):
                    return True
        
        return False

    def dibujar_bala(self, pantalla):
        if not self.explota:
            pantalla.blit(self.imagenes_bala[self.anim_index], self.rect.topleft)
        elif self.anim_index < len(self.imagenes_explosion):
            pantalla.blit(self.imagenes_explosion[self.anim_index], self.rect.topleft)


class Enemigo:
    def __init__(self,tamaño: tuple, posicion:tuple, tipo, imagenes_enemigo, limites_horizontales=(None, None), limites_verticales=(None, None)
                , puede_disparar=False, imagenes_bala=None, imagenes_explosion=None):
        self.posicion = pygame.Rect(posicion[0],posicion[1], tamaño[0],tamaño[1])  
        self.tipo = tipo  
        self.imagenes_enemigo = imagenes_enemigo 
        self.anim_index = 0
        self.anim_speed = 15  
        self.anim_counter = 0
        
        self.velocidad_x = 1  
        self.velocidad_y = 1
        self.direccion = 'derecha'  
        self.direccion_y = 'arriba'
        self.limites_horizontales = limites_horizontales
        self.limites_verticales = limites_verticales
        
        
        self.imagenes_bala = imagenes_bala
        self.imagenes_explosion = imagenes_explosion
        self.lista_balas = []
        self.puede_disparar = puede_disparar
        
        self.sonido_explosion_disparo = pygame.mixer.Sound("source/Recursos/musica/explosion_bala.wav")
        
        self.hitbox_enemigo = obtener_rectangulos(self.posicion)
    
    
    def actualizar(self,lista_plataformas,personaje):
        if self.tipo == 'caminante':
            self.mover_horizontalmente()
        elif self.tipo == "volador":
            self.mover_verticalmente()
        
        self.anim_counter += 1
        if self.anim_counter >= self.anim_speed:
            self.anim_counter = 0
            self.anim_index = (self.anim_index + 1) % len(self.imagenes_enemigo)
        
        
        if self.puede_disparar:
            self.actualizar_bala(lista_plataformas,personaje)
        
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
        if self.direccion_y == 'arriba':
            if self.limites_verticales[0] is not None and self.posicion.top > self.limites_verticales[0]:
                self.posicion.y -= self.velocidad_y
            else:
                self.direccion_y = 'abajo'
        elif self.direccion_y == 'abajo':
            if self.limites_verticales[1] is not None and self.posicion.bottom < self.limites_verticales[1]:
                self.posicion.y += self.velocidad_y
            else:
                self.direccion_y = 'arriba'
    
    
    def dibujar(self, pantalla):
        if self.direccion == 'derecha':
            pantalla.blit(self.imagenes_enemigo[self.anim_index], self.posicion.topleft)
        else:
            pantalla.blit(pygame.transform.flip(self.imagenes_enemigo[self.anim_index], True, False), self.posicion.topleft)
    
    
    def disparar(self):
        if self.puede_disparar and self.direccion == 'derecha':
            bala = Disparo(self.posicion.right, self.posicion.centery, 'derecha', self.imagenes_bala,self.imagenes_explosion)
        else:
            bala = Disparo(self.posicion.left, self.posicion.centery, 'izquierda', self.imagenes_bala,self.imagenes_explosion)
        self.lista_balas.append(bala)
    
    def actualizar_bala(self,lista_plataformas,personaje):
        for bala in self.lista_balas:
            if bala.actualizar_balas():
                self.lista_balas.remove(bala)
                self.disparar()
                continue
            
            if detectar_colisiones(bala.rect, personaje.hitbox_enemigo['main']):
                if not bala.explota:
                    bala.explota = True
                    personaje.restar_score(100)
                    self.sonido_explosion_disparo.set_volume(0.05)
                    self.sonido_explosion_disparo.play()
                    self.disparar()
                    
            
            for plataforma in lista_plataformas:
                if detectar_colisiones(bala.rect, plataforma.hitbox_plataforma['main']):
                    if not bala.explota:  
                        bala.explota = True  
                        self.sonido_explosion_disparo.set_volume(0.05)
                        self.sonido_explosion_disparo.play()
                        self.disparar()
            
            if bala.rect.x < 0 or bala.rect.x > 800:
                self.lista_balas.remove(bala)
                self.disparar()
                self.puede_disparar = True
    
    def dibujar_bala(self,pantalla):
        for bala in self.lista_balas:
            bala.dibujar_bala(pantalla)
    
    


class Plataforma:
    def __init__(self,tamaño,posicion) -> None:
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        
        self.rectangulo_plataforma = pygame.Rect(posicion,tamaño)
        
        self.hitbox_plataforma = obtener_rectangulos(self.rectangulo_plataforma)


class Trampa:
    def __init__(self, tamaño: tuple, posicion: tuple, imagenes_trampa):
        self.rect_trampa = pygame.Rect(posicion[0], posicion[1], tamaño[0], tamaño[1])
        self.imagenes_trampa = imagenes_trampa
        self.anim_index = 0
        self.anim_speed = 15
        self.anim_counter = 0
        self.activa = True
        self.cooldown = False
        self.cooldown_time = 1  
        self.last_anim_time = 0
        self.cooldown_colision_trampa = 0
    
    
    def actualizar(self):
        if not self.cooldown:
            self.anim_counter += 1
            if self.anim_counter >= self.anim_speed:
                self.anim_counter = 0
                self.anim_index += 1
                if self.anim_index >= len(self.imagenes_trampa):
                    self.anim_index = 0  
                    self.cooldown = True
                    self.last_anim_time = time.time()  
        else:
            if time.time() - self.last_anim_time >= self.cooldown_time:
                self.anim_index = 0  
                self.cooldown = False
    
    
    def dibujar(self, pantalla):
        pantalla.blit(self.imagenes_trampa[self.anim_index], self.rect_trampa.topleft)
    
    
    def detectar_colision(self, personaje):
        if self.cooldown_colision_trampa > 0:
            self.cooldown_colision_trampa -= 1
            return False  
        
        if 2 <= self.anim_index <= 7:
            self.activa = True
            if self.activa and detectar_colisiones(personaje.hitbox_personaje['main'], self.rect_trampa):
                personaje.vidas -= 1
                self.activa = False
                self.cooldown_colision_trampa = 120  
        else:
            self.activa = False
        
        return self.activa


class PowerUp:
    def __init__(self, tamaño: tuple, posicion: tuple, tipo: str, imagen_powerup=None, imagenes_powerup_animadas=None):
        self.rect_powerup = pygame.Rect(posicion[0], posicion[1], tamaño[0], tamaño[1])
        self.tipo = tipo
        self.imagen_powerup = imagen_powerup
        self.imagenes_powerup_animadas = imagenes_powerup_animadas
        self.anim_index = 0
        self.anim_speed = 15
        self.anim_counter = 0
        self.activo = True
        self.aumento_vel_y_salto = False
    
    
    
    def actualizar(self):
        if self.imagenes_powerup_animadas:
            self.anim_counter += 1
            if self.anim_counter >= self.anim_speed:
                self.anim_counter = 0
                self.anim_index = (self.anim_index + 1) % len(self.imagenes_powerup_animadas)
    
    
    def dibujar(self, pantalla):
        if self.imagenes_powerup_animadas:
            pantalla.blit(self.imagenes_powerup_animadas[self.anim_index], self.rect_powerup.topleft)
        elif self.imagen_powerup:
            pantalla.blit(self.imagen_powerup, self.rect_powerup.topleft)
    
    
    def aplicar_efecto(self, personaje):
        if self.tipo == "vida_extra":
            personaje.recoger_corazon_extra()
            self.activo = False
        elif self.tipo == "aumento_vel_y_salto":
            self.aumento_vel_y_salto = True
            personaje.velocidad_x += 1
            personaje.potencia_salto -= 1
            personaje.velocidad_caida += 1
            self.activo = False
    
    
    def detectar_colision(self, personaje,lista_powerups):
            if self.activo and detectar_colisiones(personaje.hitbox_personaje['main'], self.rect_powerup):
                self.aplicar_efecto(personaje)
                self.activo = False
                lista_powerups.remove(self)
            else:
                self.activo = True