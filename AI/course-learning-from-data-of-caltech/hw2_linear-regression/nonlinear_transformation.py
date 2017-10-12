import random
import numpy as np

def generate_dataset(n):
    data_set =[[1., random.uniform(-1, 1), random.uniform(-1, 1)]
                for i in range(n)]

    return data_set

def noisy_target(data_set, target_vector, noise):
    noisy_points = set()
    data_size = len(data_set)
    noisy_target = target_vector
    num_noise = int(noise * data_size)

    while len(noisy_points) < num_noise:
        idx = random.randint(0, data_size - 1)
        if not idx in noisy_points:
            noisy_target[idx][0] *= -1
            noisy_points.add(idx)

    return noisy_target

def target(feature):
    x1, x2 = feature[1], feature[2]

    return np.sign(x1**2 + x2**2 - 0.6)

def hypothesis(feature, weights):
    return np.sign(np.dot(feature, weights))

def linear_reg(data_set, noise=None):
    training_set = data_set
    data_matrix = np.array(training_set)
    target_vector = np.array([[target(point)] for point in training_set])

    if noise:
        target_vector = noisy_target(data_set, target_vector, noise)

    pinv = np.linalg.pinv(data_matrix)
    final_weights = np.dot(pinv, target_vector)

    return final_weights

def error(data_set, weights):
    mis_matches = 0

    for feature in data_set:
        if hypothesis(feature, weights) != target(feature):
            mis_matches += 1

    mis_matches /= float(len(data_set))

    return mis_matches

def one_experiment(data_size, noise=None):
    training_set = generate_dataset(data_size)
    final_weights = linear_reg(training_set, noise)
    err_in = error(training_set, final_weights)

    return err_in

def n_expeimets(num, data_size, noise=None):
    avg_err_in = 0

    for i in range(num):
        err_in = one_experiment(data_size, noise)
        avg_err_in += err_in

    return avg_err_in/float(num)

def main():
    num = 1000
    data_size = 1000
    noise = 0.1

    avg_err_in = n_expeimets(num, data_size, noise)

    print("Q8: average E_in is {}".format(avg_err_in))
    # 1000 sample, 1000 run times, add noise(10%)
    # Q8: average E_in is 0.514242

if __name__ == '__main__':
    main()
