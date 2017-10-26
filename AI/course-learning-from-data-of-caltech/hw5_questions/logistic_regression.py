import random
import math

import numpy as np

def gen_dataset(size):
    dataset = [[1., random.uniform(-1, 1), random.uniform(-1, 1)] for i in xrange(size)]
    return dataset

def target(feature, p1, p2):
    x, y = feature[1], feature[2]
    x1, y1 = p1
    x2, y2 = p2
    scope = (y2 - y1)/(x2 - x1)

    return 1 if y > (scope * (x - x1) + y1) else -1

def cross_entropy(feature, label, weights):
    error = math.log(1 + math.exp(-label*np.dot(feature, weights)))
    return error

def gradient(feature, label, weights):
    num = -np.multiply(feature, label)
    return num / (1 + math.exp(label * np.dot(weights, feature)))

def training(size, weights, p1, p2):
    eta = 0.01

    training_set = gen_dataset(size)
    true_label = [target(point, p1, p2) for point in training_set]

    t = 0
    previous_weights = weights

    distance = 1

    while not distance < 0.01:
        idx = random.randint(0, size-1)
        x_feature = np.array(training_set[idx])
        x_label = true_label[idx]

        descent = gradient(x_feature, x_label, weights)
        weights = previous_weights - eta * descent

        distance = np.linalg.norm(previous_weights - weights)
        previous_weights = weights

        t += 1

    return t, previous_weights

def testing(size, weights, p1, p2):
    e_out = 0.0

    testing_set = gen_dataset(size)

    for feature in testing_set:
        true_label = target(feature, p1, p2)
        e_out += cross_entropy(feature, true_label, weights)

    e_out = e_out / float(size)
    return e_out

def main():
    p1 = (random.uniform(-1, 1), random.uniform(-1, 1))
    p2 = (random.uniform(-1, 1), random.uniform(-1, 1))

    weights = [0., 0., 0]
    N = 100
    training_size = 100
    testing_size = 100

    avg_iters = 0.0
    avg_eout = 0.0

    weights = np.array([0., 0., 0.])

    for i in xrange(N):
        iterations, final_weights = training(training_size, weights, p1, p2)
        avg_iters += iterations

        avg_eout += testing(testing_size, final_weights, p1, p2)

    avg_iters /= float(N)
    avg_eout /= float(N)

    print("Average iterations: {}".format(avg_iters))
    print("Average error out of sample: {}".format(avg_eout))

if __name__ == '__main__':
    main()

"""
python logistic_regression.py
Average iterations: 1.0
Average error out of sample: 0.692341732055
There are some problems
"""
