# Task 11: Root Finding: Newton-Raphson and Secant Methods

**Mathematical concept:** Newton-Raphson uses x_new = x - f(x)/f'(x). The secant method replaces the derivative with the slope through two recent points.

---

## B. Inputs and mathematical operation

**Input values:** Investment of 10,000 followed by inflows 3000, 3500, 4000 and 2500, and starting guesses 0.10 (Newton) and 0.05 and 0.20 (secant).

**Operation performed:** Find the rate where net present value equals zero, which is the internal rate of return (IRR).

**Program:** `code/Task_11_newton_secant.py`

### Output of the original program

```text
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
Newton iterations: 4
Secant iterations: 7
NPV at Newton solution: 0.000000
```

---

## C. Changed parameter

**What was changed:** The final cash inflow was changed from 2500 to 4500.

**Program:** `changed_parameter/Task_11_newton_secant_changed.py`

```text
IRR using Newton-Raphson: 17.093686%
IRR using Secant method: 17.093686%
Newton iterations: 5
Secant iterations: 6
NPV at Newton solution: 0.000000
```

**How the result changed:** The IRR rose from 11.54 percent to 17.09 percent. Larger returns mean the investment can pay a higher discount rate before NPV hits zero. Newton needed 5 steps instead of 4 and secant 6 instead of 7.

---

## D. Meaning of the output

The IRR is 11.542461 percent. NPV at that rate is 0.000000, so the root is accurate. Newton needed only 4 iterations while the secant method needed 7: Newton is faster per step but needs a derivative formula.

**Graphs saved for this task:**

- No graph for this task (text output only).

---

## E. Modified real-world case: Finding the interest rate of a loan

**New assumptions:** A loan of 10,000 repaid in 12 monthly payments of 920. Solve payment x (1 - (1+r)^-12)/r - loan = 0 for the monthly rate r. Newton uses a numerical central-difference derivative.

**New input data:** LOAN = 10000, PAYMENT = 920, MONTHS = 12.

**Program:** `modified_case/Task_11_loan_rate_modified.py`

### Output

```text
Monthly rate using Newton-Raphson: 1.555981%
Monthly rate using Secant method: 1.555981%
Newton iterations: 4
Secant iterations: 6
Nominal annual rate: 18.6718%
Effective annual rate: 20.3555%
Total interest paid: 1040.00
Gap at Newton solution: -9.09e-12
```

### Interpretation

The monthly rate is 1.555981 percent (both methods agree), a nominal annual rate of 18.67 percent and an effective annual rate of 20.36 percent because of monthly compounding. The borrower pays 1040 in interest in total. Newton needed 4 iterations and secant 6.
