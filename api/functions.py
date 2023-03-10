import numpy as np
import numpy as np

def to_one_hot(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    counter = 0
    for char in message:
        vector = np.array([0 for i in range(27)])
        vector[alphabet.index(char)] = 1
        if counter == 0:
            previous_vector = vector
        else:
            matrix = np.column_stack((previous_vector, vector))
            previous_vector = matrix
        counter += 1
    if counter == 1:
        return previous_vector.reshape(27, 1)
    return previous_vector

def to_string(matrix):
    matrix_T = matrix.T
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    word = ""
    for vector in matrix_T:
        idx = list(vector).index(1)
        word += alphabet[idx]
    return word

def encrypt(message, permutation_matrix):
    matrix = to_one_hot(message)    
    encrypted_matrix = permutation_matrix @ matrix
    encrypted_message = to_string(encrypted_matrix)
    return encrypted_message

def decrypt(encrypted_message, permutation_matrix):
    encrypted_matrix = to_one_hot(encrypted_message)
    matrix = np.linalg.inv(permutation_matrix) @ encrypted_matrix
    return to_string(matrix)

def enigma_machine(message, permutation_matrix, auxiliary_matrix):
    encrypted_message = ""
    counter = 0
    for char in message:
        encrypted_char = encrypt(char, permutation_matrix)
        for i in range(counter):
            encrypted_char = encrypt(encrypted_char, auxiliary_matrix)
        encrypted_message += encrypted_char
        counter += 1
    return encrypted_message

def enigma_machine_decrypt(encrypted_message, permutation_matrix, auxiliary_matrix):
    original_message = ""
    counter = 0
    for char in encrypted_message:
        for i in range(counter):
            char = decrypt(char, auxiliary_matrix)
        char = decrypt(char, permutation_matrix)
        original_message += char
        counter += 1
    return original_message











