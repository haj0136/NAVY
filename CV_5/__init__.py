import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import sin, cos, pi

if __name__ == '__main__':
    M1 = 1
    M2 = 1
    L1 = 1
    L2 = 1
    G = 9.8  # m*s**2


    def get_derivative(state, t, l1, l2, m1, m2):

        theta1, velocity1, theta2, velocity2 = state

        upper_part = m2 * G * sin(theta2) * cos(theta1 - theta2) - m2 * sin(theta1 - theta2) * (l1 * velocity1**2 * cos(theta1 - theta2) + l2 * velocity2**2) - (m1 + m2) * G * sin(theta1)
        lower_part = l1 * (m1 + m2 * sin(theta1 - theta2)**2)
        next_velocity1 = upper_part / lower_part

        upper_part = (m1 + m2) * (l1 * velocity1**2 * sin(theta1-theta2) - G * sin(theta2)+ G * sin(theta1) * cos(theta1-theta2)) + m2 * l2 * velocity2**2 * sin(theta1-theta2) * cos(theta1-theta2)
        lower_part = l2 * (m1 + m2 * sin(theta1 - theta2)**2)
        next_velocity2 = upper_part / lower_part

        return velocity1, next_velocity1, velocity2, next_velocity2


    state_0 = np.array([(2 * pi) / 6, 0, (5 * pi) / 8, 0])
    t = np.arange(0, 100, 0.01)

    od = odeint(get_derivative, state_0, t, args=(L1, L2, M1, M2))

    theta1_final = od[:, 0]
    theta2_final = od[:, 2]

    x1 = L1*np.sin(theta1_final)
    y1 = -L1 * np.cos(theta1_final)
    x2 = L1 * np.sin(theta1_final) + L2 * np.sin(theta2_final)
    y2 = -L1 * np.cos(theta1_final) - L2 * np.cos(theta2_final)

    plt.grid()
    plt.scatter(x2, y2, c='red')
    plt.scatter(x1, y1, c='green')

    plt.show()

