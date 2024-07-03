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


