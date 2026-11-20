# Task 04: Floating-Point Arithmetic and Numerical Errors

**Mathematical concept:** Computers store most decimals as binary approximations, so tiny round-off errors appear. Absolute error = |true - approximate| and relative error = absolute error / |true|.

---

## B. Inputs and mathematical operation

**Input values:** The numbers 0.1, 0.2, 0.3; the true value sqrt(2) against the approximation 1.414; and x = 1e-4, 1e-8, 1e-12 for a stable and an unstable formula.

**Operation performed:** Compare numbers exactly and with np.isclose, compute absolute and relative error, and evaluate (sqrt(1+x)-1)/x against the algebraically equal stable form 1/(sqrt(1+x)+1).

**Program:** `code/Task_04_numerical_errors.py`

### Output of the original program

```text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

---

## C. Changed parameter

**What was changed:** The approximation of sqrt(2) was changed from 1.414 to 1.41421.

**Program:** `changed_parameter/Task_04_numerical_errors_changed.py`

```text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00000356
Relative error: 0.00025190%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

**How the result changed:** The absolute error dropped from 0.00021356 to 0.00000356, and the relative error from 0.0151 percent to 0.000252 percent. About two extra correct digits made the error roughly 60 times smaller.

---

## D. Meaning of the output

0.1 + 0.2 prints 0.30000000000000004, so an exact comparison with 0.3 is False while np.isclose returns True. Always compare floats with a tolerance. In the last test the direct formula loses accuracy as x shrinks (0.500044450291 at x = 1e-12) while the rewritten formula stays at 0.500000000000, the true limit. This is catastrophic cancellation: subtracting nearly equal numbers destroys digits.

**Graphs saved for this task:**

- No graph for this task (text output only).

---

## E. Modified real-world case: Banking: adding one million small deposits

**New assumptions:** One million deposits of 0.1 each (the exact total is 100,000). Compared methods: a plain loop, math.fsum, NumPy pairwise sum and Decimal. Also a 12-month balance at 1.5 percent per month.

**New input data:** deposit = 0.1, payments = 1,000,000, opening balance = 1000.

**Program:** `modified_case/Task_04_bank_rounding_modified.py`

### Output

```text
Naive loop total: 100000.0000013329
math.fsum total: 100000.0000000000
NumPy pairwise total: 100000.0000000000
Decimal total: 100000.0
naive: absolute error = 1.333e-06, relative error = 1.333e-11
fsum: absolute error = 0.000e+00, relative error = 0.000e+00
numpy: absolute error = 2.910e-11, relative error = 2.910e-16
Naive total equals expected exactly: False
Naive total close to expected: True
Balance after 12 months at 1.5 percent: 1195.618171
Rounded to cents: 1195.62
```

### Interpretation

The naive loop gives 100000.0000013329, an error of 1.33e-06, and does not equal 100000 exactly, but np.isclose says it is close. math.fsum and Decimal are exact and the NumPy pairwise sum is almost exact (2.9e-11). In banking, small errors accumulate over millions of operations, so exact tools such as Decimal are used for money. The 12-month balance is 1195.618171, which rounds to 1195.62.
