# Task 03: Mathematical Functions and Vectorization

**Mathematical concept:** Vectorization evaluates a mathematical expression on a whole array in one statement. NumPy runs it in fast compiled code instead of a slow Python loop.

---

## B. Inputs and mathematical operation

**Input values:** One million simulated network latencies in milliseconds (random values between 5 and 250, fixed seed 42 so results repeat).

**Operation performed:** Convert each value to seconds (divide by 1000) and square it, once with a Python loop and once with a vectorized expression, timing both with timeit.

**Program:** `code/Task_03_vectorization.py`

### Output of the original program

```text
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.1916 s
Vectorized time: 0.0042 s
Approximate speed-up: 46.0x
```

---

## C. Changed parameter

**What was changed:** The number of measurements was reduced from 1,000,000 to 100,000.

**Program:** `changed_parameter/Task_03_vectorization_changed.py`

```text
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.0172 s
Vectorized time: 0.0006 s
Approximate speed-up: 29.9x
```

**How the result changed:** Both versions became faster, but the speed-up fell from about 56x to about 30x. With less data the fixed overhead of calling NumPy is a larger share of the total time, so the advantage is smaller. Vectorization pays off most on big data. Exact times change slightly on every run and every computer.

---

## D. Meaning of the output

The first five squared latencies are small numbers in seconds squared (for example 0.0379). The loop needed about 0.30 s and the vectorized code about 0.005 s, so the same answer was produced roughly 56 times faster. The speed-up is the key result: vectorization is the standard way to handle millions of values.

**Graphs saved for this task:**

- No graph for this task (text output only).

---

## E. Modified real-world case: Currency conversion plus VAT on two million transactions

**New assumptions:** Prices are in a local currency between 100 and 50,000. Exchange rate: 0.0077 USD per unit. VAT: 16 percent added after conversion. Random seed 7.

**New input data:** 2,000,000 simulated prices generated with NumPy.

**Program:** `modified_case/Task_03_currency_vat_modified.py`

### Output

```text
First five totals in USD: [279.5  400.79 346.62 101.27 134.68]
Grand total in USD: 447,354,136.17
Both versions agree: True
Loop time: 0.3599 s
Vectorized time: 0.0053 s
Approximate speed-up: 68.0x
```

### Interpretation

Both methods agree (Both versions agree: True), so vectorizing did not change the answer. The grand total is about 447.35 million USD. The loop took about 0.36 s while the vectorized version took about 0.005 s, a speed-up of roughly 68x.
