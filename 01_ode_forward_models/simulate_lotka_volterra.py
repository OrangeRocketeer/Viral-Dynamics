import numpy as np
import matplotlib.pyplot as plt

from utils.ode_systems import lotka_volterra
from utils.simulate import run_ode

alpha = 0.4
beta = 0.02
gamma = 0.4
delta = 0.01
params = np.array([alpha, beta, gamma, delta])

X0 = 30
Y0 = 10
y0 = np.array([X0, Y0])

t_span = np.array([0,60])
t_eval = np.linspace(0, 60, 300)

t, y = run_ode(lotka_volterra, y0, params, t_span, t_eval)
X,Y = y

plt.plot(t_eval, X, label='X')
plt.plot(t_eval, Y, label='Y')
plt.legend()
plt.show()



