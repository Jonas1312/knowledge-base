# Metrics

## Classification

[An Overview of General Performance Metrics of Binary Classifier Systems](./Metrics%20of%20Binary%20Classifier%20Systems.pdf)

![](./which-metrics-use.jpg)

## AUROC

- ROC Curves summarize the trade-off between the **true positive rate** and **false positive rate** for a predictive model using different probability thresholds.
- AUROC = Area Under the Receiver Operating Characteristic curve.
- The AUROC of a classifier is equal to the probability that the classifier will rank a randomly chosen positive example higher than a randomly chosen negative example $P(score(x^{+}) \gt score(x^{−}))$ ([source](https://stats.stackexchange.com/a/133435)). A skilful model will assign a higher score to a randomly chosen real positive occurrence than a negative occurrence on average.
- How to train a NN to optimize the AUROC: RL or derivate free methods

## Precision-Recall curve vs ROC curve

- Precision: how often the classifier is correct when it predicts positive $PRE = \frac{TP}{TP+FP}$
- Recall: how often the classifier is correct for all positive instances
- [The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0118432)
- Indeed, ROC is useful when evaluating general-purpose classification, while AUPRC is the superior method when classifying rare events.
- <https://towardsdatascience.com/why-you-should-stop-using-the-roc-curve-a46a9adc728>
- <https://stats.stackexchange.com/questions/7207/roc-vs-precision-and-recall-curves>

## MCC

<https://lettier.github.io/posts/2016-08-05-matthews-correlation-coefficient.html>

## Cosine similarity

Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them.

$$ \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|} $$

- -1 or 1 if vectors are collinear
- cosine similarity between vectors `[2,0,2]` and `[0,1,0]` is 0.

## Confidence Intervals for ML Models

K-cross validation gives a good estimate but no CI...

### CI for an estimated parameter (accuracy)

$$CI = \bar{x} \pm z \frac{s}{\sqrt{n}}$$

- $\bar{x}$ is the sample mean for example.
- $z$ is the confidence level value (1.96 for 95%: $P(-1.96 < Z < 1.96) = 0.95$)
- $s$ sample standard deviation
- $n$ sample size

Accuracy is the number of correct predictions $X = \sum{(\hat{y} == y)}$, divided by the test set size $n$.

We consider each prediction of the model as a Bernouilli trial, and the number of correct predictions $X$ is a random variable following a binomial law $Bin(n,p)$:

- $n$ test set size
- $p$ probability of success, that is prob to have a correct prediction $\hat{y} == y$
- $k$ number of trials

The number of correct predictions is $E[X]= np$, and the variance of the estimate is $\sigma^2 = np(1-p)$.

We want the accuracy to be normalized by the test set size, so we divide the expectation and standard deviation of the random variable $X$ by $n$ (and the variance by $n^2$).

$$\frac{\sigma^2}{n^2} = \frac{1}{n}p(1-p) = \frac{1}{n}ACC(1-ACC)$$

$$\frac{\sigma}{n}=\sqrt{\frac{1}{n}ACC(1-ACC)}$$

We can now compute the CI:

$$CI = ACC \pm z \sqrt{\frac{1}{n}ACC(1-ACC)}$$

### Bootstrap the test set

With replacement of course, 200 bootstraps.

For a 95 CI:

```python
ci_lower = np.percentile(test_accuracies, 2.5)
ci_upper = np.percentile(test_accuracies, 97.5)
```
