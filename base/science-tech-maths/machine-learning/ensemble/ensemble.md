# Ensemble

> Different classifiers make up for one another's weaknesses.

Core idea is to handle a set of predictors instead of a single one.

When ensembling, you want to bring together many dissimilar models: it doesn't help much to build a parliament of very similarly thinking people. It would end up in unanimous voting most of the time.

If you do ensembling of neural networks trained from different random initializations, then you will get little performance increase due to low model diversity:

- because the hypothesis space is the same
- if SGD is good enough, it will reach the same global minimum.

Ensembling is interesting when combining different model architectures that are varied in their outputs and their inductive biases.

## Bagging (Bootstrap aggregating)

1. sample a subset $P$ of the dataset $S$ uniformly with replacement (**bootstrapping**)
2. train a predictor on $P$
3. Go back to 1. and train $N$ predictors
4. merge predictions (**aggregating**)

Bagging **reduces variance** in the predictions, thanks to the averaging of the predictions of the individual predictors.

Individual predictors can be trained in parallel!

## Boosting

Iterative process:

1. set equal weights to all samples in dataset $S$ (each sample of a dataset has a weight reflecting the importance given to that sample)
1. train a predictor on $S$ and save it
1. evaluate the predictor on $S$ and compute the error rate $e$
1. if a sample has been wrongly classified, increase the weight of this sample
1. train a second predictor with the new weights
1. repeat N times
1. make a **weighted averaging** of the individual predictions. The weight of each predictor is proportional to its accuracy on the weighted training set.

Boosting aims at reducing the bias of a large number of "small" models with low variance but high bias. They are "weak" models.

## Infographic

[PDF doc](./ML_cheatsheets_10.pdf)

## More

- <https://stats.stackexchange.com/questions/18891/bagging-boosting-and-stacking-in-machine-learning>
- <https://github.com/ujjwalkarn/DataSciencePython#random-forest-with-python>
- <https://web.archive.org/web/20210924023432/https://mlwave.com/kaggle-ensembling-guide/>
- <https://www.overkillanalytics.com/more-is-always-better-the-power-of-simple-ensembles/>
- <https://victorzhou.com/blog/intro-to-random-forests/>
- <http://www.chioka.in/which-is-better-boosting-or-bagging/>
- <https://towardsdatascience.com/ensemble-methods-bagging-boosting-and-stacking-c9214a10a205>
- <https://towardsdatascience.com/advanced-ensemble-classifiers-8d7372e74e40>
- <https://sebastianraschka.com/pdf/lecture-notes/stat479fs18/07_ensembles_slides.pdf>
- <https://jhui.github.io/2017/01/15/Machine-learning-Decision-tree-random-forest-Ensemble-methods/>
- <https://quantdare.com/what-is-the-difference-between-bagging-and-boosting/>
- <http://blog.kaggle.com/2016/12/27/a-kagglers-guide-to-model-stacking-in-practice/>
