import numpy as np
import matplotlib.pyplot as plt

from utils.ode_systems import viral_dynamics
from utils.simulate import run_ode

# Parameters (realistic HIV-like example)
params = (
    1e4,      # lam
    0.01,     # dT
    2e-7,     # beta
    0.7,      # delta
    1000,     # p
    10        # c
)

# Initial conditions
T0 = 1e6
I0 = 0
V0 = 10
y0 = [T0, I0, V0]

# Time
t_span = (0, 15)
t_eval = np.linspace(0, 15, 400)

# Solve
t, y = run_ode(viral_dynamics, y0, params, t_span, t_eval)
T, I, V = y

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, T, label="T(t)")
plt.plot(t, I, label="I(t)")
plt.plot(t, V, label="V(t)")
plt.yscale("log")
plt.xlabel("Time (days)")
plt.ylabel("Population (log scale)")
plt.grid()
plt.legend()
plt.title("Forward Simulation of Viral Dynamics Model")
plt.show()
