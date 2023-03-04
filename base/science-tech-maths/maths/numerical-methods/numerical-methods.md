# Find f(x) = 0

## Bisection method

- <https://fr.wikipedia.org/wiki/M%C3%A9thode_de_dichotomie>

## Newton method

- <https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Newton>

We start at point $x_0$ (as close as possible to the solution).

From Taylor 1st order:
$$f'(x_0) \simeq \frac{f(x) - f(x_0)}{x-x_0}$$

We want to find $x$ such as $f(x)=0$

$$0= f(x_0) + f'(x_0)(x-x_0)$$

thus:

$$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$
