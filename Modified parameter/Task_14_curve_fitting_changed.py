from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)


def model(x, a, b, c):
    return a * x ** 2 + b * x + c


parameters, covariance = curve_fit(model, users, response_ms)
a, b, c = parameters

predicted = model(users, a, b, c)
rmse = np.sqrt(np.mean((response_ms - predicted) ** 2))

print(f"Fitted model: y = {a:.6f}x^2 {b:+.4f}x {c:+.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 500 users: {model(500, a, b, c):.2f} ms")

x_plot = np.linspace(users.min(), 500, 300)

plt.scatter(users, response_ms, label="Measurements")
plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted curve")
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting")
plt.legend()
plt.grid(True)
plt.savefig(OUTPUT_DIR / "Task_14_curve_fit_changed.png", dpi=150, bbox_inches="tight")
plt.show()
