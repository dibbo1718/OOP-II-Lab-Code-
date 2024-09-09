def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    cols_B = len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(cols_A))
             for j in range(cols_B)] for i in range(rows_A)]
rows_A = int(input("Enter number of rows for the first matrix: "))
cols_A = int(input("Enter number of columns for the first matrix (and rows for the second matrix): "))
rows_B = cols_A
cols_B = int(input("Enter number of columns for the second matrix: "))
A = []
B = []
print("Enter values for the first matrix (each row on a new line):")
for _ in range(rows_A):
    row = list(map(int, input().split()))
    A.append(row)
print("Enter values for the second matrix (each row on a new line):")
for _ in range(rows_B):
    row = list(map(int, input().split()))
    B.append(row)
result = multiply_matrices(A, B)
print("Product of the matrices:")
for row in result:
    print(" ".join(map(str, row)))
