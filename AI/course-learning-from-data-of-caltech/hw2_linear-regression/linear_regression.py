import sys
sys.path.append("..")

import random

import numpy as np

class LinearRegression():

    def __init__(self, data_size, weights=None):
        self.data_size = data_size
        self.p1 = (random.uniform(-1, 1), random.uniform(-1, 1))
        self.p2 = (random.uniform(-1, 1), random.uniform(-1, 1))

        if not weights:
            self.weights = np.array([[0., 0., 0., ]]).T
        else:
            self.weights = weights


    def generate_dataset(self, data_size):
        data_set = [[1., random.uniform(-1, 1), random.uniform(-1, 1)]
                     for i in range(data_size)]
        return data_set

    def target(self, feature):
        x, y = feature[1], feature[2]
        x1, y1 = self.p1
        x2, y2 = self.p2
        slope = (y2 - y1) / (x2 - x1)

        return 1 if y > (slope * (x - x1) + y1) else -1

    def hypothesis(self, feature):
        return np.sign(np.dot(feature, self.weights))

    def training(self):
        self.training_set = self.generate_dataset(self.data_size)

        data_matrix = np.array(self.training_set)
        target_vector = np.array([[self.target(point)] for point in self.training_set])

        pinv= np.linalg.pinv(data_matrix)

        self.weights = np.dot(pinv, target_vector)

        return self.weights

    def testing(self):
        mis_matches = 0
        self.testing_set = self.generate_dataset(self.data_size)

        for feature in self.testing_set:
            if self.hypothesis(feature) != self.target(feature):
                mis_matches += 1

        mis_matches /= float(len(self.testing_set))

        return mis_matches

    def err_in(self):
        mis_matches = 0

        for feature in self.training_set:
            if self.hypothesis(feature) != self.target(feature):
                mis_matches += 1

        mis_matches /= float(len(self.training_set))

        return mis_matches

def one_experiment(data_size):
    lr = LinearRegression(data_size)

    final_weights = lr.training()

    err_test = lr.testing()

    err_in = lr.err_in()

    return final_weights, err_in, err_test

def n_exp(n, data_size):
    avg_err_in = 0
    avg_err_test = 0

    for i in range(n):
        final_weights, err_in, err_test = one_experiment(100)
        avg_err_test += err_test
        avg_err_in += err_in

    avg_err_in /= float(n)
    avg_err_test /= float(n)

    return avg_err_in, avg_err_test


if __name__ == '__main__':
    avg_err_in, avg_err_test = n_exp(1000, 100)

    print("In sample error: {}".format(avg_err_in))
    print("Test error: {}".format(avg_err_test))
