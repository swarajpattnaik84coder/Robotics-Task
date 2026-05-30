
A = input("Enter the first matrix (rows separated by ';' and elements separated by ','): ")
B = input("Enter the second matrix (rows separated by ';' and elements separated by ','): ")

# Convert input strings to matrices
A = [[int(x) for x in row.split(',')] for row in A.split(';')]
B = [[int(x) for x in row.split(',')] for row in B.split(';')]

# Result matrix
result = []

for i in range(len(A)): # Iterate through rows
    row = []
    for j in range(len(A[0])):  # Iterate through columns
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nSum Matrix:")
for row in result:
    print(row)