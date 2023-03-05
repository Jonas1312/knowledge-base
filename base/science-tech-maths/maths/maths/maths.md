# Maths

## Binomial theorem

$$(a+b)^n = \sum_{k=0}^{n} {n \choose k} a^k b^{n-k} $$

## Binomial coefficient

The binomial coefficient tells us "How many ways are there to get k heads after n tosses?"

## To remember

$$(a+b)^2 = a^2 + 2ab + b^2$$

$$(a-b)^2 = a^2 - 2ab + b^2$$

$$(a+b)(a-b) = a^2 - b^2$$

## Matrices

- Poorly conditioned matrix $A$ is a matrix with a high condition number. $A^{−1}$ amplifies input errors. Small errors (rounding errors) in $x$ can change the output of $A^{−1}x$ rapidly.
- A matrix is ill-conditioned if the conditioning number is very high. What this means is that calculations using this matrix are prone to introduce numerical errors that can overwhelm your calculation. Computers cannot hold an infinite amount of information. Numbers in a floating point representation can only hold so much precision.
- Condition number of a matrix is the ratio of its largest singular value to its smallest singular value.

### Inverse of identity matrix

Itself...

### Eigen

$$Av=\lambda v$$

$$A=V\Delta V^{-1}$$

$$A^{-1}=V\Delta^{-1} V^{-1}$$

$$A^{n}=V\Delta^{n} V^{-1}$$

The largest eigenvector of the covariance matrix always points into the direction of the largest variance of the data, and the magnitude of this vector equals the corresponding eigenvalue.

The second largest eigenvector is always orthogonal to the largest eigenvector, and points into the direction of the second largest spread of the data.

If all eigenvalues of A are:

- positive: the matrix is positive definite.
- positive or zero: positive semi-deﬁnite.
- negative: the matrix is negative definite.

## Derivatives

- the gradient of $f$ is the vector containing all of the partial derivatives
- Hessian is the Jacobian of the gradient. Is symmetric.

### Finite differences

- Taylor
  $$f(x+h)=f(x)+hf'(x)+\frac{h^2}{2}f''(x)+\frac{h^3}{3!}f'''(x)+...$$

- Forward difference
  $$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$$
  $$\frac{f(x+h)-f(x)}{h}=f'(x)+\frac{h}{2}f''(x)$$
  Truncation error: $\mathcal{O}(h)$
- Central difference
  $$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x-h)}{2h}$$
  $$\frac{f(x+h)-f(x-h)}{2h}=f'(x)+\frac{h^2}{3!}f'''(x)$$
  Truncation error: $\mathcal{O}(h^2)$
