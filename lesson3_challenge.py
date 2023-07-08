from PIL import Image

img = Image.new('RGB', (128, 128), color='Blue')
img.save('test.png')
