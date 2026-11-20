from scipy.optimize import root


def equations(z):
    x, y = z
    return [
        x ** 2 + y ** 2 - 9,
        y - (x ** 2 - 1)
    ]


for guess in ([1.0, 1.0], [-1.0, 1.0]):
    solution = root(equations, guess)
    print("Initial guess:", guess)
    print("Intersection:", solution.x)
    print("Residuals:", [float(r) for r in equations(solution.x)])
    print("Converged:", solution.success)
    print()
