# -*- coding: utf:8 -*-
import sys
from PIL import Image

# Checando os argumentos de linha de comando
if __name__ == "__main__":
    #print(f'Quantos argumentos: {len(sys.argv)}') 
    for i, arg in enumerate(sys.argv):
        if i == 1:
            entradaPrincipal = arg
        saidaPrincipal = arg
        #print(f"Argument {i}: {arg}")

# Abrindo os arquivos de entrada e saída 

entrada = open (sys.argv[1], "r+")
saida = open (sys.argv[2], "w+")

# Aplicando os filtros

original = Image.open(entradaPrincipal)
espelhar = original.transpose(Image.FLIP_LEFT_RIGHT)

# Fechar os arquivos de entrada e de saída

entrada.close()
saida = espelhar.save(saidaPrincipal)