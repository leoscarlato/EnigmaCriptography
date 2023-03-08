import numpy as np

def para_one_hot(mensagem):
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    contador = 0
    for caracter in mensagem:
        vetor = np.array([0 for i in range(27)])
        vetor[alfabeto.index(caracter)] = 1
        if contador == 0:
            anterior = vetor
        else:
            matrix = np.column_stack((anterior, vetor))
            anterior = matrix
        contador+=1
    if contador == 1:
        return anterior.reshape(27, 1)
    return anterior
        

def para_string(matrix):
    matrix_= matrix.T
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    palavra = ""
    for vetor in matrix_:
        idx = list(vetor).index(1)
        palavra += alfabeto[idx]
    return palavra



def cifrar(mensagem, matrix_permutacao):
    matrix = para_one_hot(mensagem)    
    matrix_encriptada = matrix_permutacao @ matrix
    mensagem_encriptada = para_string(matrix_encriptada)
    return mensagem_encriptada

def de_cifrar(mensagem_encriptada, matriz_permutacao):
    matriz_encriptada = para_one_hot(mensagem_encriptada)
    matriz = np.linalg.inv(matriz_permutacao) @ matriz_encriptada
    return para_string(matriz)

def enigma(mensagem, matriz_permutacao, matriz_auxiliar):
    mensagem_cripto = ""
    contador = 0
    for caracter in mensagem:
        letra_cripto = cifrar(caracter, matriz_permutacao)
        for i in range(contador):
            letra_cripto = cifrar(letra_cripto, matriz_auxiliar)
        mensagem_cripto += letra_cripto
        contador += 1
    return mensagem_cripto
    

def de_enigma(mensagem_encriptada, matriz_permutacao, matriz_auxiliar):
    mensagem_original = ""
    contador = 0
    for caracter in mensagem_encriptada:
        for i in range(contador):
            letra_original = de_cifrar(letra_original, matriz_auxiliar)
        letra_original = de_cifrar(caracter, matriz_permutacao)
        mensagem_original += letra_original
        contador += 1
    return mensagem_original










