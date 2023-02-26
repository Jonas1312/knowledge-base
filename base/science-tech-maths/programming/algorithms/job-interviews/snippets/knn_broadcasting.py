import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mode


def main():
    data = np.array(
        [
            [1, 3],
            [2, 2],
            [3, 3],
            [3, 1],
            [-1, 3],
            [-1, 1],
            [0, 2],
            [1, 1],
            [-1, -1],
            [-1, -2],
            [2, -1],
        ]
    )
    classes = np.array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2])
    k = 2
    print("data shape: ", data.shape)
    print("classes shape: ", classes.shape)

    # scale
    mean = np.mean(data, axis=0)  # (11, 2) -> (2)
    std = np.std(data, axis=0)
    print(mean, std)
    data = (data - mean) / std

    # plt.scatter(data[:, 0], data[:, 1], c=classes)
    # plt.show()

    new_points = np.array([[10, 10], [0, -10], [-5, 5]])

    diff = data - new_points[:, None, :]  # (11, 2) - (3, 1, 2) = (3, 11, 2)
    print("diff: ", diff.shape)

    # norm = np.linalg.norm(diff, axis=-1)  # (3, 11)
    norm = diff[..., 0] ** 2 + diff[..., 1] ** 2
    print("norm: ", norm.shape)
    print(norm)

    # find the k points from "data" with the smallest distance from the current point in "new_points"
    idx = np.argpartition(norm, k, axis=-1)  # (3, 11)
    # Element index to partition by.
    # The k-th value of the element will be in its final sorted position
    # all smaller elements will be moved before it and all equal or greater elements behind it.
    # The order of all elements in the partitions is undefined.
    print("idx: ", idx.shape)  # (3, 11)
    print(idx)
    print(idx[:, :k])  # (3, k)

    nearest_labels = classes[idx[:, :k]]
    print(nearest_labels)  # (3, K)

    labels = mode(nearest_labels, axis=1)[0]
    print(labels)


if __name__ == "__main__":
    main()
