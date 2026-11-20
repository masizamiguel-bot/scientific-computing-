# Task 12: Polynomial and Nonlinear Equation Solving

**Mathematical concept:** A nonlinear system has equations that are not straight lines. A numerical solver searches for values that make every residual (left side minus right side) close to zero.

---

## B. Inputs and mathematical operation

**Input values:** Circle x^2 + y^2 = 4 and parabola y = x^2 - 1 with starting guesses (1, 1) and (-1, 1).

**Operation performed:** scipy.optimize.root finds where both equations hold at the same time, then residuals and the success flag are checked.

**Program:** `code/Task_12_nonlinear_equations.py`

### Output of the original program

```text
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: [-2.4780177909633494e-13, -2.4158453015843406e-13]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991  1.30277564]
Residuals: [-2.4780177909633494e-13, -2.4158453015843406e-13]
Converged: True
```

---

## C. Changed parameter

**What was changed:** The circle was enlarged from radius 2 (x^2 + y^2 = 4) to radius 3 (x^2 + y^2 = 9).

**Program:** `changed_parameter/Task_12_nonlinear_equations_changed.py`

```text
Initial guess: [1.0, 1.0]
Intersection: [1.83637723 2.37228132]
Residuals: [-1.3891110484109959e-12, 1.4597212327771558e-12]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.83637723  2.37228132]
Residuals: [-1.3855583347321954e-12, 1.4601653219870059e-12]
Converged: True
```

**How the result changed:** The intersections moved from (+-1.5175, 1.3028) to (+-1.8364, 2.3723). A larger circle reaches the parabola further out and higher up.

---

## D. Meaning of the output

The curves meet at two mirror-image points, (1.5175, 1.3028) and (-1.5175, 1.3028). The residuals are about 1e-13 (essentially zero) and Converged is True. Different starting guesses lead to different intersections, which is why more than one initial guess is used.

**Graphs saved for this task:**

- No graph for this task (text output only).

---

## E. Modified real-world case: Drone path against a no-fly zone, and a projectile landing time

**New assumptions:** The no-fly zone is a circle with centre (2, 1) and radius 3. The drone flies along the line y = 0.5x - 1. Separately a ball follows h(t) = -4.9t^2 + 20t + 2 (height in metres) and np.roots finds when h = 0.

**New input data:** Starting guesses (5, 1.5) and (-0.2, -1); polynomial coefficients [-4.9, 20, 2].

**Program:** `modified_case/Task_12_drone_zone_modified.py`

### Output

```text
Initial guess: [5.0, 1.5]
Path enters or leaves the zone at: [4.9612 1.4806]
Residuals: [3.552713678800501e-15, -2.220446049250313e-16]
Converged: True

Initial guess: [-0.2, -1.0]
Path enters or leaves the zone at: [-0.1612 -1.0806]
Residuals: [3.552713678800501e-15, 0.0]
Converged: True

Projectile height roots (s): [ 4.1793 -0.0977]
Landing time: 4.1793 s
Height at landing time: -7.55e-15 m
```

### Interpretation

The path crosses the zone boundary at (-0.1612, -1.0806) and (4.9612, 1.4806), so between those points the drone is inside the zone. The ball lands after 4.1793 s; the other root, -0.0977 s, is negative and means a time before launch, so it is ignored.
