import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

t = np.linspace(0, 100, 1000)
x = [4, 0]
delta = 0.09
k = 4
m = 6


def sho(t, x):
    solution = (x[1], (-2*delta*x[1]-k/m*x[0]))
    return solution


solution = solve_ivp(sho, [0, 1000], y0=x, t_eval=t)
print(solution.y[0])
plt.plot(t, solution.y[0], 'b')
plt.axis([0, 50, -5, 5])
plt.legend(loc='best')
plt.xlabel("Czas")
plt.ylabel("Wychylenie")
plt.title('Oscylator z tłumieniem', fontsize=20)
plt.grid(True)
plt.show()
