# KNN

KNN is a non-parametric model, which means that it does not make any assumptions about the underlying data.

In the case of a binary classifier (so when we only have 2 classes to predict), k must be odd to avoid having undefined points.

In a multi-class classifier, k can only be 1 if you are to have a defined outcome for each test point.

Why Does Increasing k Decrease Variance in kNN:

- If we take the limit as k approaches the size of the dataset
- we will get a model that just predicts the class that appears more frequently in the dataset (which is actually the Bayes error).
- Donc si on ajoute un peu de bruit dans les points (on bouge les points en 2D par exemple) on aura toujours la même prédiction.
- So if we had some noise in the dataset (e.g. we moved the points in 2D), we would still get the same prediction regardless of the noise.
- High variance algorithms should change their predictions with such noise, but kNN does not.
- Hence kNN with high N is a low variance algorithm.
- This is the model with the highest bias, but the variance is 0 (since our error is invariant of the test data).
- High bias because it has failed to capture any local information about the model, but 0 variance because it predicts the exact same thing for any new data point.

![](./K%20Nearest%20Neighbour.jpg)
