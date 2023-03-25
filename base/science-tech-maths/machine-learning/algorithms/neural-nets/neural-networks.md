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

## Activation functions

- tanh/sigmoid: vanishing gradients
- relu: dead relu, use LeakyRelu, PRelu, ...
- exploding gradients: gradient clipping

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
