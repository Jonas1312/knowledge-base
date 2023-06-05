# Confidence Intervals

![](95%20CI%20Confidence%20Intervals.png)

## Wrong Interpretation

When reporting a CI:

- “I am 95% confident that the mean is between 25.1 and 32.6” is correct.
- “There is a 95% probability that the mean is between 25.1 and 32.6” is **WRONG**. Either μ is in that interval or not; there is no probability associated with it.

First, let’s assume we have access to the population. *(This is, of course, never the case. Otherwise, we wouldn’t have to estimate a parameter but could compute it precisely.)*

Then, if we draw a very large number of samples from the distribution, and apply our confidence interval method to these samples, 95% of the confidence intervals would contain the actual value.

![](ci-viz.png)

A confidence interval is an interval associated with a parameter and is a frequentist concept. The parameter is assumed to be non-random but unknown, and the confidence interval is computed from data.

Because the data are random, the interval is random. A 95% confidence interval will contain the true parameter with probability 0.95. That is, with a large number of repeated samples, 95% of the intervals would contain the true parameter.

## Statistical Significance

The difference of two measurements is statistically significant if confidence intervals **do not overlap**.

However we cannot say that results are not statistically significant if confidence **intervals overlap**.
