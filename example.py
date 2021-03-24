from imagelayers import LayeredImage
from PIL import Image


design = None

with Image.open('image.png') as f:
    img = LayeredImage(f)
    for layer in img.layersbycolor():
        layer.save('design.png')
        if input('y/n?').lower()[0] == 'y':
            layer.set_color(eval(input('color:')))
            if design is None:
                design = layer
            else:
                design = design + layer

design.save('design.png')
