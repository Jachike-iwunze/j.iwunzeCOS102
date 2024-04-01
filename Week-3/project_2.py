def solve_quadratic():
    A = float(input("Enter value for A:"))
    B = float(input("Enter value for B:"))
    C = float(input("Enter value for C:"))

    # Solving quadratic equation with the formula
    discriminant = (B ** 2 - 4 * A * C) ** 0.5
    x1 = (-B + discriminant) / (2 * A)
    x2 = (-B - discriminant) / (2 * A)
    print(f"The roots of the equations are: {x1} and {x2}")

def solve_cubic():
    A = float(input("Enter value for A:"))
    B = float(input("Enter value for B:"))
    C = float(input("Enter value for C:"))
    D = float(input("Enter value for D:"))

    # Solving cubic equation by trial and error from a range of integers
    roots = []
    for i in range(-100, 100):
        x = i
        equation = (A * x ** 3) + (B * x ** 2) + (C * x) + (D * x ** 0)
        if equation == 0.0:
            roots.append(x)
    if len(roots) == 0:
        print("No roots found")
    else:
        print(f"The roots are {roots}")

def solve_quartic():
    A = float(input("Enter value for A:"))
    B = float(input("Enter value for B:"))
    C = float(input("Enter value for C:"))
    D = float(input("Enter value for D:"))
    E = float(input("Enter value for E:"))

    # Solving quartic equation by trial and error from a range of integers only
    roots = []
    for i in range(-100, 100):
        x = i
        equation = (A * x ** 4) + (B * x ** 3) + (C * x ** 2) + (D * x) + (E * x ** 0)
        if equation == 0.0:
            roots.append(x)
    if len(roots) == 0:
        print("No roots")
    else:
        print(f"The roots are {roots}")

userInput = int(input("Enter your choice:\nSelect 1 for Quadratic Equation\nSelect 2 for Cubic Equation\nSelect 3 for Quartic Equation"))

if userInput == 1:
    solve_quadratic()
elif userInput == 2:
    solve_cubic()
elif userInput == 3:
    solve_quartic()
else:
    print("Invalid choice")
