import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    LENGTH = 2
    ANGLE = np.pi/8
    stack = []


    def draw_fractal(actual_position, rule, angle, number_of_iterations):
        actual_angle = angle

        for char in rule:
            new_position = [0, 0]
            if char == '+':
                actual_angle += ANGLE

            if char == '-':
                actual_angle -= ANGLE

            if char == '[':
                stack.append([actual_position, actual_angle])

            if char == ']':
                actual_position, actual_angle = stack.pop()

            if char == 'F':
                if number_of_iterations > 1:
                    actual_position = draw_fractal(actual_position, rule, actual_angle, number_of_iterations - 1)
                else:
                    new_position[0] = actual_position[0] + LENGTH * np.cos(actual_angle)
                    new_position[1] = actual_position[1] + LENGTH * np.sin(actual_angle)

                    plt.plot([actual_position[0], new_position[0]], [actual_position[1], new_position[1]])
                    actual_position = new_position

        return actual_position

    first_angle = 0
    square = 'F+F-F-FF+F+F-F'
    snowflake = 'F+F--F+F'
    tree1 = 'F[+F]F[-F]F'
    tree2 = 'FF+[+F-F-F]-[-F+F+F]'

    first_position = [0, 0]

    draw_fractal(first_position, tree2, first_angle, 4)
    plt.axis("equal")
    plt.show()
