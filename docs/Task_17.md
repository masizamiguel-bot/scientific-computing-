# Task 17: Ordinary Differential Equations: Euler Method

**Mathematical concept:** Euler's method steps forward with y_next = y + h f(t, y). A smaller step size h usually gives higher accuracy at more computation.

---

## B. Inputs and mathematical operation

**Input values:** Newton's law of cooling dT/dt = -k (T - 25) with k = 0.12 per minute, starting at 90 C, step h = 1 minute, 30 minutes.

**Operation performed:** Repeated Euler updates give the temperature curve, compared with the exact solution 25 + 65 exp(-0.12 t).

**Program:** `code/Task_17_euler_ode.py`

### Output of the original program

```text
Euler temperature after 30 min: 26.40 C
Exact temperature after 30 min: 26.78 C
Final absolute error: 0.3720 C
```

---

## C. Changed parameter

**What was changed:** The step size was increased from 1 minute to 5 minutes.

**Program:** `changed_parameter/Task_17_euler_ode_changed.py`

```text
Euler temperature after 30 min: 25.27 C
Exact temperature after 30 min: 26.78 C
Final absolute error: 1.5098 C
```

**How the result changed:** The final error grew from 0.372 C to 1.510 C (about four times larger) and the Euler result became 25.27 C instead of 26.40 C, against an exact value of 26.78 C. Bigger steps mean a cruder curve.

---

## D. Meaning of the output

After 30 minutes the object is at about 26.4 C by Euler and 26.78 C exactly, an error of 0.37 C. Euler cools slightly too fast because it uses the steeper slope from the start of each step. The graph shows the object cooling quickly at first and levelling off near room temperature (25 C).

**Graphs saved for this task:**

- `outputs/Task_17_euler.png`
- `outputs/Task_17_euler_changed.png`
- `outputs/Task_17_logistic_euler_modified.png`

---

## E. Modified real-world case: Logistic population growth with different Euler step sizes

**New assumptions:** Population P grows by dP/dt = r P (1 - P/K) with growth rate r = 0.4 per year, carrying capacity K = 1000 and starting population 100 (an S-shaped curve). The exact solution is known.

**New input data:** Steps h = 4, 1 and 0.1 years for 30 years.

**Program:** `modified_case/Task_17_logistic_euler_modified.py`

### Output

```text
h=4.0: population at t=30 is 992.794, absolute error 7.0829
h=1.0: population at t=30 is 999.993, absolute error 0.0480
h=0.1: population at t=30 is 999.952, absolute error 0.0078
Exact population at t=30: 999.945
Carrying capacity: 1000
```

### Interpretation

The exact population at year 30 is 999.945, close to the capacity of 1000. The error is 7.08 for h = 4, 0.048 for h = 1 and 0.0078 for h = 0.1, so smaller steps give better accuracy. The graph shows the S-curve: slow start, fast middle growth and levelling off at the carrying capacity.
