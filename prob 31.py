def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j]
             for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix1 = []
matrix2 = []
print("Enter values for the first matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)
print("Enter values for the second matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row)
result = add_matrices(matrix1, matrix2)
print("Sum of the matrices:")
for row in result:
    print(" ".join(map(str, row)))
