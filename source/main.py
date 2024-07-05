import pygame
from pygame.locals import *
from settings import *
from imagenes import *
from colisiones import *
from sys import exit
from rectangulos import *
from modo_debug import *



#PISO 800*60

#https://www.onlinegdb.com/lSg2Dbq1R

def salir_juego():
    pygame.quit()
    exit()



def pantalla_inicio(botones):
    continuar = True

    pygame.mixer.music.load("source\Recursos\musica\star_wars_soundtrack.wav")
    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.music.play(-1)
    reproduciendo_musica = True
    
    
    pantalla.blit(fondo,(0,0))
    pantalla.blit(music_button,(750,550))
    
    
    while continuar:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                salir_juego()
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                for boton, rect in botones:
                    if punto_en_rectangulo(evento.pos,rect):
                        if boton == "start":
                            continuar = False
                        elif boton == "exit":
                            salir_juego()
                        elif boton == "options":
                            print("MOSTRAR OPCIONES")
            if evento.type  == KEYDOWN:
                if evento.key == K_m:
                    if reproduciendo_musica:
                        pygame.mixer.music.set_volume(0)
                        pantalla.blit(muted_music,(750,550))
                    else:
                        pygame.mixer.music.set_volume(0.01)
                        pantalla.blit(music_button,(750,550))
                    reproduciendo_musica = not reproduciendo_musica



        pantalla.blit(start_button, (button_x,start_button_y))
        pantalla.blit(options_button, (button_x,options_button_y))
        pantalla.blit(exit_button, (button_x,exit_button_y))


        pygame.display.flip()

    pygame.mixer.music.stop()


def reiniciar_juego():
    global timer_nivel, texto_timer

    timer_nivel = timer_inicial  # Reinicia el timer al valor inicial
    texto_timer = f"Tiempo: {timer_nivel}"


def pantalla_fin(botones, puntuacion_final):
    continuar = True
    
    pantalla.blit(fondo, (0, 0))
    
    fuente_puntuacion = pygame.font.SysFont(None, 48)
    texto_puntuacion = fuente_puntuacion.render(f"Puntuación final: {puntuacion_final}", True, (255, 255, 255))
    texto_puntuacion_rect = texto_puntuacion.get_rect(center= (WIDTH// 2, HEIGHT // 3))
    
    while continuar:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                salir_juego()
            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                for boton, rect in botones:
                    if punto_en_rectangulo(evento.pos, rect):
                        if boton == "start":
                            reiniciar_juego()
                            continuar = False
                        elif boton == "exit":
                            salir_juego()
        
        
        
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(texto_puntuacion, texto_puntuacion_rect)
        pantalla.blit(start_button, (button_x, start_button_y))  # Botón para volver a jugar
        pantalla.blit(exit_button, (button_x, exit_button_y))    # Botón para salir del juego
        
        pygame.display.flip()
    
    pygame.mixer.music.stop()

def mover_personaje(rectangulo_pj,velocidad):
    rectangulo_pj.x += velocidad

def animar(animaciones,pantalla,rectangulo_pj):
    global contador_pasos
    largo_animaciones = len(animaciones)
    
    if contador_pasos >= largo_animaciones:
        contador_pasos = 0
    
    
    pantalla.blit(animaciones[contador_pasos],rectangulo_pj)
    contador_pasos += 1

def actualizar_pantalla(pantalla,que_hace,velocidad):
    pantalla.blit(mapa,(0,0))
    
    match que_hace:
        case 'corre_der':
            animar(personaje_corre,pantalla,hitbox_personaje)
            mover_personaje(hitbox_personaje,velocidad)
        case 'corre_izq':
            animar(personaje_corre_izq,pantalla, hitbox_personaje)
            mover_personaje(hitbox_personaje,velocidad * -1)
        case 'quieto_der':
            animar(personaje_idle,pantalla,hitbox_personaje)
        case 'quieto_izq':
            animar(personaje_idle_izq,pantalla,hitbox_personaje)






pygame.init()



#TEXTO
fuente_score = pygame.font.SysFont(None,32)
texto_score = fuente_score.render("Score: ",True, RED)
score = 0


# PISO
textura_piso = pygame.image.load("source\Recursos\piso_orueba3.png")
piso = textura_piso
piso = pygame.Rect(0,510,WIDTH,90)
lados_piso = obtener_rectangulos(piso)







#PATANLLA Y CLOCK FRAMES
pantalla = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Juego")
clock = pygame.time.Clock()





#TIEMPO
timer_inicial = 30
fuente_timer = pygame.font.SysFont(None, 32)
timer_nivel = timer_inicial
texto_timer = f"Tiempo: {timer_nivel}"
pygame.time.set_timer(pygame.USEREVENT, 1000)








#BOTONES INICIO Y FIN
botones_inicio = [("start", start_button_rect), ("options", options_button_rect), ("exit", exit_button_rect)]
botones_fin = [("start", start_button_rect), ("exit", exit_button_rect)]






pantalla_inicio(botones_inicio)
que_hace = 'quieto'


is_running = True
while is_running:
    clock.tick(FPS)
    
    
    #bliteos pantalla
    
    
    # pantalla.blit(fondo,(0,0))
    pantalla.blit(texto_score,(365,50))
    # pantalla.blit(textura_piso,(0,360))
    pantalla.blit(mapa,(0,0))
    
    
    
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            is_running = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
        if evento.type == pygame.USEREVENT:
            timer_nivel -= 1
            texto_timer = f"Tiempo: {timer_nivel}"
            if timer_nivel == 0:
                pantalla_fin(botones_fin,score)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()  
    
    
    
    keys = pygame.key.get_pressed()
    is_moving = False
    is_jumping = False
    
    #   MOVIMIENTO
    if keys[pygame.K_RIGHT] and hitbox_personaje["right"].x < rectangulos_pantalla["right"].right - velocidad_x:
        personaje_pos.x += velocidad_x
        direccion = 'derecha'
        is_moving = True
    elif keys[pygame.K_LEFT] and hitbox_personaje["left"].x > rectangulos_pantalla["left"].left + velocidad_x:
        personaje_pos.x -= velocidad_x
        direccion = 'izquierda'
        is_moving = True
    elif keys[pygame.K_SPACE]:
        is_jumping = True
    
    
    
    
    hitbox_personaje = obtener_rectangulos(personaje_pos)
    
    
    #ACA SE PARA MI PERSONAJE 
    hitbox_personaje["main"].bottom = lados_piso["top"].bottom
    
    rectangulos_pantalla = limites_pantalla(pantalla)
    
    
    
    
    # Actualización de la animació
    
    if is_moving:
        anim_counter += 1
        if anim_counter >= anim_correr_speed:
            anim_counter = 0
            anim_index = (anim_index + 1) % len(personaje_corre)
    else:
        anim_counter += 1
        if anim_counter >= anim_idle_speed:
            anim_counter = 0
            anim_index = (anim_index + 1) % len(personaje_idle)
    
    
    
    
    #ANIMACION IDLE Y CORRER
    if is_moving:
        if direccion == 'derecha':
            pantalla.blit(personaje_corre[anim_index], personaje_pos.topleft)
        else:
            pantalla.blit(personaje_corre_izq[anim_index], personaje_pos.topleft)
    else:
        if direccion == 'derecha':
            pantalla.blit(personaje_idle[anim_index], personaje_pos.topleft)
        else:
            pantalla.blit(personaje_idle_izq[anim_index], personaje_pos.topleft)
    
    if is_jumping:
        posicion_y -= desplazamiento_y
        desplazamiento_y -= gravedad
        if desplazamiento_y < -potencia_salto:
            is_jumping = False
            desplazamiento_y = potencia_salto
            pantalla.blit(personaje_salta[1],personaje_pos.topleft)
        else:
            pantalla.blit(personaje_idle[anim_index], personaje_pos.topleft)
    
    
    if get_modo():
        for lado in lados_piso:
            pygame.draw.rect(pantalla,"orange",lados_piso[lado],1)
        
        for lado in hitbox_personaje:
            pygame.draw.rect(pantalla, "red", hitbox_personaje[lado], 1)
        
        for lado in rectangulos_pantalla:
            pygame.draw.rect(pantalla,"blue",rectangulos_pantalla[lado],1)
    
    texto_timer_surface = fuente_timer.render(texto_timer, True, (255, 0, 0))
    
    pantalla.blit(texto_timer_surface, (670,10))
    
    pygame.display.flip()


salir_juego()

