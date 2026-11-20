# Task 16: Numerical Integration

**Mathematical concept:** An integral is accumulated quantity (area under a curve). The trapezoidal rule uses straight segments and Simpson's rule uses parabolas, which is usually more accurate for smooth data.

---

## B. Inputs and mathematical operation

**Input values:** Smart-meter power readings in kW every two hours from 0 to 12 h.

**Operation performed:** np.trapezoid and scipy simpson integrate power over time to give energy in kWh.

**Program:** `code/Task_16_numerical_integration.py`

### Output of the original program

```text
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule: 15.800 kWh
Difference between estimates: 0.100 kWh
```

---

## C. Changed parameter

**What was changed:** The 6 hour reading was raised from 1.8 kW to 3.0 kW (a short, sharp peak).

**Program:** `changed_parameter/Task_16_numerical_integration_changed.py`

```text
Energy using trapezoidal rule: 18.100 kWh
Energy using Simpson's rule: 19.000 kWh
Difference between estimates: 0.900 kWh
```

**How the result changed:** Energy rose from 15.7 to 18.1 kWh (trapezoid) and from 15.8 to 19.0 kWh (Simpson). The difference between the rules grew from 0.1 to 0.9 kWh because a sharper peak means more curvature, which straight segments handle worse.

---

## D. Meaning of the output

The house used about 15.7 to 15.8 kWh over 12 hours. The two rules differ by only 0.1 kWh, so the estimate is stable. Energy is the area under the power curve, which is why integration is used for billing and consumption.

**Graphs saved for this task:**

- No graph for this task (text output only).

---

## E. Modified real-world case: Total river water volume from flow measurements

**New assumptions:** Flow in m3/s is recorded every hour for 12 hours during a flood. Volume = flow integrated over time, multiplied by 3600 seconds per hour. A check integrates sin(x) from 0 to pi (exact value 2).

**New input data:** 13 hourly flows from 12.0 up to 49.5 and back down to 13.0 m3/s.

**Program:** `modified_case/Task_16_river_flow_modified.py`

### Output

```text
Volume using trapezoidal rule: 1,261,800 m3
Volume using Simpson's rule: 1,262,400 m3
Difference between estimates: 600 m3
Average flow over 12 hours: 29.22 m3/s

Accuracy check on sin(x) from 0 to pi with 9 points (exact value 2)
Trapezoidal error: 2.577e-02
Simpson error: 2.692e-04
```

### Interpretation

Total volume is about 1,261,800 m3 (trapezoid) or 1,262,400 m3 (Simpson), a difference of only 600 m3, and the average flow is 29.22 m3/s. In the accuracy check the trapezoid error is 2.6e-02 and the Simpson error is 2.7e-04, so Simpson is about 100 times more accurate on smooth data.
