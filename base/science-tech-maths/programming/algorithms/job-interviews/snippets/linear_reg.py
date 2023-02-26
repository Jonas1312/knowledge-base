import matplotlib.pyplot as plt
import numpy as np


def grad_descent():
    x = np.arange(0, 100, 1)[:, np.newaxis]
    y = x * 3.14 + 22
    y += 5 * np.random.randn(*x.shape)
    print(y.shape)

    norm_factor = np.max(np.abs(x))
    x = x / norm_factor
    y = y / norm_factor

    plt.plot(x, y)
    plt.show()

    # add bias
    x = np.hstack((x, np.ones_like(x)))
    print(x.shape)

    w = np.random.randn(2, 1)
    print(w.shape)

    lr = 0.005
    for _ in range(100000):
        y_pred = x @ w  # (100, 2) @ (2, 1)
        # grad = np.mean(-2 * (y - y_pred) * x, axis=0)[:, np.newaxis]
        grad = -2 * x.T @ (y - y_pred)  # (100, 2).T @ (100, 1)
        w -= lr * grad

    print(w[0])
    print(w[1] * norm_factor)


if __name__ == "__main__":
    grad_descent()
