# Probabilities and Statistics

## Random variables

- A random variable is a variable holding an outcome or the result of some outcomes in a random process e.g. the observed value in rolling a die. Associatse possible outcomes with probabilities. toss/flip a fair coin, roll a die
- *i.i.d*: independent and identically distributed: they follow the same distribution and are independent

## Probability distributions

- for continious probabilities there's no "probabilities", but rather probability density
- $P_{Z}(A) = \int_{A}^{}p_{Z}(z)dz$ where $p_{Z}(z)$ is the probability density function of $Z$
- probability distribution : the process of sampling from a given process an infinite number of times, it gives a smooth histogram

## Independence, Marginalization, Conditioning and Chain rule

independence: if $X$ and $Y$ are independent, then $P(X,Y)=P(X)P(Y)$

marginalization (over $Y$): $P(X)=\sum_{y}P(X,Y=y)=\sum_{y}P(X|Y=y)P(y)$

conditionning: $P(X,Y) = P(X|Y)P(Y)$ [(more info here)](https://en.wikipedia.org/wiki/Conditional_probability)

- $P(X|Y)=\frac{P(X,Y)}{P(Y)}$
- $P(X|Y)$ is the probability of $X$ given $Y$, i.e. the probability of $X$, given that $Y$ has already occurred.
- So we need to look at the space where $X$ and $Y$ overlap, i.e. $P(X,Y)$.
- $P(Y)$ is a normalizing factor, to make sure that the probabilities sum to $1$. It is the probability of $Y$, regardless of $X$.

chain rule: $P(A,B,C,D)=P(A|B,C,D)P(B|C,D)P(C|D)P(D)$

## Gaussian law

- $\mathbb{P}(\mu-\sigma \le x \le \mu+\sigma) \approx 68\%$
- $\mathbb{P}(\mu-2\sigma \le x \le \mu+2\sigma) \approx 95\%$
- $\mathbb{P}(\mu-3\sigma \le x \le \mu+3\sigma) \approx 99\%$

## Percentile

Having a 25% percentile means that 25% of the data is below that value.

## Variance, SD, Covariance and Correlation

- variance: $Var(X) = \sigma_X^2 = E[(X-E[X])^2] = E[X^2] - E[X]^2$
- standard deviation: $\sigma_X = \sqrt{Var(X)}$
- covariance: $Cov(X,Y) = E[(X-E[X])(Y-E[Y])] = E[XY] - E[X]E[Y]$
- correlation: $Corr(X,Y) = \frac{Cov(X,Y)}{\sigma_X\sigma_Y} = \frac{Cov(X,Y)}{\sqrt{Var(X)Var(Y)}}$
  - having a high correlation doesn't mean that the variables are dependent, it just means that they are related.
  - also, having a low correlation doesn't mean that the variables are independent, since correlation is a measure of linear dependence. There can be other types of dependence that are not captured by correlation.

## Interview questions

- estimator of the mean: $E(\bar{X}) = E(\frac{X_1 + ... + X_n}{n}) = \frac{1}{n}[E(X_1) + ... + E(X_n)] = \frac{1}{n}(\mu_1 + ... + \mu_n) = \frac{1}{n}n \mu = \mu$
- of variance: $Var(\bar{X})=\text{Var}\left(\frac{\sum_{i=1}^n X_i}{n}\right) = \frac{1}{n^2}\text{Var}\left(\sum_{i=1}^n X_i\right) = \frac{1}{n^2}\sum_{i=1}^n\text{Var}\left(X_i\right)  = \frac{1}{n^2} n\sigma^2 = \frac{\sigma^2}{n}$

### Generate random values with custom distribution

![](./pdf-cdf.gif)

- Get the cumulative distribution function (CDF)
- Mirror the CDF along y = x
- Apply the resulting function to a uniform value between 0 and 1

### Monty Hall problem

- 3 doors closed
- behind one door a car
- behind two other doors goats
- you pick one door, this door has 1/3 chance to have a car behind it, and the other two doors have 2/3 chance to have a car behind them
- then a guy opens a door with a goat
- should you pick the other door?
- YES, cause you have 1/3 chance to have a car with the first door you picked
- but 2/3 with the other doors
- the fact that one door is opened now doesn't change the 2/3 probability

### Fair coin from unfair coin

![](./fair-coin-from-biased-coin.png)

## More

- <https://www.simonwardjones.co.uk/posts/probability_distributions/>
- <https://www.simonwardjones.co.uk/posts/bayesian_inference/>
- <https://longintuition.com/2020/07/20/max-entropy-intuition.html>
- <https://seeing-theory.brown.edu/index.html#firstPage>
