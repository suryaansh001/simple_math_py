import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the function to be integrated
f = x/(x-1)

# Compute the antiderivative (indefinite integral)
F = sp.integrate(f, x)

# Display the result
print(f"The antiderivative of the function is: {F}")
