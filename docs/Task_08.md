# Task 08: Iterative Methods for Linear Systems

**Mathematical concept:** Jacobi and Gauss-Seidel start from a guess and repeatedly improve it until the change is smaller than a tolerance. They suit very large systems with mostly zero coefficients.

---

## B. Inputs and mathematical operation

**Input values:** A 5x5 tridiagonal system for the temperatures of five interior points on a rod with a left boundary of 100 C and a right boundary of 20 C, starting guess all zeros, tolerance 1e-8.

**Operation performed:** Run both methods, record the largest change at every iteration, compare with the direct solution and plot the errors on a log scale.

**Program:** `code/Task_08_iterative_linear.py`

### Output of the original program

```text
Jacobi temperatures: [86.66666665 73.33333331 59.99999997 46.66666664 33.33333332]
Gauss-Seidel temperatures: [86.66666665 73.3333333  59.99999997 46.66666665 33.33333332]
Direct solution: [86.66666667 73.33333333 60.         46.66666667 33.33333333]
Jacobi iterations: 150
Gauss-Seidel iterations: 75
```

---

## C. Changed parameter

**What was changed:** The tolerance was relaxed from 1e-8 to 1e-3.

**Program:** `changed_parameter/Task_08_iterative_linear_changed.py`

```text
Jacobi temperatures: [86.66497153 73.33079063 59.99660973 46.66412396 33.3316382 ]
Gauss-Seidel temperatures: [86.66475179 73.33046102 59.99712769 46.66451243 33.33225622]
Direct solution: [86.66666667 73.33333333 60.         46.66666667 33.33333333]
Jacobi iterations: 70
Gauss-Seidel iterations: 35
```

**How the result changed:** Iterations fell from 150 to 70 for Jacobi and from 75 to 35 for Gauss-Seidel, but accuracy fell too: the first temperature is 86.665 instead of 86.6667. A looser tolerance saves time at the price of precision.

---

## D. Meaning of the output

Temperatures drop evenly from 86.67 C near the hot end to 33.33 C near the cold end, as heat flows steadily from 100 C to 20 C. Gauss-Seidel needed 75 iterations against 150 for Jacobi, about half. On the graph both lines are straight on a logarithmic axis, meaning the error shrinks by a constant factor each iteration, and the Gauss-Seidel line is steeper, meaning faster convergence.

**Graphs saved for this task:**

- `outputs/Task_08_convergence.png`
- `outputs/Task_08_convergence_changed.png`
- `outputs/Task_08_heat_rod_modified.png`

---

## E. Modified real-world case: Steady-state heat along a 7-point rod

**New assumptions:** A rod with seven interior points, left end held at 80 C and right end held at 30 C, no heat source, steady state.

**New input data:** Tridiagonal matrix with 2 on the diagonal and -1 beside it, b = [80, 0, 0, 0, 0, 0, 30].

**Program:** `modified_case/Task_08_heat_rod_modified.py`

### Output

```text
Direct solution: [73.75 67.5  61.25 55.   48.75 42.5  36.25]
Jacobi solution: [73.75 67.5  61.25 55.   48.75 42.5  36.25]
Gauss-Seidel solution: [73.75 67.5  61.25 55.   48.75 42.5  36.25]
Jacobi iterations: 263
Gauss-Seidel iterations: 132
Jacobi max error vs direct: 6.506225247449038e-08
Gauss-Seidel max error vs direct: 5.52623760086135e-08
```

### Interpretation

The temperatures are 73.75, 67.5, 61.25, 55.0, 48.75, 42.5 and 36.25 C, falling by exactly 6.25 C per step, a straight line between the two ends. Jacobi needed 263 iterations and Gauss-Seidel 132, and both are within 7e-08 of the direct solution. Left graph: the temperature profile. Right graph: convergence of both methods.
