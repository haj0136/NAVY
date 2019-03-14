import numpy as np
import matplotlib.pyplot as plt
import sys  # For printing

NO_TRAINING_INPUTS = 4
NO_TESTING_INPUTS = 100
THRESH_HOLD = 30000
LEARNING_RATE = 0.01
# The parameter to help with overfitting.
REG_PARAM = 0.00

NO_I_NEURONS = 2  # Number of Input units
NO_H_NEURONS = 2  # Number of Hidden units
NO_O_NEURONS = 1  # Number of Output units


def sigmoid_function(z, derivation=False):
    if derivation:
        return z * (1 - z)
    else:
        return 1 / (1 + np.exp(-z))


training_inputs = np.array([[0, 1],
                            [1, 0],
                            [1, 1],
                            [0, 0]])
labels = np.array([[1],
                   [1],
                   [0],
                   [0]])

np.random.seed(1)
W1 = np.random.normal(0, 1, (NO_H_NEURONS, NO_I_NEURONS))
W2 = np.random.normal(0, 1, (NO_O_NEURONS, NO_H_NEURONS))
B1 = np.random.random((NO_H_NEURONS, 1))
B2 = np.random.random((NO_O_NEURONS, 1))


def forward(x, predict=False):
    input_vector = x.reshape(x.shape[0], 1)

    net1 = W1.dot(input_vector) + B1
    out1 = sigmoid_function(net1)

    net2 = W2.dot(out1) + B2
    out2 = sigmoid_function(net2)

    if predict:
        return out2
    return (input_vector, out1, out2)




def train(_W1, _W2, _B1, _B2):  # The arguments are to bypass UnboundLocalError error
    for i in range(THRESH_HOLD):
        c = 0

        dW1 = 0
        dW2 = 0

        dB1 = 0
        dB2 = 0

        for j in range(NO_TRAINING_INPUTS):
            sys.stdout.write("\rIteration: {} and {}".format(i + 1, j + 1))

            # Forward Prop.
            a0 = training_inputs[j].reshape(training_inputs[j].shape[0], 1)  # 2x1

            z1 = _W1.dot(a0) + _B1  # 2x2 * 2x1 + 2x1 = 2x1
            a1 = sigmoid_function(z1)  # 2x1

            z2 = _W2.dot(a1) + _B2  # 1x2 * 2x1 + 1x1 = 1x1
            a2 = sigmoid_function(z2)  # 1x1

            # Back prop.
            dz2 = a2 - labels[j]  # 1x1
            dW2 += dz2 * a1.T  # 1x1 .* 1x2 = 1x2

            dz1 = np.multiply((_W2.T * dz2), sigmoid_function(a1, derivation=True))  # (2x1 * 1x1) .* 2x1 = 2x1
            dW1 += dz1.dot(a0.T)  # 2x1 * 1x2 = 2x2

            dB1 += dz1  # 2x1
            dB2 += dz2  # 1x1

            c = c + (-(labels[j] * np.log(a2)) - ((1 - labels[j]) * np.log(1 - a2)))
            sys.stdout.flush()  # Updating the text.

        _W1 = _W1 - LEARNING_RATE * (dW1 / NO_TRAINING_INPUTS) + ((REG_PARAM / NO_TRAINING_INPUTS) * _W1)
        _W2 = _W2 - LEARNING_RATE * (dW2 / NO_TRAINING_INPUTS) + ((REG_PARAM / NO_TRAINING_INPUTS) * _W2)

        _B1 = _B1 - LEARNING_RATE * (dB1 / NO_TRAINING_INPUTS)
        _B2 = _B2 - LEARNING_RATE * (dB2 / NO_TRAINING_INPUTS)

    return (_W1, _W2, _B1, _B2)


dW1 = 0
dW2 = 0

dB1 = 0
dB2 = 0


W1, W2, B1, B2 = train(W1, W2, B1, B2)


for x in training_inputs:
    print("\n")
    print(x)
    print(forward(x, predict=True))


