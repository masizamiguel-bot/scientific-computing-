# Task 14: Curve Fitting and Approximation

**Mathematical concept:** Curve fitting picks model parameters that minimise the sum of squared residuals between data and model.

---

## B. Inputs and mathematical operation

**Input values:** Server response times for 50 to 350 concurrent users and a quadratic model a x^2 + b x + c.

**Operation performed:** curve_fit estimates a, b and c; RMSE measures the typical error and the model predicts the response at a higher load.

**Program:** `code/Task_14_curve_fitting.py`

### Output of the original program

```text
Fitted model: y = 0.002167x^2 -0.1345x +85.00
RMSE: 1.55 ms
Predicted response at 400 users: 377.86 ms
```

---

## C. Changed parameter

**What was changed:** The prediction point was moved from 400 users to 500 users.

**Program:** `changed_parameter/Task_14_curve_fitting_changed.py`

```text
Fitted model: y = 0.002167x^2 -0.1345x +85.00
RMSE: 1.55 ms
Predicted response at 500 users: 559.40 ms
```

**How the result changed:** The predicted response grew from 377.86 ms to 559.40 ms. The fit is unchanged, but 500 users is much further outside the measured range (50 to 350), so the prediction is less trustworthy. Extrapolation far from the data is risky.

---

## D. Meaning of the output

The fitted model is y = 0.002167x^2 - 0.1345x + 85.00 with RMSE 1.55 ms, so predictions are typically within about 1.5 ms of the measurements. Response time grows faster than load: the positive x^2 term shows delays building up. On the graph the curve passes very close to every dot.

**Graphs saved for this task:**

- `outputs/Task_14_app_growth_modified.png`
- `outputs/Task_14_curve_fit.png`
- `outputs/Task_14_curve_fit_changed.png`

---

## E. Modified real-world case: Mobile app user growth: exponential versus linear model

**New assumptions:** Monthly users (thousands) grow by a roughly constant percentage, so users = a exp(b month) is tested against a straight line.

**New input data:** Months 1 to 10 with users 12, 15, 19, 24, 30, 37, 47, 58, 73, 91 (thousands).

**Program:** `modified_case/Task_14_app_growth_modified.py`

### Output

```text
Exponential model: users = 9.744 * exp(0.2235 * month)
Monthly growth rate: 25.05%
Doubling time: 3.10 months
Exponential RMSE: 0.22 thousand, R2 = 0.9999
Linear RMSE: 6.61 thousand, R2 = 0.9304
Predicted users in month 12 (exponential): 142.5 thousand
Predicted users in month 12 (linear): 95.3 thousand
```

### Interpretation

The exponential model is users = 9.744 exp(0.2235 month): monthly growth of 25.05 percent and a doubling time of 3.10 months. Its RMSE is 0.22 thousand (R2 = 0.9999) against 6.61 thousand (R2 = 0.9304) for the line, so exponential is the better model. Month 12 forecast: 142.5 thousand users (exponential) against 95.3 thousand (linear), a big difference caused by the model choice.
