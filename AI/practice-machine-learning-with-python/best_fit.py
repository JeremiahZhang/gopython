import numpy as np

def best_fit_slope(xs, ys):
    m = ((np.mean(xs) * np.mean(ys)) - np.mean(xs*ys)) / \
            (np.mean(xs)**2 - np.mean(xs*xs))
    return m

def main():
    xs = np.array([1, 2, 3, 4, 5], dtype=np.float64)
    ys = np.array([5, 4, 6, 5, 6], dtype=np.float64)

    m = best_fit_slope(xs, ys)
    print("Best fit slope: {}".format(m))

if __name__ == '__main__':
    main()
