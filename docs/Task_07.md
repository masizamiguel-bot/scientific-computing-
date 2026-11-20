# Task 07: Gaussian Elimination and LU Decomposition

**Mathematical concept:** Gaussian elimination turns Ax = b into a triangular system. LU decomposition stores that work as A = LU so many right-hand sides b can be solved cheaply.

---

## B. Inputs and mathematical operation

**Input values:** One 3x3 coefficient matrix A that stays fixed, and three different measurement vectors b.

**Operation performed:** Factor A once with lu_factor and reuse it with lu_solve for each b, checking the residual and comparing with np.linalg.solve.

**Program:** `code/Task_07_gaussian_lu.py`

### Output of the original program

```text
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```

---

## C. Changed parameter

**What was changed:** The bottom-right coefficient of A was changed from 3.0 to 6.0.

**Program:** `changed_parameter/Task_07_gaussian_lu_changed.py`

```text
Measurement set 1
Solution: [4.8255814  4.30232558 2.38372093]
Residual norm: 1.7763568394002505e-15

Measurement set 2
Solution: [5.15116279 4.60465116 2.26744186]
Residual norm: 0.0

Measurement set 3
Solution: [4.70930233 4.8372093  2.63953488]
Residual norm: 2.5121479338940403e-15

Direct solution for first set: [4.8255814  4.30232558 2.38372093]
```

**How the result changed:** For the first measurement set the solution changed from [5, 5, 5] to [4.826, 4.302, 2.384]. The third unknown fell the most (5 to 2.38) because a larger diagonal coefficient means that unknown responds less to the same input, and the neighbouring unknowns shifted a little as well.

---

## D. Meaning of the output

Each row of output is the solution for one measurement set. The residual norms are about 1e-15, which is zero up to rounding, and the LU answer matches the direct solve. The matrix was factored once but used three times.

**Graphs saved for this task:**

- No graph for this task (text output only).

---

## E. Modified real-world case: Electrical circuit mesh currents with repeated voltage settings

**New assumptions:** A three-loop resistor network with resistance matrix A (ohms). Four different battery voltage settings are applied, so A is the same each time and only b changes. A second test uses a 400x400 matrix with 300 different right-hand sides to measure the benefit.

**New input data:** A = [[10,-4,0],[-4,12,-5],[0,-5,9]] and four voltage vectors, including all zeros.

**Program:** `modified_case/Task_07_circuit_lu_modified.py`

### Output

```text
Voltage set 1: [12.  0. -6.]
Mesh currents (A): [ 1.276968  0.19242  -0.559767]
Residual norm: 9.992007221626409e-16

Voltage set 2: [12.  3. -6.]
Mesh currents (A): [ 1.434402  0.586006 -0.341108]
Residual norm: 0.0

Voltage set 3: [ 9.  0. -3.]
Mesh currents (A): [ 1.001458  0.253644 -0.19242 ]
Residual norm: 5.551115123125783e-17

Voltage set 4: [0. 0. 0.]
Mesh currents (A): [0. 0. 0.]
Residual norm: 0.0

300 solves with np.linalg.solve: 0.5632 s
300 solves reusing LU factors: 0.0123 s
Speed-up from reusing LU: 45.8x
```

### Interpretation

Currents are in amperes. Zero voltages give zero currents, as expected. Residuals are around 1e-16. In the timing test, 300 repeated solves took 0.56 s while reusing the LU factors took 0.012 s, about 46 times faster, which is the whole point of LU decomposition.
