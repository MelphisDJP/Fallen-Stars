import qrcode
from qrcode.main import QRCode
from PIL import Image
import qrcode.image.svg as svg

# URL que se va a convertir en un código QR
input_data = [
    'https://www.instagram.com/contecsolutions/',
    'https://www.instagram.com/contecsolutions/'
]

# Crear un objeto QRCode con parámetros especificados
qr = QRCode(version=1, box_size=10, border=5)

# Iterar sobre la lista de URLs y generar los códigos QR
for i, data in enumerate(input_data):
    # Crear un nuevo objeto QRCode para cada URL
    qr = QRCode(version=1, box_size=10, border=5)

    # Agregar datos al código QR
    qr.add_data(data)
    qr.make(fit=True)

    # Crear la imagen en PNG con fondo transparente
    img = qr.make_image(fill='black', back_color='white').convert('RGBA')

    # Asegurarse de que el fondo sea transparente
    img = img.convert('RGBA')
    data = img.getdata()

    new_data = []
    for item in data:
        # Cambiar todo lo blanco (o tonos de blanco) a transparente
        if item[:3] == (255, 255, 255):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)

    # Guardar la imagen en formato PNG
    img.save(f'qr_instagram{i}.png')

    # Crear la imagen en formato SVG
    svg_factory = svg.SvgImage
    img_svg = qrcode.make(data, image_factory=svg_factory)

    # Guardar la imagen en formato SVG
    with open(f'qr_instagram{i}.svg', 'wb') as svg_file:
        img_svg.save(svg_file)

