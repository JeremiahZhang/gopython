import numpy as np
import random

class Perceptron:

    def __init__(self, training_size, test_size=None, p1, p2, weights=None):
        self.training_size = training_size
        self.p1 = p1
        self.p2 = p2

        if not test_size:
            self.test_size = training_size
        else:
            self.test_size = test_size

        if not weights:
            self.weights = weights
        else:
            self.weights = np.array([[0., 0., 0.]]).T

    def generate_dataset(self):
        self.data_set = [[1., random.uniform(-1, 1), random.uniform(-1, 1)]
                     for i in range(self.data_size)]
        return self.data_set

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

        training_set = generate_dataset(self.training_size)

        while True:
            for feature in training_set:
                true_label = target(feature)

                if hypothesis(feature) != true_label:
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
        testing_set = generate_dataset(self.test_size)

        for feature in testing_set:
            if hypothesis(feature) != target(feature):
                mis_matches += 1

        mis_matches /= float(self.test_size)

        return mis_matches
