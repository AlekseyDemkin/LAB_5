import numpy as np
import matplotlib.pyplot as plt


def rect(t):
    return np.where(np.abs(t) <= 0.5, 1, 0)


def sinc(u):
    u = np.where(u == 0, 1e-10, u)
    return np.sin(np.pi * u) / (np.pi * u)


t = np.linspace(-1, 1, 400)
u = np.linspace(-10, 10, 400)

plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.plot(t, rect(t))
plt.title('Прямоугольная функция $\\Pi(t)$')
plt.xlabel('t')
plt.ylabel('$\\Pi(t)$')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(u, sinc(u))
plt.title('Фурье-образ $\\Pi(\\hat{\\u})$')
plt.xlabel('$\\nu$')
plt.ylabel('$\\Pi(\\hat{u})$')
plt.grid(True)

plt.tight_layout()
plt.show()
