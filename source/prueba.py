from PIL import Image

# Ruta de la imagen original
image_path = 'ruta/a/tu/imagen/Spike_8.png'

# Abrir la imagen original
original_image = Image.open(image_path)

# Obtener las dimensiones de la imagen original
width, height = original_image.size

# Crear una nueva imagen con el tamaño de tres veces el ancho de la imagen original
new_width = width * 3
new_image = Image.new('RGBA', (new_width, height))

# Pegar la imagen original tres veces en la nueva imagen
new_image.paste(original_image, (0, 0))
new_image.paste(original_image, (width, 0))
new_image.paste(original_image, (width * 2, 0))

# Guardar la nueva imagen
new_image_path = 'ruta/a/tu/imagen/Spike_8_triple.png'
new_image.save(new_image_path)

# Mostrar la nueva imagen
new_image.show()
