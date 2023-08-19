# Neural Networks

A neural network is a directed graph:

- weighted connections on the edges
- computational units on the nodes
- Feed forward, no cycles

Created from Perceptron (1962):

- $y=g(w^{T}\phi(x))$, $\phi$ is the **basis function**
- $g(x) = -1$ if $x<0$ else $1$

## SGD

- batch: all training set, slow but accurate
- one sample: many SGD iterations but inaccurate
- SGD (minibatch): fast and more or less accurate
- if Hessian is positive semidefinite $x^{T}Hx \ge 0$ (convex function) all local minima are global minima
  - if **all** eigenvalues(H) > 0: local minima
  - if **all** eigenvalues(H) < 0: local maxima
  - else: saddle point

## Compute neural network gradients

[PDF file](./Computing%20Neural%20Network%20Gradients.pdf)

## Why is the cost function of neural networks non-convex?

The MSE loss $L(y, \hat{y})=\sum_i (y_i- \hat y_i)^2$ is indeed convex in $\hat y_i$.

But if $\hat y_i = f(x_i ; \theta)$ it **may not be convex in $\theta$**, which is the situation with most non-linear models, and we actually care about convexity in $\theta$ because that's what we're optimizing the cost function over. We derive the loss with respect to $\theta$!

A neural network is just a parametric function. It doesn’t necessary means it’s non-convex. A simple example of such a parametric function, just take any 2nd degree polynomial function. It’s still convex, though it’s parametric. Other answers say it’s not convex because it’s not linear. ReLU is not linear and is completely convex.

What makes convex or not convex your network is the problem you’re optimising. If the problem is convex, your network is convex. Then the question is: are problems using deep learning are convex? If you take a random problem (i.e.: a random function) it’s not convex. Experiments showed it’s highly non-convex so no, if problems are usually not convex then networks are not convex.

## Activation functions

- tanh/sigmoid:
  - can have the problem of vanishing gradients
  - slow to compute
- relu:
  - fast to compute
  - <https://zinkx.github.io/posts/relu_guide/>
  - dead relu problem: use LeakyRelu, PRelu, etc.

## Dropout

- drop out units (both hidden and visible) in a neural network with probability $p$
- at test time multiply all the activations by $p$ (or scale by $\frac{1}{p}$ at training)

## BatchNorm

Standardize the activations of every layers to keep the same distribution during training

[Batchnorm notes](./batchnorm/batchnorm.md)

## Deep Learning

- Deep learning algorithms *"only learn superficial clues, not concepts"* diagnoses researcher Yoshua Bengio.
- Deep learning allows the computer to build complex concepts out of simpler concepts
- Deep learning may provide state-of-the-art results, but one does not always understand why, and part of our scientist job remains on explaining why things work
- From a theoretical point of view, deep neural networks are not well understood because of their non-convex properties. Despite many efforts, there are no guarantees of convergence (since we are talking about nonlinear optimization in high-dimensional spaces). Thus, most of the research in this area is experimental and empirical.

## Troubleshooting neural networks

<http://josh-tobin.com/troubleshooting-deep-neural-networks.html>

## Batch size

Set the batch size to maximize the GPU utilization! No need to set it to a power of 2...

- <https://sebastianraschka.com/blog/2022/batch-size-2.html>
- <https://towardsdatascience.com/discontinuity-in-cnn-training-time-with-increase-batch-size-bd2849129283>
- <https://twitter.com/Remi_Coulom/status/1259188988646129665>

Guidelines For Good Performance On Tensor Cores:

- Make sure that the convolution operation is eligible for Tensor Cores by avoiding any combinations of large padding and large filters.
- Transform the inputs and filters to NHWC, pre-pad channel and batch size to be a multiple of 8.

## Model training

- <https://myrtle.ai/learn/how-to-train-your-resnet/>
- <https://github.com/mosaicml/composer>
- <https://www.mosaicml.com/blog/5-best-practices-for-efficient-model-training>
- <https://old.reddit.com/r/MachineLearning/comments/v8rmtj/r_blazingly_fast_computer_vision_training_with/>
- <https://pytorch.org/tutorials/intermediate/memory_format_tutorial.html#performance-gains>
- <https://pytorch.org/blog/how-to-train-state-of-the-art-models-using-torchvision-latest-primitives/>
