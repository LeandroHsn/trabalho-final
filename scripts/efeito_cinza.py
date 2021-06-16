import sys
from PIL import Image

if __name__ == "__main__":
    print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

img = Image.open(sys.argv[1])

matriz = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = matriz[i,j][0]
        g = matriz[i,j][1]
        b = matriz[i,j][2]
        pixel = int((r + g + b) / 3)
        matriz[i,j] = (pixel, pixel, pixel)

img.save(sys.argv[2])
