# Task 05: Matrix Algebra and Matrix Operations

**Mathematical concept:** Matrix multiplication combines rows and columns. A transformation matrix moves, rotates or scales every point of an object at once. The determinant tells how much areas are scaled.

---

## B. Inputs and mathematical operation

**Input values:** The four corners of a unit square, a 45 degree rotation matrix and a scaling matrix (x by 2.0, y by 1.5).

**Operation performed:** Multiply rotation @ scale to get one combined matrix, then apply it to all points with a matrix product. The determinant is computed with np.linalg.det.

**Program:** `code/Task_05_matrix_algebra.py`

### Output of the original program

```text
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]
Determinant: 2.9999999999999996
```

---

## C. Changed parameter

**What was changed:** The rotation angle was changed from 45 degrees to 90 degrees.

**Program:** `changed_parameter/Task_05_matrix_algebra_changed.py`

```text
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.22464680e-16 -1.50000000e+00]
 [ 2.00000000e+00  9.18485099e-17]]
Transformed points:
 [[ 0.00000000e+00  0.00000000e+00]
 [ 1.22464680e-16  2.00000000e+00]
 [-1.50000000e+00  2.00000000e+00]
 [-1.50000000e+00  9.18485099e-17]]
Determinant: 2.9999999999999996
```

**How the result changed:** The matrix became approximately [[0, -1.5], [2, 0]] (the tiny 1e-16 entries are floating-point noise for zero). The square is now turned a quarter turn: point (1, 0) goes to (0, 2) instead of (1.414, 1.414). The determinant is still 3.0, because rotation never changes area.

---

## D. Meaning of the output

The unit square becomes a rotated rectangle. The determinant of 3.0 equals 2.0 x 1.5, which means every area is multiplied by 3, and because it is not zero the transformation is invertible. For example the corner (1, 1) moves to (0.354, 2.475) in the original run.

**Graphs saved for this task:**

- No graph for this task (text output only).

---

## E. Modified real-world case: Drone waypoint path transformation (homogeneous coordinates)

**New assumptions:** A drone path of three waypoints is rotated by 30 degrees, scaled by 0.5 and moved by (4, 3). Using 3x3 matrices with an extra coordinate of 1 lets translation be done with matrix multiplication too.

**New input data:** Waypoints (0,0), (2,0), (2,1).

**Program:** `modified_case/Task_05_drone_path_modified.py`

### Output

```text
Original waypoints:
 [[0. 0.]
 [2. 0.]
 [2. 1.]]
Transformation matrix:
 [[ 0.433 -0.25   4.   ]
 [ 0.25   0.433  3.   ]
 [ 0.     0.     1.   ]]
Transformed waypoints:
 [[4.    3.   ]
 [4.866 3.5  ]
 [4.616 3.933]]
Determinant: 0.25
Inverse recovers original path: True
```

### Interpretation

The new waypoints are (4, 3), (4.866, 3.5) and (4.616, 3.933). The determinant 0.25 equals 0.5 x 0.5, the area scaling. Multiplying by the inverse matrix recovers the original path (True), which confirms that the transformation is correct and reversible.
