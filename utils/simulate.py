import numpy as np
from scipy.integrate import solve_ivp

def run_ode(ode_func, y0, params, t_span, t_eval, method="RK45"):
    """
    Generic ODE solver wrapper.
    ode_func: function f(t, y, params)
    y0      : initial state (array-like)
    params  : parameters passed into ode_func
    t_span  : (t0, tf)
    t_eval  : array of evaluation times
    """
    sol = solve_ivp(
        fun=lambda t, y: ode_func(t, y, params),
        t_span=t_span,
        y0=y0,
        t_eval=t_eval,
        method=method
    )
    return sol.t, sol.y
