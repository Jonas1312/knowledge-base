# Machine Learning Algorithm Types

![](./machinelearningtypes.jpg)

Pros and cons: [link to PDF](./pros-cons-different-ml-algorithms.pdf)

## Supervised learning

- Each sample is a pair $(x,y)$ where $y$ is the label
- Oracle $p_{Y|X}(y|x)$

We want to learn a function $f$ that mimics the oracle.

### Binary Classification

Goal: find a boundary (hyperplane if linear) that best separates the two classes.

Some algorithms (SVM) also return a confidence score (a point close to the hyperplane has a low score).

### Multi-class Classification

- one-vs-all (one-vs-rest):
  - train one classifier per class (problem of class imbalance)
  - N classifiers for N classes
  - decision: keep highest score (**requires an algorithm that can give a score**)
- one-vs-one:
  - binomial coeff: $\frac{N!}{2!(N-2)!}=\frac{N(N-1)}{2}$ classifiers
  - majority vote

### Regression

The output variable $y$ is a scalar.

### Label Aware Dimensionality Reduction

- LDA: linear discriminant analysis
- GDA: gaussian discriminant analysis
- maximize distance between classes
- minimize distance within classes

## Semi-supervised learning

- sometimes getting the label is expensive
- active sampling (choose label for training)
- Examples:
  - mean teacher
  - VAT
  - pseudo-labelling
  - MixMatch
  - Unsupervised Data Augmentation or UDA
  - Pi-Model

### Learning with not Enough Data

- <https://lilianweng.github.io/posts/2021-12-05-semi-supervised/>
- <https://lilianweng.github.io/posts/2022-02-20-active-learning/>
- <https://lilianweng.github.io/posts/2022-04-15-data-gen/>

### Pseudo-labeling

Use your model trained on training set to get labels on your unlabelled samples.

Take the predictions (hard targets (one-hot coded) or soft targets (predicted probabilities)) and retrain your model.

Soft targets as can give much better results.

Another important detail is the balance between original data and pseudo-labeled data in the resulting dataset. In some experiments 33% of the minibatch was sampled from the pseudolabeled dataset and 67% from the real training set.

## Unsupervised learning

It consists in handling data that are not labelled, no oracle involved.

The only thing we can do is to describe the distribution.

1. dimensionality reduction: PCA, t-SNE, SOMs.
2. membership test: one class svm, autoencoders with reconstruction error, GMMs.
3. representation learning: autoencoders, VAEs, GANs, transformers.
4. clustering: k-means, DBSCAN, GMMs.
5. data visualization: SOMs, t-SNE, PCA.
6. Data estimation and generation: GMMs, VAEs, GANs.

## Put model in production

### Knowledge distillation

Knowledge distillation is a technique in machine learning where a smaller, more compact model is trained to replicate the behavior of a larger, more complex model, by transferring the knowledge learned by the larger model to the smaller model.

The larger model, also called the teacher model, is typically a deep neural network that has been trained on a large dataset to perform a specific task, such as image classification or natural language processing. The smaller model, also called the student model, is usually a simpler version of the teacher model, such as a shallow neural network or a decision tree.

The process of knowledge distillation involves training the student model to predict the same outputs as the teacher model, while also minimizing the difference between the two models' outputs. This can be achieved by using the teacher model's output probabilities as a soft label for the student model during training, instead of using the hard labels from the dataset.

The benefits of knowledge distillation include reducing the size and complexity of models, which can lead to faster inference times and reduced memory usage, while also maintaining or even improving the accuracy of the model. Additionally, knowledge distillation can be used to transfer knowledge learned from pre-trained models to new, smaller models, allowing for faster and more efficient training of new models.

## More

- <https://github.com/ahkarami/Deep-Learning-in-Production>
- <https://madewithml.com/>
- <https://old.reddit.com/r/MachineLearning/comments/sobfvm/p_what_we_learned_by_accelerating_by_5x_hugging/>
- <https://machinethink.net/blog/how-fast-is-my-model/>
