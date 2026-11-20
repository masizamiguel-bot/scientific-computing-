# Task 13: Interpolation

**Mathematical concept:** Interpolation estimates values between known points. Linear interpolation joins points by straight lines; a cubic spline joins them with smooth curves.

---

## B. Inputs and mathematical operation

**Input values:** Hourly temperatures from 08:00 to 14:00 and a request for estimates every 10 minutes.

**Operation performed:** Build interp1d (linear) and CubicSpline functions, evaluate them at 10-minute steps and print the 10:30 estimate.

**Program:** `code/Task_13_interpolation.py`

### Output of the original program

```text
Linear estimate at 10:30: 23.25 C
Cubic estimate at 10:30: 23.36 C
```

---

## C. Changed parameter

**What was changed:** The estimate time was changed from 10:30 to 13:30.

**Program:** `changed_parameter/Task_13_interpolation_changed.py`

```text
Linear estimate at 13:30: 25.25 C
Cubic estimate at 13:30: 25.41 C
```

**How the result changed:** Linear gives 25.25 C and cubic gives 25.41 C (previously 23.25 and 23.36). Near the afternoon peak the temperature curve bends over, so the spline bulges above the straight line, and the gap between the two estimates is 0.16 C.

---

## D. Meaning of the output

At 10:30 the linear estimate is 23.25 C (the midpoint of 22.5 and 24.0) and the cubic estimate is 23.36 C. The graph shows the dots as measurements, a straight-segment line and a smooth curve passing through all dots. The cubic follows the real shape of temperature, which rises quickly and then flattens.

**Graphs saved for this task:**

- `outputs/Task_13_interpolation.png`
- `outputs/Task_13_interpolation_changed.png`
- `outputs/Task_13_missing_data_modified.png`

---

## E. Modified real-world case: Filling missing sensor readings

**New assumptions:** A sensor following a known daily curve T(t) = 22 + 6 sin(pi (t - 6)/12) failed at hours 5 and 6. Because the true curve is known, estimation errors can be measured.

**New input data:** Recorded hours 0 to 4 and 7 to 12; estimates requested at hours 5 and 6.

**Program:** `modified_case/Task_13_missing_data_modified.py`

### Output

```text
Missing hours: [5. 6.]
True values: [20.4471 22.    ]
Linear estimates: [20.5176 22.0353]
Cubic estimates: [20.4482 22.0008]
Linear absolute errors: [0.0706 0.0353]
Cubic absolute errors: [0.0011 0.0008]
```

### Interpretation

True values are 20.4471 and 22.0000. Linear errors are 0.0706 and 0.0353, cubic errors are only 0.0011 and 0.0008, about 60 times smaller. For smooth natural data a cubic spline fills gaps much better than straight lines.
