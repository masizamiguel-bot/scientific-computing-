# Task 15: Numerical Differentiation

**Mathematical concept:** A derivative is a rate of change. When only data are available it is estimated by differences: forward, backward and central.

---

## B. Inputs and mathematical operation

**Input values:** GPS positions in metres at times 0 to 6 s.

**Operation performed:** Forward difference at the first point, central differences for interior points and backward difference at the last point give speed in m/s.

**Program:** `code/Task_15_numerical_differentiation.py`

### Output of the original program

```text
t=0s, position=0.0m, estimated speed=4.80m/s
t=1s, position=4.8m, estimated speed=5.10m/s
t=2s, position=10.2m, estimated speed=5.65m/s
t=3s, position=16.1m, estimated speed=6.25m/s
t=4s, position=22.7m, estimated speed=6.95m/s
t=5s, position=30.0m, estimated speed=7.65m/s
t=6s, position=38.0m, estimated speed=8.00m/s
```

---

## C. Changed parameter

**What was changed:** The last position reading was changed from 38.0 m to 42.0 m (a GPS glitch).

**Program:** `changed_parameter/Task_15_numerical_differentiation_changed.py`

```text
t=0s, position=0.0m, estimated speed=4.80m/s
t=1s, position=4.8m, estimated speed=5.10m/s
t=2s, position=10.2m, estimated speed=5.65m/s
t=3s, position=16.1m, estimated speed=6.25m/s
t=4s, position=22.7m, estimated speed=6.95m/s
t=5s, position=30.0m, estimated speed=9.65m/s
t=6s, position=42.0m, estimated speed=12.00m/s
```

**How the result changed:** The final speed jumped from 8.00 to 12.00 m/s and the previous point from 7.65 to 9.65 m/s. A central difference uses both neighbours, so one bad value spoils the estimates beside it as well.

---

## D. Meaning of the output

The estimated speed rises from 4.80 m/s to 8.00 m/s, so the vehicle is accelerating steadily. The graph is an upward line of speed against time. End points use one-sided differences, which are less accurate than the central differences in the middle.

**Graphs saved for this task:**

- `outputs/Task_15_acceleration_modified.png`
- `outputs/Task_15_speed.png`
- `outputs/Task_15_speed_changed.png`

---

## E. Modified real-world case: Acceleration from velocity data, plus step-size study

**New assumptions:** A car's velocity is recorded every second for 10 s. np.gradient estimates acceleration. A second test differentiates sin(x) at x = 1 (true derivative cos 1) for h = 0.1, 0.01 and 0.001.

**New input data:** Velocity from 0 to 17.0 m/s at t = 0 to 10 s.

**Program:** `modified_case/Task_15_acceleration_modified.py`

### Output

```text
t=0s, velocity=0.0m/s, estimated acceleration=2.10m/s2
t=1s, velocity=2.1m/s, estimated acceleration=2.15m/s2
t=2s, velocity=4.3m/s, estimated acceleration=2.35m/s2
t=3s, velocity=6.8m/s, estimated acceleration=2.35m/s2
t=4s, velocity=9.0m/s, estimated acceleration=2.20m/s2
t=5s, velocity=11.2m/s, estimated acceleration=2.05m/s2
t=6s, velocity=13.1m/s, estimated acceleration=1.80m/s2
t=7s, velocity=14.8m/s, estimated acceleration=1.45m/s2
t=8s, velocity=16.0m/s, estimated acceleration=1.00m/s2
t=9s, velocity=16.8m/s, estimated acceleration=0.50m/s2
t=10s, velocity=17.0m/s, estimated acceleration=0.20m/s2
Peak acceleration: 2.35 m/s2 at t=3s

Step-size study for the derivative of sin(x) at x=1
       h    forward error    central error
     0.1        4.294e-02        9.001e-04
    0.01        4.216e-03        9.005e-06
   0.001        4.208e-04        9.005e-08
```

### Interpretation

Peak acceleration is 2.35 m/s2 at about 3 s; it then falls to 0.20 m/s2 as the car approaches a top speed near 17 m/s, which is realistic. In the step-size study the forward error falls from 4.3e-02 to 4.2e-04 (it scales with h), but the central error falls from 9.0e-04 to 9.0e-08 (it scales with h squared), so central differences are much more accurate.
