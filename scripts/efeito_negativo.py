import sys
from PIL import Image

if __name__ == "__main__":
    print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

img = Image.open(sys.argv[1])


#Adicionando a imagem na matriz
matriz = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = 255 - matriz[i, j][0]
        g = 255 - matriz[i, j][1]
        b = 255 - matriz[i, j][2]
        matriz[i, j] = (r, g, b)

img.save(sys.argv[2])