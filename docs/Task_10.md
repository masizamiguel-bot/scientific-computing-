# Task 10: Root Finding: Bisection and Fixed-Point Methods

**Mathematical concept:** A root is a value where f(x) = 0. Bisection halves an interval whose end values have opposite signs. Fixed-point iteration rewrites f(x) = 0 as x = g(x) and repeats x = g(x).

---

## B. Inputs and mathematical operation

**Input values:** Heat-balance function f(T) = T - 25 - 10 exp(-T/20), the bracket [20, 40], tolerance 1e-10 and a fixed-point start of 30 C.

**Operation performed:** Bisection with root_scalar and a hand-written fixed-point loop for T = 25 + 10 exp(-T/20); both are plotted and compared.

**Program:** `code/Task_10_bisection_fixed_point.py`

### Output of the original program

```text
Bisection equilibrium temperature: 27.525211 C
Bisection iterations: 38
Fixed-point equilibrium temperature: 27.525211 C
Fixed-point iterations: 13
```

---

## C. Changed parameter

**What was changed:** The coefficient 10 in the heat-balance equation was changed to 20.

**Program:** `changed_parameter/Task_10_bisection_fixed_point_changed.py`

```text
Bisection equilibrium temperature: 29.561521 C
Bisection iterations: 38
Fixed-point equilibrium temperature: 29.561521 C
Fixed-point iterations: 17
```

**How the result changed:** The equilibrium temperature moved from 27.525211 C to 29.561521 C and fixed-point iterations rose from 13 to 17, while bisection stayed at 38 steps. A stronger heat term raises the balance point, and fixed-point iteration converges a little more slowly when the slope of g is steeper.

---

## D. Meaning of the output

Heat gain equals heat loss at 27.525211 C. Both methods agree. Bisection needed 38 iterations and fixed point only 13. On the graph the curve crosses the horizontal zero line exactly at the dashed vertical line, the equilibrium temperature.

**Graphs saved for this task:**

- `outputs/Task_10_break_even_modified.png`
- `outputs/Task_10_equilibrium.png`
- `outputs/Task_10_equilibrium_changed.png`

---

## E. Modified real-world case: Break-even analysis of a product with congestion cost

**New assumptions:** Price 50 per unit, variable cost 20 per unit, fixed cost 2000, plus a congestion cost of 0.05 q squared. Profit(q) = 50q - (2000 + 20q + 0.05q^2). Break-even is where profit is zero.

**New input data:** Bisection bracket [10, 200]; fixed-point form q = (2000 + 0.05 q^2)/30 starting at 50; second root searched in [300, 800].

**Program:** `modified_case/Task_10_break_even_modified.py`

### Output

```text
Break-even quantity (bisection): 76.3932 units
Bisection iterations: 41
Break-even quantity (fixed point): 76.3932 units
Fixed-point iterations: 20
Second break-even quantity (profit turns negative again): 523.6068 units
Profit at first break-even: 0.00000000
```

### Interpretation

The business breaks even at 76.3932 units (bisection 41 iterations, fixed point 20, same answer). Profit is positive between 76.39 and 523.61 units; above 523.61 units congestion costs push profit negative again. The graph shows a hill-shaped profit curve with the two break-even points marked.
