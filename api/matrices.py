import numpy as np
lines = np.array([i for i in range(27)])
np.random.shuffle(lines)
identity_matrix = np.eye(27)
permute_matrix = identity_matrix[lines,:]
np.random.shuffle(lines)
auxiliary_matrix = identity_matrix[lines,:]