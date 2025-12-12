import numpy as np
import matplotlib.pyplot as plt

from utils.ode_systems import spring_mass
from utils.simulate import run_ode

alpha = 0
beta = 1
params = np.array([alpha, beta])

t_span = np.array([0, 100])
t_eval = np.linspace(0, 100, 3000)

y0 = np.array([4.0,0.0])

t, y = run_ode(spring_mass , y0, params, t_span, t_eval)

displacement = y[0]

plt.plot(t_eval, displacement)
plt.show()
