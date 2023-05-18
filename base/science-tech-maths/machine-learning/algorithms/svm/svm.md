# SVM

- linear separator (can be non-linear if use of a kernel)
- not prone to the curse of dimensionality
- not sensitive to outliers
- not prone to overfitting
- we search for the hyperplane that maximizes the margin between two classes
- margin: distance between the hyperplane and the support vectors $=\frac{2}{||w||}$
- we want to find $w$ that maximizes $y_{i}(w^{T}x_{i}+b)\ge 1$
- we want to maximize the margin, that is minimize $||w||$ or $||w||^{2}$ (convex)
- soft margin: maximize $y_{i}(w^{T}x_{i}+b)\ge (1-\xi_{i})$ with $\xi_{i}\ge0$
- $\xi_{i}$ is a **slack variable**
- misclassification when $\xi_{i} > 1$, in the margin when $1\ge\xi_{i}\ge0$
- or minimize $\frac{1}{2}||w||^{2} + C\sum_{i}\xi_{i}$
- $C$ is the penalty error term (positive):
  - $C$ small: soft-SVM
    - large margin
    - tolerates more errors
    - low variance, high bias
  - $C$ big: hard-SVM
    - small margin
    - tolerates no errors (overfitting)
    - low bias, high variance
- the support vectors are the vectors that define the separating hyperplanes ($\alpha_{i} \ne 0$)
- $h(x)=\sum_{i}^{N}\alpha_{i}y_{i}\vec{x_{i}}.\vec{x} + b$
- $k(x, x') = <\varphi(x) ,\varphi(x')>$
- The problem with this scalar product is that it is performed in a large dimensional space, which leads to impractical calculations.
- The kernel trick is therefore to replace a scalar product in a large dimensional space with a kernel function that is easy to calculate. In this way, a linear classifier can easily be transformed into a non-linear classifier. Another advantage of kernel functions is that it is not necessary to specify the transformation φ.
- $K(\mathbf{x},\mathbf{y})=\exp\left(- \frac{\|\mathbf{x} - \mathbf{y}\|^2}{2 \sigma^2}\right)$
- for a function to be a kernel there must exist a function into a feature space such that the function output the same result as the dot product of the projected vectors.

## One class SVM

One-Class SVM is similar

- instead of using a hyperplane to separate two classes of instances
- it uses a hypersphere to encompass all of the instances.
- Now think of the "margin" as referring to the outside of the hypersphere
- so by "the largest possible margin", we mean "the smallest possible hypersphere".

## Infographic

![](./Support%20Vector%20Machines.jpg)

## More

- <https://stats.stackexchange.com/questions/23391/how-does-a-support-vector-machine-svm-work>
- <https://pythonmachinelearning.pro/classification-with-support-vector-machines/>
- <https://github.com/ujjwalkarn/DataSciencePython#support-vector-machine-in-python>
- <https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf>
- <https://web.archive.org/web/20230318045102/http://rvlasveld.github.io/blog/2013/07/12/introduction-to-one-class-support-vector-machines/>
- <http://vxy10.github.io/2016/06/26/lin-svm/>
- <https://sebastianraschka.com/faq/docs/num-support-vectors.html>
- <https://chunml.github.io/ChunML.github.io/tutorial/Support-Vector-Machine/>
- <http://www.statsoft.com/textbook/support-vector-machines>
- <https://www.svm-tutorial.com/2015/06/svm-understanding-math-part-3/>
- <https://cs.stanford.edu/people/karpathy/svmjs/demo/>
- <https://dscm.quora.com/The-Kernel-Trick>
- <https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/>
- <https://fr.wikipedia.org/wiki/Astuce_du_noyau#Contexte_et_principe>
- <https://medium.com/@zxr.nju/what-is-the-kernel-trick-why-is-it-important-98a98db0961d>
- <https://stats.stackexchange.com/questions/323593/how-does-a-one-class-svm-model-work?rq=1>
- <https://towardsdatascience.com/support-vector-machines-soft-margin-formulation-and-kernel-trick-4c9729dc8efe>
- <https://towardsdatascience.com/truly-understanding-the-kernel-trick-1aeb11560769>
