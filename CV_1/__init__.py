import numpy as np
import matplotlib.pyplot as plt
from CV_1.Perceptron import Perceptron

NO_TRAINING_INPUTS = 1000
NO_TESTING_INPUTS = 100
THRESH_HOLD = 50


def fitness_function(x, y):
    result = 2*x + 1
    if y < result:
        return -1
    elif y > result:
        return 1
    else:
        return 0


training_inputs = []
testing_inputs = []
for i in range(NO_TRAINING_INPUTS):
    xy = np.random.randint(-25,25, size=2)
    training_inputs.append(np.array(xy))

labels = np.array([])
for input in training_inputs:
    labels = np.append(labels, fitness_function(input[0], input[1]))

perceptron = Perceptron(2, threshold=THRESH_HOLD)
perceptron.train(training_inputs, labels)


for i in range(NO_TESTING_INPUTS) :
    xy = np.random.randint(-25,25, size=2)
    testing_inputs.append(np.array(xy))


xAxis = np.arange(-25,25,1)
plt.plot(xAxis, 2 * xAxis + 1)
plt.grid()

for x in testing_inputs:
    result = perceptron.predict(x)
    color = "yelow"
    if result == 1:
        color = "green"
    elif result == -1:
        color = "red"

    plt.scatter(x[0], x[1], c=color)
plt.show()
