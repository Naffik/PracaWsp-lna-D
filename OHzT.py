import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

t = np.linspace(0, 50, 1000)
x = [4, 0]
x_2 = [0, 4]
delta = 0.05
k = 2
m = 2


def sho(t, x):
    result = [x[1], (-2 * delta * x[1] - k / m * x[0])]
    return result


def sho_2(t, x_2):
    result = [x_2[1], (-2 * delta * x_2[1] - k / m * x_2[0])]
    return result


solution = solve_ivp(sho, [0, 1000], y0=x, t_eval=t)
solution_2 = solve_ivp(sho_2, [0, 1000], y0=x_2, t_eval=t)
plt.plot(t, solution.y[0], 'b')
plt.plot(t, solution_2.y[0], 'orange')
plt.axis([0, 50, -5, 5])
plt.xlabel("Czas")
plt.ylabel("Wychylenie")
plt.title('Oscylator z tłumieniem', fontsize=20)
plt.grid(True)
plt.show()
