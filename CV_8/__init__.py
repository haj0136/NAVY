import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


def main():
    iterations_count = 500
    width = 720
    height = 720

    def mandelbrot(c):
        z = c
        for n in range(iterations_count):
            if abs(z) > 2:
                return n
            z = z*z + c
        return 0

    def mandelbrot_set(x_min, x_max, y_min, y_max):
        x_points = np.linspace(x_min, x_max, width)
        y_points = np.linspace(y_min, y_max, height)
        n = np.empty((width, height))
        for i in range(width):
            print(i)
            for j in range(height):
                n[i][j] = mandelbrot(x_points[i] + 1j * y_points[j])
        return n

    matrix = mandelbrot_set(-2, 0.5, -1.25, 1.25)
    fig, ax = plt.subplots(figsize=(10, 10), dpi=720)
    norm = colors.PowerNorm(0.3)
    ax.imshow(matrix.T, cmap="hot", origin="lower", norm=norm)
    plt.show()


if __name__ == "__main__":
    main()
