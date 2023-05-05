import numpy as np

# Definindo a matriz A
A = np.array([[3, 2, 7], [2, 5, 7], [7, 1, 8]])

# Calculando os autovalores e autovetores
autovalores, autovetores = np.linalg.eig(A)

# Imprimindo os resultados
print("Autovalores:")
print(autovalores)

print("\nAutovetores:")
print(autovetores)

import numpy as np

# Definindo a matriz A
A = np.array([[3, 2, 7], [2, 5, 7], [7, 1, 8]])

# Calculando a decomposição SVD
U, S, Vt = np.linalg.svd(A)

# Imprimindo os resultados
print("Matriz U:")
print(U)

print("\nMatriz diagonal de valores singulares S:")
print(S)

print("\nMatriz V transposta:")
print(Vt)