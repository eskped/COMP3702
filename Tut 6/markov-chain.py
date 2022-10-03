import numpy as np

P = np.array([[0.5, 0.5, 0.0],
              [0.2, 0.5, 0.3],
              [0.0, 0.5, 0.5]])

print(P)

# k-step transition matrix
Pk = np.linalg.matrix_power(P, 40)
print(Pk)

p0 = np.array([1.0, 0.0, 0.0])

print(np.matmul(p0, Pk))
