import numpy as np
import matplotlib.pyplot as plt


def rect_function(t):
    return np.where(np.abs(t) <= 0.5, 1, 0)


def fourier_transform(t, rect, u):
    F_u = np.array([np.trapz(rect * np.exp(-2j * np.pi * nu * t), t) for nu in u])
    return F_u


def inverse_fourier_transform(u, F_u):
    t = np.linspace(-1, 1, 4000)
    f_t = np.array([np.trapz(F_u * np.exp(2j * np.pi * n * u), u) for n in t])
    return t, f_t.real


t = np.linspace(-10, 10, 400)
u = np.linspace(-10, 10, 4000)

rect = rect_function(t)

F_u = fourier_transform(t, rect, u)
t_inverse, rect_inverse = inverse_fourier_transform(u, F_u)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(u, fourier_transform(t, rect, u))
plt.title('Фурье-образ')
plt.xlabel('ν')
plt.ylabel('Π(ν)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(t_inverse, rect_inverse)
plt.title('Восстановленная функция')
plt.xlabel('t')
plt.ylabel('Π(t)')
plt.grid(True)
plt.tight_layout()
plt.show()
