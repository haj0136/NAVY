import numpy


def sigmoid_function(z, derivation=False):
    if derivation:
        return z * (1 - z)
    else:
        return 1 / (1 + numpy.exp(-z))


class NeuralNetwork:
    def __init__(self, neuron_layers):
        numpy.random.seed(0)

        self.activity = sigmoid_function
        self.layers = len(neuron_layers)
        self.architecture = neuron_layers
        self.weights = []

        # Random initialization with range of weight values (-1,1)
        for layer in range(self.layers - 1):
            w = 2 * numpy.random.rand(neuron_layers[layer] + 1, neuron_layers[layer + 1]) - 1
            self.weights.append(w)

    def forward(self, x, _weights):
        outputs = x

        for i in range(len(_weights)-1):
            activation = numpy.dot(outputs[i], _weights[i])
            activity = self.activity(activation)

            # add bias unit
            activity = numpy.concatenate((numpy.ones(1), numpy.array(activity)))
            outputs.append(activity)

        # last layer
        activation = numpy.dot(outputs[-1], _weights[-1])
        activity = self.activity(activation)
        outputs.append(activity)

        return outputs

    def weight_adjust(self, y, target, learning_rate):
        error = target - y[-1]
        delta_vector = [error * self.activity(y[-1], derivation=True)]

        for i in range(self.layers-2, 0, -1):
            error = delta_vector[-1].dot(self.weights[i][1:].T)
            error = error*self.activity(y[i][1:], derivation=True)
            delta_vector.append(error)

        delta_vector.reverse()

        for i in range(len(self.weights)):
            layer = y[i].reshape(1, self.architecture[i] + 1)
            delta = delta_vector[i].reshape(1, self.architecture[i + 1])
            self.weights[i] += learning_rate * layer.T.dot(delta)

    def train(self, data, labels, learning_rate=0.1, epochs=100):

        # Add bias units to the input layer
        ones = numpy.ones((1, data.shape[0]))
        Z = numpy.concatenate((ones.T, data), axis=1)
        error = 0

        # loop over training inputs
        for sample in range(Z.shape[0]):
            # forward propagation:
            x = [Z[sample]]
            y = self.forward(x, self.weights)
            target = labels[sample]
            error += abs(target - y[-1])

        for k in range(epochs):
            if (k + 1) % 10000 == 0:
                print('epochs: {}'.format(k + 1))
                print('error: {}'.format(error))

            new_weights = []
            for layer in range(self.layers - 1):
                w = 2 * numpy.random.rand(self.architecture[layer] + 1, self.architecture[layer + 1]) - 1
                w = w * learning_rate
                w = w + self.weights[layer]
                new_weights.append(w)

            test_error = 0
            # fitness func
            for sample in range(Z.shape[0]):

                # forward propagation:
                x = [Z[sample]]
                y = self.forward(x, new_weights)
                target = labels[sample]
                test_error += abs(target - y[-1])

            if abs(test_error) < abs(error):
                self.weights = new_weights
                error = round(test_error[0], 10)

    def predict_single_data(self, x):
        val = numpy.concatenate((numpy.ones(1).T, numpy.array(x)))
        for i in range(0, len(self.weights)):
            val = self.activity(numpy.dot(val, self.weights[i]))
            val = numpy.concatenate((numpy.ones(1).T, numpy.array(val)))
        return val[1]

    def predict(self, X):
        Y = numpy.array([]).reshape(0, self.architecture[-1])
        for x in X:
            y = numpy.array([[self.predict_single_data(x)]])
            Y = numpy.vstack((Y, y))
        return Y
