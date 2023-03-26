# Hypothesis testing

- p-value = $P(X | H_0)$
  - too small: we reject $H_0$. It doesn't mean that $H_0$ is false, it just means that we don't have enough evidence to support it.
  - too big: $H_0$ cannot be rejected
- a Type I error refers to the action of rejecting the null hypothesis, while it actually holds true (it is not-null)
- a Type II error refers to the rejection of the alternative (non-null) hypothesis, while in fact it is true
- making a Type I/II error in a medical setting may not be the same as testing the results of a marketing survey in the fashion industry.
- accepting the hypothesis that a certain drug treatment is effective against cancer when in fact it is not (Type II) error may result in severe consequences vs another scenario (say advertisement) in which the degree of impact of the decisions being made as a result of the analysis is orders of magnitude lower.

## More

Interpret p-values: <https://blog.minitab.com/blog/adventures-in-statistics-2/how-to-correctly-interpret-p-values>

## Example

Let's say we have events coin flips: 1 head and 9 tails. We want to test the hypothesis that the coin is fair.

We can use the binomial distribution to calculate the probability of getting 1 head out of 10 flips.

Binomial law:

$$f_X(x) = \binom{n}{x} p^x (1-p)^{n-x}$$

We have $n=10$ and $p=0.5$ since the coin is fair.

We want to calculate the probability of getting 1 head out of 10 flips.

$$\binom{10}{1} 0.5^1 (1-0.5)^{10-1} = \frac{10!}{1!9!} 0.5 (0.5)^{9} = 10 \times 0.5^{10} = 0.01$$

The probability of getting 1 head out of 10 flips is 1%. This is the p-value. The probability of the null hypothesis (fair coin) being true.

Since the p-value is less than 5%, we reject the null hypothesis and conclude that the coin is not fair.
