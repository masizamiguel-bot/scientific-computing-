# Task 19: Numerical Optimization

**Mathematical concept:** Optimization finds inputs that minimise (or maximise) an objective function, often subject to constraints and bounds.

---

## B. Inputs and mathematical operation

**Input values:** Type A costs 12 per unit with capacity 100; Type B costs 18 per unit with capacity 170; total capacity must be at least 1000; units cannot be negative.

**Operation performed:** scipy.optimize.minimize with the SLSQP method minimises cost subject to the capacity constraint; a search over whole numbers finds the best integer plan.

**Program:** `code/Task_19_optimization.py`

### Output of the original program

```text
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution: (108, 0, 6, 1020)
```

---

## C. Changed parameter

**What was changed:** The required capacity was doubled from 1000 to 2000.

**Program:** `changed_parameter/Task_19_optimization_changed.py`

```text
Optimization success: True
Type A allocation: 0.000
Type B allocation: 11.765
Total capacity: 2000.00
Minimum planning cost: 211.76
Best nearby integer solution: (216, 0, 12, 2040)
```

**How the result changed:** The cost roughly doubled from 105.88 to 211.76 and Type B units from 5.882 to 11.765. The integer plan went from 6 Type B servers (cost 108) to 12 Type B servers (cost 216). The model is linear, so doubling the requirement doubles the cost.

---

## D. Meaning of the output

The cheapest plan uses only Type B (5.882 units, cost 105.88), because Type B costs 0.106 per unit of capacity against 0.12 for Type A. Since only whole servers can be bought, the best integer choice is 6 Type B servers with capacity 1020 and cost 108.

**Graphs saved for this task:**

- No graph for this task (text output only).

---

## E. Modified real-world case: Production planning: maximise profit

**New assumptions:** A workshop makes chairs (profit 30) and tables (profit 50). Wood: 2 per chair and 4 per table, 100 available. Labour: 3 per chair and 2 per table, 90 available. Maximising profit is done by minimising negative profit.

**New input data:** Two inequality constraints and non-negative bounds; start point (1, 1); whole-number search for confirmation.

**Program:** `modified_case/Task_19_production_plan_modified.py`

### Output

```text
Optimization success: True
Chairs to make: 20.000
Tables to make: 15.000
Maximum profit: 1350.00
Wood used: 100.00 of 100
Labour used: 90.00 of 90
Best whole-number plan (profit, chairs, tables): (1350.0, 20, 15)
```

### Interpretation

The best plan is 20 chairs and 15 tables with a maximum profit of 1350. It uses all 100 units of wood and all 90 units of labour, which is why those two constraints are called binding. The whole-number search gives the same plan, so no rounding is needed.
