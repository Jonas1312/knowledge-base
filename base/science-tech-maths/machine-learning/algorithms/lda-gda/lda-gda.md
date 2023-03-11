# Linear Discriminant Analysis and Gaussian Discriminant Analysis

## LDA

- The general LDA approach is very similar to a Principal Component Analysis, but in addition to finding the component axes that maximize the variance of our data (PCA), **we are additionally interested in the axes that maximize the separation between multiple classes (LDA).**
- Linear Discriminant Analysis (LDA) is most commonly used as dimensionality reduction technique.
- The goal is to project a dataset onto a lower-dimensional space with good class-separability.
- Both LDA and PCA are linear transformation techniques.
- PCA can be described as an "unsupervised" algorithm, since it "ignores" class labels and its goal is to find the directions (the so-called principal components) that maximize the variance in a dataset.
- In contrast to PCA, LDA is "**supervised**" and computes the directions ("linear discriminants") that will represent the axes that that maximize the separation between multiple classes.
- <https://sebastianraschka.com/Articles/2014_python_lda.html>

## GDA

- QDA is a better option for large data sets, as it tends to have a lower bias and a higher variance.
- On the other hand, LDA is more suitable for smaller data sets, and it has a higher bias, and a lower variance.
