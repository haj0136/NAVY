import numpy as np
import CV_3B.Hopfield as Hopfield


if __name__ == '__main__':

    train_inputs = [[1, -1, 1, -1, 1, -1],
                    [-1, 1, -1, 1, -1, 1]]
    test_input = np.matrix([1, 1, 1, 1, -1, 1])

    hopfield_matrix = Hopfield.learn(train_inputs)

    Hopfield.predict(hopfield_matrix, test_input)

