from sympy import symbols, Eq, solve

# Define the variable
x = symbols('x')

# Define the equation
equation = Eq(x**4 + 2*x**2 + 1, 0)

# Solve the equation for x
solutions = solve(equation, x)

# Print the solutions
print("Solutions:", solutions)
