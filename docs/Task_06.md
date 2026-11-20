# Task 06: Solution of Systems of Linear Equations

**Mathematical concept:** A system of linear equations is written Ax = b. np.linalg.solve finds x so that A multiplied by x reproduces b.

---

## B. Inputs and mathematical operation

**Input values:** Type A servers use 4 CPU and 8 GB; Type B servers use 2 CPU and 12 GB. Observed totals: 20 CPU and 72 GB.

**Operation performed:** Solve the 2x2 system 4x + 2y = 20 and 8x + 12y = 72, then verify with A @ x and the residual b - Ax.

**Program:** `code/Task_06_linear_systems.py`

### Output of the original program

```text
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

---

## C. Changed parameter

**What was changed:** The observed totals were changed from (20 CPU, 72 GB) to (26 CPU, 76 GB).

**Program:** `changed_parameter/Task_06_linear_systems_changed.py`

```text
Type A servers: 5
Type B servers: 3
Verification A @ solution: [26. 76.]
Residual: [0. 0.]
Residual norm: 0.0
```

**How the result changed:** The solution changed from 3 Type A and 4 Type B servers to 5 Type A and 3 Type B servers (check: 4x5 + 2x3 = 26 and 8x5 + 12x3 = 76). More CPU use with only slightly more memory means more of the CPU-heavy Type A servers.

---

## D. Meaning of the output

There are 3 servers of Type A and 4 of Type B. The verification A @ solution reproduces [20, 72] exactly and the residual norm is 0, so the answer satisfies both equations.

**Graphs saved for this task:**

- No graph for this task (text output only).

---

## E. Modified real-world case: Traffic flow through three roads

**New assumptions:** Three roads share traffic at three junctions. Junction totals are 800, 700 and 500 vehicles per hour: x1 + x2 = 800, x2 + x3 = 700, x1 + x3 = 500.

**New input data:** A = [[1,1,0],[0,1,1],[1,0,1]] and b = [800, 700, 500].

**Program:** `modified_case/Task_06_traffic_flow_modified.py`

### Output

```text
Road 1 flow (vehicles/hour): 300.0
Road 2 flow (vehicles/hour): 500.0
Road 3 flow (vehicles/hour): 200.0
Verification A @ solution: [800. 700. 500.]
Residual norm: 0.0
Determinant: 2.0
Condition number: 2.0
```

### Interpretation

Road flows are 300, 500 and 200 vehicles per hour, with residual norm 0. The determinant is 2 (not zero), so the solution is unique, and the condition number is 2, which means the system is well-conditioned and small measurement errors will not be magnified.
