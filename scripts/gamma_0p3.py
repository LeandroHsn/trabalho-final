import sys
from PIL import Image

if __name__ == "__main__":
    #print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

img = Image.open(sys.argv[1])

matriz = img.load()

gamma = 0.3
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int((matriz[i, j][0] / 255) ** gamma * 255)
        g = int((matriz[i, j][1] / 255) ** gamma * 255)
        b = int((matriz[i, j][2] / 255) ** gamma * 255)
        matriz[i, j] = (r, g, b)

img.save(sys.argv[2])