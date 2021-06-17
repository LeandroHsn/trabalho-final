import sys
from PIL import Image

if __name__ == "__main__":
    print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

imgG = Image.open(sys.argv[1])

matrizG = imgG.load()

for i in range(imgG.size[0]):
    for j in range(imgG.size[1]):
        g = matrizG[i, j][1]
        matrizG[i,j] = (0, g, 0)

imgG.save(sys.argv[2])