import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
import math
sns.set()

t = np.linspace(0, 100, 1000)
x = [0, 0]
delta = 0.3
omega = 2
k = 14.5
m = 27
A = 0.1


def sho(t, x):
    solution = [x[1], (-2 * delta * x[1] - (k / m) * x[0] + A * math.sin(omega*t))]
    return solution


solution = solve_ivp(sho, [0, 1000], y0=x, t_eval=t)
plt.plot(t, solution.y[0], 'b')
plt.axis([0, 50, -0.075, 0.075])
plt.xlabel("Czas")
plt.ylabel("Wychylenie")
plt.title('Oscylator z tłumieniem i z wymuszeniem', fontsize=20)
plt.grid(True)
plt.show()
