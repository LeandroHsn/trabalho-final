import sys
from PIL import Image, ImageFilter

if __name__ == "__main__":
    #print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

img1 = Image.open(sys.argv[1])

kern = ImageFilter.Kernel((3,3), (0, 1, 0, 1, -4, 1, 0, 1, 0), 1, 0 )

img2 = img1.filter(kern)

img2.save(sys.argv[2])