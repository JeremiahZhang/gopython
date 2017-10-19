import numpy as np
import random

def target(x):
    return np.sin(np.pi * x[0])

class LinearRegression():

    def __init__(self, dataset, target, weights=None):
        self.dataset = dataset
        self.target = target
        if not weights:
            self.weights = np.array([[0., 0.]]).T
        else:
            self.weights = weights

    def hypothesis(self, feature):
        return np.sign(np.dot(feature, self.weights))

    def train(self):
        self.training_set = self.dataset
        data_matrix = np.array(self.training_set)
        target_vector = self.target

        pinv = np.linalg.pinv(data_matrix)
        self.weights = np.dot(pinv, target_vector)

        return self.weights

def run_exp():
    all_weights = []

    training_set = np.array([[random.uniform(-1, 1)] for i in xrange(10000)])
    print("Shape of training_set: {}".format(training_set.shape))
    targets = np.array([[target(point)] for point in training_set])
    print("Shape of target: {}".format(targets.shape))

    for i in xrange(10000):
        subset = random.sample(training_set, 2)
        sample_target = np.array([[target(point)] for point in subset])
        lr = LinearRegression(subset, sample_target)
        lr.train()
        all_weights += [lr.weights.T[0]]

    print("len of all weights list:".format(len(all_weights)))
    g_bar = np.mean(all_weights)
    print(type(g_bar))

    # g_bar precict
    g_bar_targets = np.dot(training_set, g_bar.T)
    print("g_bar_targets shape: ")
    print(g_bar_targets.shape)

    # bias
    bias = np.mean((g_bar_targets - targets) ** 2)

    weights = np.array(all_weights)
    print("weights.shape")
    print(weights.shape)

    # variance
    g_hypo = np.dot(training_set, weights.T)
    print("g_hypo shape")
    print(g_hypo.shape)
    print("len g_hypo")
    print(len(g_hypo))

    variance = []

    for i in xrange(len(g_hypo)):
        g = np.array([g_hypo[:, i]]).T
        variance += [np.mean(g - g_bar_targets) ** 2]

    variance = np.mean(variance)

    return (g_bar, bias, variance)

if __name__ == '__main__':
    g_bar, bias , variance = run_exp()
    print("g bar: {}".format(g_bar))
    print("bias: {}".format(bias))
    print("variance: {}".format(variance))

"""
g bar: 1.41866604832 # q4 choose d, 1.58
bias: 0.267127115438 # q5 choose b: 0.3
variance: 4.78593319556e-06 # q6 choose a: 0.2
[Finished in 2.866s]
"""
