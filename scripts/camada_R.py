import sys
from PIL import Image

if __name__ == "__main__":
    print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

imgR = Image.open(sys.argv[1])

matrizR = imgR.load()

for i in range(imgR.size[0]):
    for j in range(imgR.size[1]):
        r = matrizR[i, j][0]
        matrizR[i,j] = (r, 0, 0)

imgR.save(sys.argv[2])