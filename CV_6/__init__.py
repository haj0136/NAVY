import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    LENGTH = 2
    ANGLE = np.pi/2
    stack = []

    dragonX = 'X+YF+'
    dragonY = '-FX-Y'
    hilbert_curveX = '-YF+XFX+FY-'
    hilbert_curveY = '+XF-YFY-FX+'


    def draw_fractal(actual_position, rule, angle, number_of_iterations, number_of_rewrites):
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

            if char == 'X' and number_of_rewrites > 0:
                actual_position, actual_angle = draw_fractal(actual_position, hilbert_curveX, actual_angle, number_of_iterations, number_of_rewrites - 1)

            if char == 'Y' and number_of_rewrites > 0:
                actual_position, actual_angle = draw_fractal(actual_position, hilbert_curveY, actual_angle, number_of_iterations, number_of_rewrites - 1)

            if char == 'F':
                if number_of_iterations > 1:
                    actual_position = draw_fractal(actual_position, rule, actual_angle, number_of_iterations - 1, number_of_rewrites)
                else:
                    new_position[0] = actual_position[0] + LENGTH * np.cos(actual_angle)
                    new_position[1] = actual_position[1] + LENGTH * np.sin(actual_angle)

                    plt.plot([actual_position[0], new_position[0]], [actual_position[1], new_position[1]])
                    actual_position = new_position

        return actual_position, actual_angle

    first_angle = 0
    square = 'F+F-F-FF+F+F-F'
    snowflake = 'F+F--F+F'
    tree1 = 'F[+F]F[-F]F'
    tree2 = 'FF+[+F-F-F]-[-F+F+F]'
    dragon = 'FX'
    hilbert_curve = 'X'


    # plt.figure(dpi=200)

    first_position = [0, 0]

    draw_fractal(first_position, hilbert_curve, first_angle, 1, 5)
    plt.axis("equal")
    plt.show()
