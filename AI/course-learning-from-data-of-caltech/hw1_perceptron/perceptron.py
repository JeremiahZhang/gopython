import numpy as np
import random

class Perceptron:

    def __init__(self, data_size, weights=None):
        self.data_size = data_size
        self.p1 = (random.uniform(-1, 1), random.uniform(-1, 1))
        self.p2 = (random.uniform(-1, 1), random.uniform(-1, 1))

        if not weights:
            self.weights = np.array([[0., 0., 0.]]).T
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
        mis_classified = []
        iterations = 0

        training_set = self.generate_dataset(self.data_size)

        while True:
            for feature in training_set:
                true_label = self.target(feature)

                if self.hypothesis(feature) != true_label:
                    mis_classified.append((feature, true_label))

            if not mis_classified:
                break
            else:
                iterations += 1
                x, y = random.choice(mis_classified)
                adapt = np.array([x]).T * y
                self.weights += adapt
                mis_classified = []

        return iterations

    def testing(self):
        mis_matches = 0
        testing_set = self.generate_dataset(self.data_size)

        for feature in testing_set:
            if self.hypothesis(feature) != self.target(feature):
                mis_matches += 1

        mis_matches /= float(len(testing_set))

        return mis_matches

def one_experiment(data_size):
    pp = Perceptron(data_size)
    # data_set = pp.generate_dataset()
    # for data in data_set:
    #     true_label = pp.target(data)
    #     print("True label: {}".format(true_label))
    #     predict = pp.hypothesis(data)
    #     print("Predice: {}".format(predict[0]))

    iterations = pp.training()
    # print("Iterations: {}".format(iterations))

    err_test = pp.testing()
    # print("Test error: {}%".format(err_test * 100))
    return iterations, err_test

def n_experiments(n, data_size):
    avg_iter = 0
    avg_err_test = 0

    for i in range(n):
        iterations, err_test = one_experiment(data_size)
        avg_iter += iterations
        avg_err_test += err_test

    avg_iter /= float(n)
    avg_err_test /= float(n)

    return avg_iter, avg_err_test

if __name__ == '__main__':
    num_experiments = 1000
    data_size = 10

    avg_iter, avg_err_test = n_experiments(num_experiments, data_size)

    print("Dataset(N={0}), avgrage iterations in {1}: {2:0.2f}".format(
        data_size, num_experiments, avg_iter))
    print("Average test error: {0:0.2f}%".format(avg_err_test * 100))

"""
$ python .\perceptron.py
Dataset(N=100), avgrage iterations in 1000: 106
Average test error: 1.35%

$ python .\perceptron.py
Dataset(N=10), avgrage iterations in 1000: 9.34
Average test error: 11.23%
"""
