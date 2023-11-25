# 1. Напишите функцию для транспонирования матрицы.

def transpose(matrix):
  transpose_matrix = []
  zipped_rows = zip(*matrix)
  transpose_matrix = [list(row) for row in zipped_rows]
  return transpose_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
matrix_1 = transpose(matrix)
print(matrix_1)