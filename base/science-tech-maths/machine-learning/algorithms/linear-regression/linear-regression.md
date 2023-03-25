# Linear Regression

There are four assumptions associated with a linear regression model: (**LHIN** to remember)

- **Linearity**: The relationship between X and the mean of Y is linear. $\hat{y} = \beta_0 + \beta_1x$
- **Homoscedasticity**: The residuals have constant variance (*fitted values minus the actual observed values of Y*). $Var(\epsilon_i) = Var(y_i - \hat{y_i}) = \sigma^2$
- **Independence**: The residuals are independent. In particular, there is no correlation between consecutive residuals in time series data. $Cov(\epsilon_i, \epsilon_j) = 0$
- **Normality**: The residuals of the model are normally distributed. $N(0, \sigma^2)$

In general, you do not need to center or standardize your data for regression. However, if you are using regularization, you should standardize your data.

## Multicollinearity

- Multicollinearity is a phenomenon in which two or more independent variables in a multiple regression model are highly linearly related.
- The interpretation of a regression coefficient is that it represents the mean change in the dependent variable for each 1 unit change in an independent variable **when you hold all of the other independent variables constant**.
- That last portion is crucial for our discussion about multicollinearity.
- When independent variables are correlated, it indicates that changes in one variable are associated with shifts in another variable.
- Multicollinearity generates high variance of the estimated coefficients and hence, the coefficient estimates corresponding to those interrelated explanatory variables will not be accurate in giving us the actual picture. They can become very sensitive to small changes in the model.
- You can detect Multicollinearity using VIF (Variance inflation factor)

## Derive the formula for linear regression

![](./Derivation%20of%20the%20Normal%20Equation%20for%20linear%20regression%20-%20Eli%20Bendersky's%20website.png)

[PDF explanation](./OLS.pdf)

## Infographic

![](./linear%20regression.jpg)

![](./multiple%20linear%20regression.jpg)

## More

- <https://www.dataschool.io/linear-regression-in-python/>
- <https://github.com/ujjwalkarn/DataSciencePython#linear-regression-in-python>
- <https://chunml.github.io/ChunML.github.io/tutorial/Linear-Regression/>
- <http://jakevdp.github.io/blog/2015/07/06/model-complexity-myth/>
- <https://www.hackingnote.com/en/machine-learning/linear-regression>
- <https://enlight.nyc/projects/linear-regression/>
- <https://nbviewer.jupyter.org/github/rasbt/algorithms_in_ipython_notebooks/blob/master/ipython_nbs/statistics/linregr_least_squares_fit.ipynb>
- <https://wiseodd.github.io/techblog/2017/01/05/bayesian-regression/>
