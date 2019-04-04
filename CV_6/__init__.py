import numpy as np

if __name__ == '__main__':

    stack = []

    def draw_fractal(rule, angle, number_of_iterations):
        actual_angle = 0

        new_possition = [0, 0]

        for char in rule:
            if char == '+':
                actual_angle += angle

            if char == '-':
                actual_angle -= angle

            if char == '[':

            if char == ']':

            if char == 'F':


    first_angle = np.pi/2
    square = 'F+F-F-FF+F+F-F'
    snowflake = 'F+F--F+F'
    tree1 = 'F[+F]F[-F]F'
    tree2 = 'FF+[+F-F-F]-[-F+F+F]'

