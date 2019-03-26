from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Flatten, Dropout
from keras.optimizers import SGD
import numpy as np


if __name__ == '__main__':

    def chaos_function(x, a):
        x1 = x * a * (1 - x)
        return x1

    def generate_inputs(number_of_inputs, a):
        inputs = np.array([[x0, a]])
        for i in range(0, number_of_inputs):
            new_arr = np.array([chaos_function(inputs[i][0], a), a])
            inputs = np.vstack((inputs, new_arr))

        return inputs

    def generate_labels(number_of_inputs):
        inputs = np.array([[0.6]])
        for i in range(0, number_of_inputs):
            new_arr = np.array([0.6])
            inputs = np.vstack((inputs, new_arr))

        return inputs

    # A = [2.5, 3.3, 4.0]
    a = 2.5
    x0 = 0.1
    X = generate_inputs(10, a)
    # labels = np.array([[0.6], [0.47943, 0.8236], [0]])
    labels = generate_labels(10)

    model = Sequential()
    model.add(Dense(16, activation='sigmoid', input_dim=2))
    model.add(Dense(1, activation='sigmoid'))

    sgd = SGD(lr=0.1)
    model.compile(optimizer=sgd, loss='mean_squared_error')

    model.fit(X, labels, batch_size=1, epochs=1000, verbose=0)
    print(model.predict(np.array([[0.1, a]])))


