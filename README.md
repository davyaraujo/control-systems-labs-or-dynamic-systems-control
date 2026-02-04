# control-systems-labs-or-dynamic-systems-control
This repository contains a collection of Python implementations for modeling, simulating, and controlling dynamic systems. These projects cover classical control theory, state-space analysis, and optimal control techniques.
# Control Systems & Dynamic Modeling Labs

This repository contains a collection of Python implementations for modeling, simulating, and controlling dynamic systems. These projects cover classical control theory, state-space analysis, and optimal control techniques.

## 🚀 Repository Content

The project is organized into various labs (TDs and TPs) covering different control engineering challenges:

* **TD1: Thermal Modeling** - State-space modeling for room temperature control, including open-loop and closed-loop simulations.
* **TP2: Inverted Pendulum** - Stability analysis and Linear Quadratic Regulator (LQR) design for the classic inverted pendulum on a cart.
* **TP5: Optimal Control & Dynamic Programming** - Implementation of value functions $V(x,t)$, cost surfaces, and optimal trajectory generation.
* **TP6: Coupled Tank Systems** - Level control for a two-tank system, featuring mode switching and reference tracking.

## 🛠️ Requirements & Technologies

This project uses **Python 3.x** and the following libraries:
* [Python Control Systems Library](https://python-control.readthedocs.io/) - For LTI systems and feedback analysis.
* **NumPy & SciPy** - For numerical integration and matrix computations.
* **Matplotlib** - For plotting system responses and 3D cost surfaces.

### Installation
To set up the environment, run:
```bash
pip install numpy scipy matplotlib control
