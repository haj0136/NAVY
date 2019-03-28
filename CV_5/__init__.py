import numpy as np
from scipy.integrate import odeint
import math

if __name__ == '__main__':

    M1 = 5
    M2 = 10
    L1 = 20
    L2 = 10
    G = 9.8  # m*s^2

    def get_derivative(state, t, l1, l2, m1, m2):
        theta1, velocity1, theta2, velocity2 = state

        next_velocity1 = m2*G*math.sin(velocity2)*math.cos(velocity1-velocity2)
        next_velocity2 = 0

        return theta1, next_velocity1, theta2, next_velocity2

    state = np.array((2*math.pi)/6, 0, (5*math.pi)/8, 0)
    t = np.arange(0, 100, 0.1)

    od = odeint(get_derivative, t, args=(L1, L2, M1, M2))
