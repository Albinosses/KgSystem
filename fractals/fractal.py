import numpy as np
import matplotlib.pyplot as plt


width, height = 800, 800
x_min, x_max = -2.0, 2.0
y_min, y_max = -2.0, 2.0
max_iter = 50


def f_ch(z):
    return np.cosh(z)


def f_sin_z_cos_z(z):
    return np.sin(z) * np.cos(z)


def build_fractal(f, eps, iterations):
    image = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            zx = x * (x_max - x_min) / (width - 1) + x_min
            zy = y * (y_max - y_min) / (height - 1) + y_min
            z = zx + 1j * zy
            for i in range(iterations):
                if abs(z) > eps:
                    break
                z = f(z)
            image[x, y] = i
    return image


def build_fractal_ch_z(eps, iterations):
    return build_fractal(f_ch, eps, iterations)


def build_fractal_sin_z_cos_z(eps, iterations):
    return build_fractal(f_sin_z_cos_z, eps, iterations)


def save_fractal(image, cmap):
    plt.clf()
    plt.imshow(image, extent=(x_min, x_max, y_min, y_max), cmap=cmap, origin='lower')
    plt.savefig("fractal.png", format="png")
