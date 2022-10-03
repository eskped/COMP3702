import numpy as np

P = np.array([[0.5, 0.5, 0, 0, 0, 0],
              [0.5, 0, 0.5, 0, 0, 0],
              [0, 0.5, 0, 0.5, 0, 0],
              [0, 0, 0.5, 0, 0.5, 0],
              [0, 0, 0, 0.5, 0, 0.5],
              [0, 0, 0, 0, 0.5, 0.5]])
print(P)

x0 = np.array([0, 0, 1, 0, 0, 0])
print(np.matmul(x0, np.linalg.matrix_power(P, 4)))
print(np.matmul(x0, np.linalg.matrix_power(P, 10)))
print(np.matmul(x0, np.linalg.matrix_power(P, 20)))
