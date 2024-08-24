import numpy as np

def matrix_power(A, k):
    # Calculate matrix power A^k using numpy
    return np.linalg.matrix_power(A, k)

def multiply_matrices(A, B):
    # Check if the dimensions of the matrices are compatible
    if len(A[0]) != len(B):
        raise ValueError("The number of columns of A must match the number of rows of B.")

    # Initialize the result matrix
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(B[0])):
            result[i].append(0)
            # Perform the multiplication
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    # Return the result matrix
    return result

def matrix_input(prompt):
    # Function to take matrix input from the user
    matrix = []
    print(prompt)
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter the matrix elements row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

# Main program
print("Enter details for matrix A:")
A = matrix_input("Matrix A:")
print("\nEnter details for matrix B:")
B = matrix_input("Matrix B:")
k = int(input("\nEnter the power k for matrix A: "))

# Calculate A^k
try:
    A_k = matrix_power(A, k)
    # Multiply A^k with B
    result = multiply_matrices(A_k, B)
    print(f"\nThe result of matrix multiplication A^{k} * B is:")
    for row in result:
        print(row)
except ValueError as e:
    print(e)
