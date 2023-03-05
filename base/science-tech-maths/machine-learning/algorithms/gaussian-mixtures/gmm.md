# GMM

- **a Bayesian generalization of K-means**
- Though GMM is often categorized as a clustering algorithm, **fundamentally it is an algorithm for density estimation**.
- That is to say, the result of a GMM fit to some data is technically not a clustering model, but a generative probabilistic model describing the distribution of the data.

## GMM vs K-means

- K-means drawbacks:
  - no probabilities
  - circular clusters (need to standardize the data)
- GMM:
  - confidence score with probabilities
  - clusters can overlap
  - elliptical sizes
  - can be used as a density estimator, model the distribution of the input data in order to generate new data
  - GMMs usually tend to be slower than K-Means because it takes more iterations of the EM algorithm to reach the convergence.
  - They can also quickly converge to a local minimum that is not a very optimal solution. To avoid this issue, GMs are usually initialized with K-Means.

## Expectation maximization algorithm

The goal of the EM algorithm is to find a maximum to the likelihood function $p(X|\theta)$ wrt parameter $\theta$, when this expression or its log cannot be discovered by typical MLE methods. Used for estimating hidden variables

E-step: evaluate using current parameters

M-step: re-estimate the parameters

- E-step: for each point, find weights encoding the probability of membership in each cluster:
  - for the gaussian $j$ and point $x_{i}$:
  - $W_{j}^{(i)} = \frac{\phi_{j}\mathcal{N}_{\mu_{j}, \Sigma_{j}}(x^{(i)})}{\sum_{q=1}^{N}\phi_{q}\mathcal{N}_{\mu_{q}, \Sigma_{q}}(x^{(i)})}$
  - $W_{j}^{(i)}$, $x_{i}$ lines, $j$ columns, contains probabilities for each point
- M-step: for each cluster, update its location, normalization, and shape based on all data points, making use of the weights computed in the E-step:
  - update $\mu, \Sigma, \phi_{i}$:
  - $\phi_{j}=\frac{1}{N}\sum_{i=1}^{N}W_{j}^{(i)}$
  - $\mu_{j} = \frac{\sum_{i=1}^{N}W_{j}^{(i)}x^{(i)}}{\sum_{i=1}^{N}W_{j}^{(i)}}$
  - $\Sigma_{j}=\frac{\sum_{i=1}^{N}W_{j}^{(i)}(x^{(i)}-\mu_{j})(x^{(i)}-\mu_{j})^{T}}{\sum_{i=1}^{N}W_{j}^{(i)}}$

You can constraint the covariance matrix:

- diagonal
- spherical
- full

## More

- <https://pythonmachinelearning.pro/clustering-with-gaussian-mixture-models/>
- <https://jakevdp.github.io/PythonDataScienceHandbook/05.12-gaussian-mixtures.html>
- <https://towardsdatascience.com/gaussian-mixture-models-d13a5e915c8e>
- <https://towardsdatascience.com/how-to-code-gaussian-mixture-models-from-scratch-in-python-9e7975df5252>
- <http://www.oranlooney.com/post/ml-from-scratch-part-5-gmm/>
