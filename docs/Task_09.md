# Task 09: Eigenvalues and Eigenvectors

**Mathematical concept:** An eigenvector keeps its direction under a matrix: Av = lambda v. For a network adjacency matrix the dominant eigenvector scores how influential each node is.

---

## B. Inputs and mathematical operation

**Input values:** Adjacency matrix of a 4-node network (A, B, C, D). A and D connect to B and C; B and C also connect to each other.

**Operation performed:** Compute all eigenvalues with np.linalg.eig, take the largest, normalise its eigenvector so the scores add to 1 and verify Av = lambda v.

**Program:** `code/Task_09_eigenvalues.py`

### Output of the original program

```text
Dominant eigenvalue: 2.5615528128088285
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 1.9357399876532506e-15
```

---

## C. Changed parameter

**What was changed:** An extra link between A and D was added (the matrix has 1 in both A-D positions).

**Program:** `changed_parameter/Task_09_eigenvalues_changed.py`

```text
Dominant eigenvalue: 3.0
Eigenvector-based importance:
A: 0.2500
B: 0.2500
C: 0.2500
D: 0.2500
Verification error: 2.220446049250313e-16
```

**How the result changed:** The dominant eigenvalue rose from 2.5616 to 3.0 and every node now scores 0.25. With every node linked to every other, no node is more important than another.

---

## D. Meaning of the output

The dominant eigenvalue is 2.5616 and the verification error is about 2e-15, so the answer is correct. B and C score 0.2808 each and A and D score 0.2192 each. B and C are more central because they have 3 connections while A and D have 2.

**Graphs saved for this task:**

- No graph for this task (text output only).

---

## E. Modified real-world case: PageRank of a five-page website

**New assumptions:** Links: Home to Blog and Shop, Blog to Shop, Shop to Home, About to Shop and Contact, Contact to About. Damping factor 0.85 (a surfer follows a link 85 percent of the time and jumps to a random page 15 percent).

**New input data:** Google matrix G = 0.85 M + 0.15/5, where M is the column-stochastic link matrix.

**Program:** `modified_case/Task_09_pagerank_modified.py`

### Output

```text
Dominant eigenvalue: 1.0000000000000004
Column sums of G: [1. 1. 1. 1. 1.]
PageRank scores from eigenvector:
Shop: 0.3498
Home: 0.3273
Blog: 0.1691
About: 0.0869
Contact: 0.0669
Power iteration agrees: True
Verification error: 2.8031757299712627e-16
```

### Interpretation

The dominant eigenvalue is 1, as it must be for a Google matrix, and every column sums to 1. Ranks: Shop 0.3498, Home 0.3273, Blog 0.1691, About 0.0869, Contact 0.0669. Shop ranks highest because three pages link to it. The power-iteration method gives the same ranking (True).
