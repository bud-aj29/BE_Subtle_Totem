from PIL import Image
import math

image = Image.open("totem.png")

width, height = image.size

right = math.ceil(width*0.5)
left = math.ceil(width*0.5)
top = math.ceil(height*0.75)
bottom = math.ceil(height*0.25)

new_width = width + right + left
new_height = height + top + bottom

result = Image.new(image.mode, (new_width, new_height), (255, 255, 255, 0))

result.paste(image, (left, top))

result.save('totem.png')
