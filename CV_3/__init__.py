import numpy as np
from CV_3.NeuralNetwork import NeuralNetwork

if __name__ == '__main__':
    LEARNING_RATE = 0.001
    NUMBER_OF_EPOCHS = 100000

    nn = NeuralNetwork([2, 2, 1])

    input_data = np.array([[0, 0], [0, 1],
                           [1, 0], [1, 1]])
    labels = np.array([0, 1,
                       1, 0])

    nn.train(input_data, labels, LEARNING_RATE, epochs=NUMBER_OF_EPOCHS)

    for sample in input_data:
        print(sample, nn.predict_single_data(sample))