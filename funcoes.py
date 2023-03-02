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
    print(matriz_permutacao.shape,matriz_encriptada.shape)
    print(np.linalg.inv(matriz_permutacao).shape)
    matriz = np.linalg.inv(matriz_permutacao) @ matriz_encriptada
    
    return para_string(matriz)

def enigma():
    pass

def de_enigma():
    pass




