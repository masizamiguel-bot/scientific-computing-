from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root_scalar

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"


def heat_balance(T):
    return T - 25 - 20 * np.exp(-T / 20)


solution = root_scalar(
    heat_balance,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-10
)


def g(T):
    return 25 + 20 * np.exp(-T / 20)


T = 30.0
history = [T]

for _ in range(100):
    T_new = g(T)
    history.append(T_new)
    if abs(T_new - T) < 1e-10:
        break
    T = T_new

print(f"Bisection equilibrium temperature: {solution.root:.6f} C")
print(f"Bisection iterations: {solution.iterations}")
print(f"Fixed-point equilibrium temperature: {history[-1]:.6f} C")
print("Fixed-point iterations:", len(history) - 1)

temps = np.linspace(20, 40, 300)

plt.plot(temps, heat_balance(temps))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")
plt.xlabel("Temperature (C)")
plt.ylabel("Heat-balance function")
plt.title("Equilibrium temperature")
plt.grid(True)
plt.savefig(OUTPUT_DIR / "Task_10_equilibrium_changed.png", dpi=150, bbox_inches="tight")
plt.show()
