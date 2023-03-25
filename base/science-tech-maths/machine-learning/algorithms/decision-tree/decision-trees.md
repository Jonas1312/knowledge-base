# Decision Trees and Random Forests

## Decision Trees

### Entropy

The entropy $H(X)$ of a random variable $X$ with $n$ possible events that occur with probabilities $p(x_i)$ is defined as:

$$H(X) = E[I(X)]=-\sum_{i}^{n}{p(x_i) * log_2(p(x_i))}$$

**$H$ is maximum when all the $p(x_i)$ are equal (uniform distribution). This is the most uncertain, or 'impure', situation.**

For decision trees, a feature with a lot of different values will be impure.

We start by taking the feature with the highest impurity and we split it.

Why? Because we want to find the class the sample belongs to in a limited number of questions (split nodes).

So at each node, we need to find the best question that is going to halve (if possible) the search space (like in a binary search algorithm). So that's why we start with splitting at the node with highest impurity.

### ID3

Information gain is a measure of how much information is gained by splitting on a particular feature.

As the name implies, information gain measures the amount of information that we gain.

The idea is to subtract from the entropy of our data before the split, the entropy of each possible partition thereafter.

**We then select the split that yields the largest reduction in entropy, or equivalently, the largest increase in information.**

The core algorithm to calculate information gain is called ID3. It's a recursive procedure that starts from the root node of the tree and iterates top-down on all non-leaf branches in a greedy manner, calculating at each depth the difference in entropy:

Identify the partition that leads to the maximum information gain. Create a decision node on that feature and split value.

An alternative to the entropy for the construction of Decision Trees is the Gini impurity.

### Why low bias and high variance?

The tree makes almost no assumptions about target function but it is highly susceptible to variance in data.

If the number of levels is too high i.e a complicated decision tree, the model tends to overfit.

A complicated decision tree (e.g. deep) has low bias and high variance. The bias-variance tradeoff does depend on the depth of the tree.

Decision tree is sensitive to where it splits and how it splits. Therefore, even small changes in input variable values might result in very different tree structure.

if the tree is shallow then we're not checking a lot of conditions/constrains ie the logic is simple or less complex, hence it automatically reduces over-fitting. This introduces more bias compared to deeper trees where we overfit the data.

There are ensemble algorithms, such as bootstrapping aggregation and random forest, which aim to reduce variance at the small cost of bias in decision tree.

### Infographic about decision trees

![](./Decision%20Tree.jpg)

## Random forests

Random Forest is a bagging algorithm rather than a boosting algorithm. They are two opposite way to achieve a low error.

Random forest reduces variance of a large number of "complex" models with low bias. We can see the composition elements are not "weak" models but too complex models

We start by sampling with replacement from a population

For each split of the tree building, we compute the best splitting using only a randomly selected subset of the features. This is another way to ensure that the decision trees are as different as possible.

### Infographic about random forests

![](./Random%20Forest.jpg)

## More

- <https://mlu-explain.github.io/decision-tree/>
- <https://www.analyticsvidhya.com/blog/2016/04/complete-tutorial-tree-based-modeling-scratch-in-python/>
- <https://github.com/ujjwalkarn/DataSciencePython#decision-trees-in-python>
- <https://chunml.github.io/ChunML.github.io/tutorial/Decision-Tree/>
- <https://stackoverflow.com/questions/1859554/what-is-entropy-and-information-gain>
- <https://web.archive.org/web/20210414083548/https://kldavenport.com/pure-python-decision-trees/>
- <https://enlight.nyc/projects/random-forest/>
- <https://towardsdatascience.com/demystifying-entropy-f2c3221e2550>
- <https://victorzhou.com/blog/gini-impurity/>
- <https://stats.stackexchange.com/questions/210829/difference-is-summary-statistics-gini-coefficient-and-standard-deviation>
- <https://en.wikipedia.org/wiki/Gini_coefficient>
- <https://victorzhou.com/blog/information-gain/>
- <https://sebastianraschka.com/pdf/lecture-notes/stat479fs18/06_trees_slides.pdf>
- <https://www.youtube.com/watch?v=g9c66TUylZ4>
- <https://www.youtube.com/watch?v=7VeUPuFGJHk>
- <http://www.oranlooney.com/post/ml-from-scratch-part-4-decision-tree/>
- <https://sebastianraschka.com/faq/index.html#tree-models>
- <https://zerowithdot.com/decision-tree/>
