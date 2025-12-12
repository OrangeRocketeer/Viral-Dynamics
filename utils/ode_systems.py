# file containing reusable ODE systems
import numpy as np

# Logistic Growth Model
def logistic(t,y, params):
    P = y[0]
    k,l = params
    dP_dt = k*P*(1-(P/l))
    return dP_dt

# Susceptible Infectious Recovered model
def sir_model(t,y,params):
    beta, gamma = params
    S, I, R = y
    dS_dt = -beta*S*I
    dI_dt = beta*S*I - gamma*I
    dR_dt = gamma*I
    return np.array([dS_dt, dI_dt, dR_dt])

# Viral Dynamics (Target Cell Limited) Model
def viral_dynamics(t,y,params):
    T,I,V = y
    lambd, d, beta, delta, p, c = params
    dT_dt = lambd - d*T - beta*T*V
    dI_dt = beta*T*V - delta*I
    dV_dt = p*I - c*V
    return np.array([dT_dt, dI_dt, dV_dt])

# predator-prey Lotka-Volterra System
def lotka_volterra(t,y,params):
    X,Y = y
    alpha, beta, gamma, delta = params
    dX_dt = alpha*X - beta*X*Y
    dY_dt = -gamma*Y + delta*X*Y
    return np.array([dX_dt, dY_dt])

# pendulum equation converted to a system
def spring_mass(t,y,params):
    # here, A represents y and B represents y'
    # equation will be y''+ alpha*y' + beta*y = 0
    A,B = y
    alpha, beta = params
    dA_dt = B
    dB_dt = -beta*A - alpha*B
    return np.array([dA_dt, dB_dt])




