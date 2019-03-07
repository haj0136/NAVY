import numpy as np


class Perceptron(object):

    def __init__(self, no_of_inputs, threshold=50, learning_rate=0.1):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation == 0:
            activation = 0
        elif summation < 0:
            activation = -1
        else:
            activation = 1
        return activation

    def train(self, training_inputs, labels):
        for i in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = (label - prediction)
                self.weights[1:] += self.learning_rate * error * inputs
                self.weights[0] += self.learning_rate * error
            print("Epoch: ", i + 1)
            print("Weights: ", self.weights)