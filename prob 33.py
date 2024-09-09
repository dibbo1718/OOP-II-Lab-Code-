def transpose(matrix):
    return list(map(list, zip(*matrix)))
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter values for the matrix (each row on a new line):")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
transposed = transpose(matrix)
print("Transposed matrix:")
for row in transposed:
    print(" ".join(map(str, row)))
