def punto_en_rectangulo(punto, rect):
    x, y = punto
    return rect.left <= x <= rect.right and rect.top <= y <= rect.bottom


def detectar_colisiones(rec_1,rec_2):
    if (punto_en_rectangulo(rec_1.topleft, rec_2) or
        punto_en_rectangulo(rec_1.topright, rec_2) or
        punto_en_rectangulo(rec_1.bottomright, rec_2) or
        punto_en_rectangulo(rec_1.bottomleft, rec_2)):
        return True
    
    if (punto_en_rectangulo(rec_2.topleft, rec_1) or
        punto_en_rectangulo(rec_2.topright, rec_1) or
        punto_en_rectangulo(rec_2.bottomright, rec_1) or
        punto_en_rectangulo(rec_2.bottomleft, rec_1)):
        return True
    
    return False