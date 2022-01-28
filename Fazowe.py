import math

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

t = np.linspace(0, 20, 1000)
x = [5, 0]
delta = 0.05
k = 2
m = 2


def sho(t, x):
    result = (x[1], (-2*delta*x[1]-(k/m)*x[0]))
    return result


solution = solve_ivp(sho, [0, 1000], y0=x, t_eval=t)
plt.plot(solution.y[0], solution.y[1], color='b')
plt.xlabel("Czas")
plt.ylabel("Wychylenie")
plt.title('Oscylator z tłumieniem', fontsize=20)
plt.grid(True)
plt.show()
