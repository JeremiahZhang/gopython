import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

def best_fit_slope(xs, ys):
    m = ((np.mean(xs) * np.mean(ys)) - np.mean(xs*ys)) / \
            (np.mean(xs)**2 - np.mean(xs*xs))

    b = np.mean(ys) - m * np.mean(xs)
    return m, b

def main():
    xs = np.array([1, 2, 3, 4, 5], dtype=np.float64)
    ys = np.array([5, 4, 6, 5, 6], dtype=np.float64)

    m, b = best_fit_slope(xs, ys)
    print("Best fit slope: {} and constant b: {}".format(m, b))

    # plot regression_line
    regression_line = [(m*x) + b for x in xs]

    plt.figure(1)
    plt.scatter(xs, ys, color="#003F72")
    plt.plot(xs, regression_line)
    plt.show()

    # prediction
    predict_x = 7
    predict_y = (m*predict_x) + b
    print("Prediction of x({}) is {}".format(predict_x, predict_y))

    plt.figure(2)
    plt.scatter(xs, ys, color="#003F72", label="data")
    plt.plot(xs, regression_line, label="regression line")
    plt.scatter(predict_x, predict_y, color="green", label="predict_data")
    plt.legend(loc=4)
    plt.show()


if __name__ == '__main__':
    main()
