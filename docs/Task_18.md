# Task 18: Numerical Solution of ODEs Using SciPy

**Mathematical concept:** solve_ivp uses higher-order adaptive methods to solve dy/dt = f(t, y) and automatically adjusts its step size.

---

## B. Inputs and mathematical operation

**Input values:** RC charging circuit: supply 5 V, R = 1000 ohms, C = 0.001 F (time constant RC = 1 s), initial voltage 0 V, time 0 to 5 s.

**Operation performed:** Solve dV/dt = (Vs - V)/(RC) and compare with the exact curve 5 (1 - exp(-t/RC)).

**Program:** `code/Task_18_scipy_ode.py`

### Output of the original program

```text
Solver success: True
Capacitor voltage at 5 s: 4.9663 V
Maximum error against exact solution: 9.282e-10 V
```

---

## C. Changed parameter

**What was changed:** The capacitance was increased from 0.001 F to 0.004 F (time constant 4 s).

**Program:** `changed_parameter/Task_18_scipy_ode_changed.py`

```text
Solver success: True
Capacitor voltage at 5 s: 3.5675 V
Maximum error against exact solution: 4.587e-10 V
```

**How the result changed:** The capacitor voltage at 5 s fell from 4.9663 V to 3.5675 V. A bigger capacitor takes longer to charge. The exact value is 5 (1 - exp(-1.25)) = 3.5675 V, so the solver is still correct (maximum error 4.6e-10 V).

---

## D. Meaning of the output

After 5 s (five time constants) the capacitor is at 4.9663 V, nearly the 5 V supply. The solver succeeded and its maximum error against the exact solution is only 9.3e-10 V. The graph shows a curve that rises quickly and then flattens toward 5 V; the solver line and the exact dashed line lie on top of each other.

**Graphs saved for this task:**

- `outputs/Task_18_rc_circuit.png`
- `outputs/Task_18_rc_circuit_changed.png`
- `outputs/Task_18_sir_epidemic_modified.png`

---

## E. Modified real-world case: SIR epidemic model

**New assumptions:** A population of 1000 with one initial infection. Infection rate beta = 0.4 per day, recovery rate gamma = 0.1 per day, so R0 = beta/gamma = 4. S, I and R are the susceptible, infected and recovered people.

**New input data:** Initial values S = 999, I = 1, R = 0 over 160 days.

**Program:** `modified_case/Task_18_sir_epidemic_modified.py`

### Output

```text
Solver success: True
Basic reproduction number R0: 4.00
Peak infections: 403.6 people on day 27.2
Total ever infected by day 160: 980.2 of 1000
Still susceptible at day 160: 19.8
Largest deviation from population size: 6.821e-13
```

### Interpretation

Infections peak at about 403.6 people on day 27.2. By day 160 about 980.2 of the 1000 people have been infected and only 19.8 never were. S + I + R stays equal to 1000 within 7e-13, which confirms the solver conserves the population. The graph shows susceptible falling, infected rising and falling in a hump and recovered growing.
