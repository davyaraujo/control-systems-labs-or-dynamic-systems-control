# Room Heating Control (using hand-made open/closed-loop simulation)
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as pt
pt.rcParams.update({"text.usetex": True, "font.family": "Times"})
import control as ct
# state-space LTI model of heated room
# TODO
A = np.array([-.2])
B = np.array([[.2]])
C = np.array([[5]])
D = np.array([[0.0]])
# system and controller
# TODO
ks = 5
kp = 0.3
y0 = 20
x0 = np.array([1/ks * y0])
t0, tf = 0,30
t = np.linspace(t0, tf, 100)
# parameters
# TODO
HeatedRoom = ct.ss(A, B, C, D)
Thermostat = ct.tf([kp], [1])
System = ct.series(Thermostat, HeatedRoom)
closed_loop = ct.feedback(System, 1)
# simulation
y,t = ct.step_response(HeatedRoom, T=t)

# compute and plot system response



# TODO
pt.plot(t, y, linewidth=2.0, color='blue')
pt.grid(color='lightgray', linestyle='--')
pt.xlim([t0, tf])
pt.ylabel(r'Temperature (\textdegree C)')
pt.xlabel('Time (s)')
pt.title('Room heating')
pt.show()
