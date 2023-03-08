import numpy as np
linhas = np.array([i for i in range(27)])
np.random.shuffle(linhas)
matriz_identidade = np.eye(27)
matriz_permutacao = matriz_identidade[linhas,:]
np.random.shuffle(linhas)
matriz_auxiliar = matriz_identidade[linhas,:]