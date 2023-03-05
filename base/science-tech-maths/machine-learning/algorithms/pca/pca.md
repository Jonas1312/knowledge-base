# PCA

- problem statements (same)
  - finding an affine transformation **minimizing the reconstruction error**
  - finding an affine transformation **maximizing the variance of the projections**
- you do not necessarily lose information by reducing the number of dimensions: you just change the representation of the data
- we want the dimensions to be **orthogonal to each other**
- the first principal component vector is a normalized eigenvector associated with the largest eigenvalue of the sample covariance matrix $\tilde{X}\tilde{X}^{T}$
- fraction of variance we want to keep: $\frac{\sum_{i=0}^{r-1}}{\sum_{i=0}^{N-1}}$ keeps $r$ first eigenvalues
- Algorithm:
  - Principal Componentss are the eigenvectors of the covariance matrix of the original dataset
  - covariance matrix is symmetric => eigenvectors are orthogonal
  - big eigenvalue => big variance, we want to keep this dimension
  1) scale data (standardize only)
  2) compute cov matrix
  3) compute eigenvalues/vectors
  4) sort eigenvalues and keep the $K$ highest eigenvalues and corresponding eigenvectors
  5) normalize eigenvectors
  6) compute $X(PC1|PC2|...)$

## Questions

- In what case is a PCA lossless?
- If you **losslessly** reduce your data dimensionality from 3 to 2 with PCA, then one eigenvalue of the covariance matrix must have been zero.
- Remember that a big eigenvalue means there's a lot of variance on this axis.
- So a small eigenvalue means there's no variance on this axis. Thus it's useless.

## More

- <https://sebastianraschka.com/Articles/2015_pca_in_3_steps.html>
- <http://benalexkeen.com/principle-component-analysis-in-python/>
- <https://nbviewer.jupyter.org/github/rasbt/pattern_classification/blob/master/dimensionality_reduction/projection/principal_component_analysis.ipynb>
- <https://github.com/rasbt/pattern_classification/blob/master/dimensionality_reduction/projection/scale_center_pca/scale_center_pca.pdf>
- <http://www.oranlooney.com/post/ml-from-scratch-part-6-pca/>
- <https://sebastianraschka.com/faq/docs/pca-scaling.html>
