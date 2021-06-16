# -*- coding: utf:8 -*-
import sys
from PIL import Image

# Checando os argumentos de linha de comando
if __name__ == "__main__":
    #print(f'Quantos argumentos: {len(sys.argv)}') 
    for i, arg in enumerate(sys.argv):
        if i == 1:
            entradaPrincipal = arg
        if i == 2:    
            saidaPrincipal = arg
        if (i == 3):
            teste = arg

# Abrindo os arquivos de entrada e saída 

entrada = open (sys.argv[1], "r+")
saida = open (sys.argv[2], "w+")

# Aplicando os filtros

original = Image.open(entradaPrincipal)
imgPng = original.convert('RGBA')

pixels = list(imgPng.getdata())

for i, p in enumerate(pixels):
    pixels[i] = (p[0], p[1], p[2], int(teste) * 3)

outputImg = Image.new('RGBA', original.size)
outputImg.putdata(pixels)

# Fechar os arquivos de entrada e de saída

entrada.close()
saida = outputImg.save(saidaPrincipal)