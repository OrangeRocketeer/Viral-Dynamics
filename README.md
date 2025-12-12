# Viral Dynamics Inverse Problem Toolkit

This repository implements a complete workflow for studying inverse problems in viral dynamics.  
It brings together forward simulation, classical inference, Bayesian methods, identifiability diagnostics, and physics-informed neural networks (PINNs).  
The goal is to provide a reproducible and extensible research environment for parameter estimation, model validation, and uncertainty quantification in mechanistic viral models.  

---

## 1. Core Models

### 1.1 Logistic Growth
A simple nonlinear ODE used for numerical warm-up, solver comparison, and sensitivity tests:
$$
\frac{dX}{dt} = rX\left(1 - \frac{X}{K}\right).
$$

### 1.2 SIR Epidemic Model
A classical compartment model used to benchmark inference pipelines:
$$
\begin{aligned}
\frac{dS}{dt} &= -\beta S I, \\
\frac{dI}{dt} &= \beta S I - \gamma I, \\
\frac{dR}{dt} &= \gamma I.
\end{aligned}
$$

### 1.3 Viral Dynamics (Target-Cell Model)
The main model of interest:
$$
\begin{aligned}
\frac{dT}{dt} &= -\beta T V, \\
\frac{dI}{dt} &= \beta T V - \delta I, \\
\frac{dV}{dt} &= p I - c V.
\end{aligned}
$$

This system captures infection of target cells, production and clearance of virions, and the interplay between observed and unobserved states. Its inverse problem is well-known to be partially identifiable when only viral load \(V(t)\) is observed.

---

## 2. What This Repository Actually Does

### 2.1 Forward ODE Simulation
- Implements stable solvers (RK45, BDF) and stiffness detection.
- Generates synthetic datasets with tunable noise, sampling sparsity, and observation masks.
- Enables controlled experiments where “true” parameters are known.

This provides the ground truth needed to evaluate inference methods.

---

### 2.2 Classical Least-Squares Inference
- Uses nonlinear least squares to fit parameters to noisy observations.
- Supports both full-state observation ($T, I, V$) and viral-load-only settings.
- Includes residual analysis and sensitivity to initial guesses.

What it demonstrates:
- Classical methods work reliably only if the model is fully observed.  
- When only $V(t)$ is available, many parameter combinations produce indistinguishable viral curves, revealing structural non-identifiability.

---

### 2.3 Identifiability Analysis
Includes tools for:
- Profile likelihood computation for parameters such as $\beta$, $p$, and $c$.
- Detection of flat likelihood manifolds caused by latent state coupling.
- Exploration of parameter scalings that leave $V(t)$ nearly unchanged.

What it demonstrates:
- The viral model cannot uniquely determine $\beta$, $p$, and $\delta$ using viral load alone.  
- Practical identifiability heavily depends on data richness (dense vs sparse), noise levels, and whether early infection dynamics are captured.

---

### 2.4 Bayesian Inference (PyMC or Stan)
Implements:
- Priors reflecting biological plausibility.
- NUTS samplers for efficient posterior exploration.
- Posterior diagnostics: traceplots, autocorrelation, parameter correlations.

What it demonstrates:
- Bayesian methods quantify uncertainty more honestly than least-squares fits.  
- Posteriors blow up (wide, multimodal) when data do not constrain parameters.  
- When all states are observed, Bayesian posteriors shrink and center correctly.

---

### 2.5 PINN-Based Inverse Modeling
Provides PINN architectures that:
- Enforce the ODE system through automatic differentiation.
- Allow training on full observations or sparse viral-load-only data.
- Estimate both trajectories and parameters jointly.

What it demonstrates:
- PINNs can reconstruct unobserved states $T(t)$ and $I(t)$ surprisingly well.  
- Parameter estimation with PINNs is only reliable if physics loss is balanced properly and data include enough temporal variation.  
- Over-regularization makes the PINN collapse to degenerate solutions that satisfy the ODE but ignore data.

---

### 2.6 Comparison & Benchmarking
The repository includes:
- Scripts that run all methods side-by-side on identical synthetic datasets.
- Metrics for:
  - Parameter recovery error  
  - Predictive accuracy  
  - Posterior interval width  
  - Runtime and numerical stability

What it demonstrates:
- No single method dominates.  
- Least squares is fast but fragile.  
- Bayesian inference is principled but expensive.  
- PINNs interpolate missing structure but can misestimate parameters silently.  
- Identifiability is the real bottleneck.

---

## 3. Why This Repository Exists

Mechanistic viral models are widely used in immunology, virology, vaccine research, and personalized-treatment modeling.  
However, many studies implicitly assume that model parameters can be recovered from data, which is often false.

This toolkit:
- Makes these limitations explicit.  
- Provides reproducible experiments demonstrating how inference fails and why.  
- Offers an extensible foundation for more advanced modeling (immune response, latent reservoirs, drug effects, multi-compartment systems).

---

## 4. Dependencies

- Python 3.10+  
- NumPy, SciPy  
- Matplotlib  
- PyMC or Stan  
- PyTorch or JAX (for PINNs)  

---

## 5. License

MIT License.
