import numpy as np


def learn(learn_data):
    k = len(learn_data[0])
    hopfield = np.zeros([k, k])
    for in_data in learn_data:
        np_arr = np.matrix(in_data)
        lesson = np_arr.T*np_arr
        np.fill_diagonal(lesson, 0)
        hopfield = hopfield + lesson
    return hopfield


def normalize(res):
    res[res > 0] = 1
    res[res < 0] = -1
    return res


def predict(hopfield_matrix, sample):
    res = hopfield_matrix * sample.T
    normalize(res)
    print(res)
