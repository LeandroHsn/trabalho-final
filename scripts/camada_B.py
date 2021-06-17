import sys
from PIL import Image

if __name__ == "__main__":
    print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

imgB = Image.open(sys.argv[1])

matrizB = imgB.load()

for i in range(imgB.size[0]):
    for j in range(imgB.size[1]):
        b = matrizB[i, j][0]
        matrizB[i,j] = (0, 0, b)

imgB.save(sys.argv[2])