import numpy as np


def main():
    x = np.array([[0, 1], [2, 3], [4, 0], [2, 2], [0, 0]])  # (5, 2)

    centroids = np.array([[0, 1], [2, 0], [3, 4]])  # (3, 2)

    diff = x - centroids[:, np.newaxis, :]
    print("diff shape: ", diff.shape)  # (1,5,2) - (3,1,2) = (3,5,2)

    # norms = np.linalg.norm(diff, axis=-1)  # useless square root
    norms = diff[..., 0] ** 2 + diff[..., 1] ** 2
    print("norms shape: ", norms.shape)  # (3,5)

    classes = np.argmin(norms, axis=0)
    print("classes shape: ", classes.shape)  # (5,)
    print(classes)

    assert (classes == np.array([0, 2, 1, 1, 0])).all()


if __name__ == "__main__":
    main()
