# K-means

- quantization algorithm, known as Linde-Buzo-Gray algorithm
- K is determined by the user of Elbow methods
- It minimizes intra-cluster variance.

Question:

- Does convergence depends on centroids initialization?
- NO, it will always converge.
- The algorithm always converges (by-definition) **but not necessarily to global optimum**.
- The best you can do is to repeat the experiment several times with random starting points.

![](./K-means%20Clustering.jpg)
