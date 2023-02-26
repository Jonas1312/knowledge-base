import numpy as np


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def main():
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
    print(x.shape)  # (4, 2), 4 exemples, 2 dimensions

    y = np.array([[0], [1], [1], [0]])
    print(y.shape)  # (4, 1)

    lr = 1e-1
    hidden = 4
    weights_1 = 2 * np.random.random((x.shape[1], hidden)) - 1  # (2, 4)
    weights_2 = 2 * np.random.random((hidden, 1)) - 1  # (4, 1)
    bias_1 = np.random.randn(hidden)  # (4, )
    bias_2 = np.random.randn(1)  # (1, )

    for _ in range(60000):
        # Forward
        a = x @ weights_1 + bias_1
        b = sigmoid(a)
        c = b @ weights_2 + bias_2
        z = sigmoid(c)
        # error = z - y  # mse

        # Backward
        # d_c = error * z * (1 - z)  # mse
        d_c = -y * (1 - z) + (1 - y) * z  # bce
        d_a = (d_c @ weights_2.T) * b * (1 - b)
        weights_2 -= lr * (b.T @ d_c) / x.shape[0]
        bias_2 -= lr * d_c.mean(axis=0)
        weights_1 -= lr * (x.T @ d_a) / x.shape[0]
        bias_1 -= lr * d_a.mean(axis=0)

    print(
        sigmoid(
            ((sigmoid((np.array([[1, 1]]) @ weights_1) + bias_1)) @ weights_2) + bias_2
        )
    )
    print(
        sigmoid(
            ((sigmoid((np.array([[1, 0]]) @ weights_1) + bias_1)) @ weights_2) + bias_2
        )
    )
    print(
        sigmoid(
            ((sigmoid((np.array([[0, 1]]) @ weights_1) + bias_1)) @ weights_2) + bias_2
        )
    )
    print(
        sigmoid(
            ((sigmoid((np.array([[0, 0]]) @ weights_1) + bias_1)) @ weights_2) + bias_2
        )
    )
    print(
        sigmoid(
            ((sigmoid((np.array([[0, 0.5]]) @ weights_1) + bias_1)) @ weights_2)
            + bias_2
        )
    )


if __name__ == "__main__":
    main()
