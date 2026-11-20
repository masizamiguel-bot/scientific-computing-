from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline, interp1d

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"

hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])

linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

ten_minute_times = np.linspace(8, 14, 37)
linear_estimates = linear(ten_minute_times)
cubic_estimates = cubic(ten_minute_times)

target_time = 13.5

print(f"Linear estimate at 13:30: {float(linear(target_time)):.2f} C")
print(f"Cubic estimate at 13:30: {float(cubic(target_time)):.2f} C")

plt.scatter(hours, temperature, label="Hourly measurements")
plt.plot(ten_minute_times, linear_estimates, label="Linear")
plt.plot(ten_minute_times, cubic_estimates, label="Cubic spline")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("Temperature interpolation")
plt.legend()
plt.grid(True)
plt.savefig(OUTPUT_DIR / "Task_13_interpolation_changed.png", dpi=150, bbox_inches="tight")
plt.show()
