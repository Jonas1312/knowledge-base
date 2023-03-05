# MLE and MAP

## MLE

- MLE: maximum likelihood estimation (MAP with uniform prior)
- is simply a common principled method with which we can derive good estimators, hence, picking $\theta$ such that it fits the data $X$.
- Calculate the likelihood of the data given the model parameters $\theta$.
  - $\hat{\theta}_{MLE}=\underset{\theta}{argmax}(P_{model}(X|\theta))=\underset{\theta}{argmax}(\prod P_{model}(x_{i}|\theta))$ (observations are independent)
  - $=\underset{\theta}{argmax}(log(\prod_{i} P_{model}(x_{i}|\theta)))$
  - $=\underset{\theta}{argmax}(\sum_{i} log(P_{model}(x_{i}|\theta)))$
  - then take the derivative of it with respect to $\theta$ and set it to $0$: $\frac{\partial}{\partial \theta} \sum_{i} log(P_{model}(x_{i}|\theta))=0$
- drawback:
  - higher variance compared to MAP
- benefit:
  - non dependent on prior parametrization
- One way to interpret MLE is to view it as minimizing the "closeness" between the training data distribution $p_{data}(\textbf{x})$ and the model distribution $p_{model}(\textbf{x}, \boldsymbol{\theta})$.
- The best way to quantify this "closeness" between distributions is the KL divergence,
- Maximizing likelihood is equivalent to minimizing KL-Divergence and minimizing cross-entropy!
  - Why does this matter, though?
  - Because this gives MLE a nice interpretation: maximizing the likelihood of data under our estimate is equal to minimizing the difference between our estimate and the real data distribution.
  - We can see MLE as a proxy for fitting our estimate to the real distribution, which cannot be done directly as the real distribution is unknown to us.
  - Minimizing cross-entropy means there's no surprise, we know what to expect

## MAP

- MAP: maximum a posteriori estimation
  - $P(\theta|X) \propto P(X|\theta)P(\theta)$
  - $\hat{\theta}_{MAP}=\underset{\theta}{argmax}(P(X|\theta)P(\theta))$
  - $=\underset{\theta}{argmax}[log(P(\theta)) + log(P(X|\theta))]$
  - What it means is that, the likelihood is now weighted with some weight coming from the prior.
  - if $P(\theta)$ is follows a uniform law => MLE
- Choosing prior $P(\theta)$
  - the less knowledge, the more scattered the distribution (uniform)
  - choosing a good/bad prior can speed up/slow down convergence
  - prior can be interpreted as regularization (useful when few observations)
