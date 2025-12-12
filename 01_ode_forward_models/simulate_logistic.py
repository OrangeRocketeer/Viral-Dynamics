import numpy as np
import matplotlib.pyplot as plt

from utils.ode_systems import logistic
from utils.simulate import run_ode

# Parameters
r = 0.5
K = 1000
params = (r, K)

# Initial condition
X0 = 10
y0 = [X0]

# Time
t_span = (0, 20)
t_eval = np.linspace(0, 20, 300)

# Solve
t, y = run_ode(logistic , y0, params, t_span, t_eval)
X = y[0]

# Plot
plt.plot(t, X)
plt.xlabel("Time")
plt.ylabel("Population X(t)")
plt.title("Logistic Growth Simulation")
plt.grid()
plt.show()
