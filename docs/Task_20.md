# Task 20: Random Numbers and Monte Carlo Methods

**Mathematical concept:** Monte Carlo methods estimate a probability by running many random simulations and counting how often an event occurs.

---

## B. Inputs and mathematical operation

**Input values:** Server capacity 1000; demand is random with mean 850 and standard deviation 120; 100,000 simulations; seed 42.

**Operation performed:** Draw normally distributed demand, count overloads (demand above capacity) and divide by the number of simulations.

**Program:** `code/Task_20_monte_carlo.py`

### Output of the original program

```text
Estimated overload probability: 10.6160%
Number of overload cases: 10616 out of 100000
```

---

## C. Changed parameter

**What was changed:** The mean demand was increased from 850 to 920.

**Program:** `changed_parameter/Task_20_monte_carlo_changed.py`

```text
Estimated overload probability: 25.0880%
Number of overload cases: 25088 out of 100000
```

**How the result changed:** The overload probability rose from 10.62 percent to 25.09 percent. The theory agrees: with mean 920 the capacity is only 0.67 standard deviations above the mean, which gives about 25.2 percent.

---

## D. Meaning of the output

About 10.62 percent of simulated scenarios (10,616 of 100,000) overload the server, close to the theoretical value of about 10.56 percent. On the graph the running estimate jumps around when only a few simulations have been used and settles near 10.6 percent as the number grows. More simulations give a more reliable estimate.

**Graphs saved for this task:**

- `outputs/Task_20_monte_carlo.png`
- `outputs/Task_20_monte_carlo_changed.png`
- `outputs/Task_20_project_risk_modified.png`

---

## E. Modified real-world case: Project completion risk, plus estimating pi

**New assumptions:** A project has three tasks with uncertain durations given as (minimum, most likely, maximum) days: design (5, 7, 12), build (10, 14, 25) and testing (4, 6, 10), modelled with triangular distributions. The deadline is 30 days. Pi is also estimated using random points in a square.

**New input data:** 200,000 simulated projects; 1,000,000 random points for pi; seed 42.

**Program:** `modified_case/Task_20_project_risk_modified.py`

### Output

```text
Mean project duration: 30.99 days
Standard deviation: 3.71 days
90th percentile duration: 36.07 days
Probability of missing the 30-day deadline: 57.3835%
Number of overruns: 114767 out of 200000
Pi estimate with 1000000 points: 3.13967
Error against np.pi: 0.00192
```

### Interpretation

The mean duration is 30.99 days with a standard deviation of 3.71 days. The chance of missing the 30-day deadline is 57.38 percent, and a 90 percent safe schedule needs about 36.07 days. The pi estimate is 3.13967 (error 0.0019). The histogram shows a right-skewed distribution: the long tail on the right is the risk of delays.
