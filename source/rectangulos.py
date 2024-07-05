from pygame import Rect


def obtener_rectangulos(principal: Rect):
    diccionario_rectangulo = {}
    
    rectangulo = principal
    
    diccionario_rectangulo["main"] = rectangulo
    diccionario_rectangulo["bottom"] = Rect(rectangulo.left, rectangulo.bottom - 5, rectangulo.width, 5)
    diccionario_rectangulo["right"] = Rect(rectangulo.right - 5, rectangulo.top, 5, rectangulo.height)
    diccionario_rectangulo["left"] = Rect(rectangulo.left, rectangulo.top, 5, rectangulo.height)
    diccionario_rectangulo["top"] = Rect(rectangulo.left, rectangulo.top  , rectangulo.width, 6)
    
    return diccionario_rectangulo

def limites_pantalla(pantalla):
    diccionario_pantalla = {}
    
    rectangulo_pantalla = pantalla.get_rect()
    
    diccionario_pantalla["main"] = rectangulo_pantalla
    diccionario_pantalla["bottom"] = Rect(rectangulo_pantalla.left, rectangulo_pantalla.bottom - 5, rectangulo_pantalla.width, 5)
    diccionario_pantalla["right"] = Rect(rectangulo_pantalla.right - 5, rectangulo_pantalla.top, 5, rectangulo_pantalla.height)
    diccionario_pantalla["left"] = Rect(rectangulo_pantalla.left, rectangulo_pantalla.top, 5, rectangulo_pantalla.height)
    diccionario_pantalla["top"] = Rect(rectangulo_pantalla.left, rectangulo_pantalla.top , rectangulo_pantalla.width, 5)
    
    return diccionario_pantalla
