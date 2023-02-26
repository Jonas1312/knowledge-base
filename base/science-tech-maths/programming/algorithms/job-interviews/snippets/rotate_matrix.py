"""le plus élégant c'est d'implémenter trois fonctions
(transpose, invert lines, invert columns) et de les utiliser pour rotater"""

import numpy as np


def main():
    mat = np.arange(25).reshape((5, 5))
    mat_rot = np.rot90(mat.copy(), k=-1)
    print(mat)
    N = mat.shape[0]

    depth = (N - 1) // 2 + 1  # number of sub-matrices
    print("depth: ", depth)

    for d in range(depth):
        if N - 2 * d == 1:  # skip last inner matrix (scalar)
            break
        for step in range(d, N - d - 1):
            # save top
            top = mat[d, step]
            # left to top
            mat[d, step] = mat[N - 1 - step, d]
            # bottom to left
            mat[N - 1 - step, d] = mat[N - 1 - d, N - 1 - step]
            # right to bottom
            mat[N - 1 - d, N - 1 - step] = mat[step, N - 1 - d]
            # restore top to right
            mat[step, N - 1 - d] = top

    print(mat)
    print((mat == mat_rot).all())


if __name__ == "__main__":
    main()
