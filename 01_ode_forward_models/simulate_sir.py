import numpy as np
import matplotlib.pyplot as plt

from utils.ode_systems import sir_model
from utils.simulate import run_ode

# Parameters
beta = 0.3
gamma = 0.1
params = (beta, gamma)

# Initial conditions
S0 = 0.99
I0 = 0.01
R0 = 0.0
y0 = [S0, I0, R0]

# Time
t_span = (0, 60)
t_eval = np.linspace(0, 60, 300)

# Solve
t, y = run_ode(sir_model, y0, params, t_span, t_eval)
S, I, R = y

# Plot
plt.plot(t, S, label="S(t)")
plt.plot(t, I, label="I(t)")
plt.plot(t, R, label="R(t)")
plt.xlabel("Time (days)")
plt.ylabel("Population Fractions")
plt.legend()
plt.grid()
plt.title("SIR Model Simulation")
plt.show()

print(t)
