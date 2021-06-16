import sys
from PIL import Image, ImageFilter

if __name__ == "__main__":
    print(f'quanto argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i}: {arg}')

img = Image.open(sys.argv[1])

matriz = img.load()

img2 = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

img2.save(sys.argv[2])