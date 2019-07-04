### 6.1

$$
\begin{align}
p(x;\mu,\gamma)=&\frac{e^{-(x-\mu)/\gamma}}{\gamma(1+e^{-(x-\mu)/\gamma})^2}\\
=&\exp(-(x-\mu)/\gamma-2\ln{(1+e^{-(x-\mu)/\gamma})}-\ln\gamma)\\
=&\exp(-\frac{x}{\gamma}-2\ln{(1+e^{-(x-\mu)/\gamma})})\exp(\frac{\mu}{\gamma}-\ln \gamma)
\end{align}
$$

？？？这怎么化成指数分布族的形式

https://stats.stackexchange.com/questions/275773/does-logistic-distribution-belongs-to-exponential-family

![1561696988140](C:\Users\CJ\AppData\Roaming\Typora\typora-user-images\1561696988140.png)

对于离散的情况：
$$
\begin{align}
p(y;w,x)&=(\frac{1}{1+e^{-wx}})^y(\frac{1}{1+e^{wx}})^{1-y}\\
&=\exp(-y\ln(1+e^{-wx})-(1-y)\ln(1+e^{wx}))\\
&=\exp(y\cdot wx)\exp(-\ln(1+e^{wx}))
\end{align}
$$
易得
$$
\begin{align}
\eta&=wx\\
T(y)&=y\\
a(\eta)&=\frac{1}{1+e^{wx}}\\
b(y)&=1
\end{align}
$$


### 6.2



