# Apa itu Numpy
'''
- Numpy (Numerical Python) : library untuk operasi matematika & array
- Mirip "Exel" tapi lebih cepat, efisien, bisa multi-dimensi
- Dipakai hampir di semua Machine Learning
'''
# Contoh Code:
import numpy as np

# Membuat array
arr = np.array([1,2,3,4,5])
print("Array:", arr)

# Operasi Matematika
print("Jumlah:", arr.sum())
print("Rata-Rata:", arr.mean())
print("Maksimum:", arr.max())
print("Minimum:", arr.min())

# Array 2D
mat = np.array([[1,2,3], [4,5,6]])
print("Matrix:\n", mat)
print("Transpose\n", mat.T)