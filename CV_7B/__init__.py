import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def main():
    X = [0]
    Y = [0]
    Z = [0]
    for n in range(200000):
        p = random.uniform(0, 100)
        if p < 1.0:
            x = 0.01*Z[n - 1]
            y = 0.6 * Y[n - 1]
            z = 0.05 * Z[n - 1]
        elif p < 8.0:
            x = 0.2 * X[n - 1] - 0.26 * Y[n - 1] - 0.01 * Z[n-1]
            y = 0.23 * X[n - 1] + 0.22 * Y[n - 1] - 0.07*Z[n-1] + 0.8
            z = 0.07 * X[n - 1] + 0.24 * Z[n-1]
        elif p < 15.0:
            x = -0.25 * X[n - 1] + 0.28 * Y[n - 1] + 0.01 * Z[n-1]
            y = 0.26 * X[n - 1] + 0.24 * Y[n - 1] - 0.07*Z[n-1] + 0.22
            z = 0.07 * X[n - 1] + 0.24 * Z[n-1]
        else:
            x = 0.85 * X[n - 1] + 0.04 * Y[n - 1] - 0.01 * Z[n-1]
            y = -0.04 * X[n - 1] + 0.85 * Y[n - 1] - 0.09*Z[n-1] + 0.8
            z = 0.08 * Y[n-1] + 0.84 * Z[n-1]
        X.append(x)
        Y.append(y)
        Z.append(z)

    fig = plt.figure(figsize=[15, 15])
    ax = plt.axes(projection='3d')
    ax.scatter3D(X, Y, Z, color='g', marker='.')
    plt.show()


if __name__ == "__main__":
    main()
