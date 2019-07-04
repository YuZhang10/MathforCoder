### 7.2



### 7.3

先写出原始问题的拉格朗日函数
$$
\mathcal{L}(w,b,\xi,\alpha,\beta)=\frac{1}{2}\parallel w\parallel^2+C\sum_{i=1}^N{\xi_i^2}-\sum_{i=1}^N{\alpha_i\cdot(y_i(w\cdot x_i+b)-1+\xi_i)}-\sum_{i=1}^N{\beta_i\cdot\xi_i}\\
\alpha_i\geq 0\\
\beta_i \geq 0
$$
对变量求导
$$
\frac{\partial \mathcal{L}}{\partial w}=w-\sum_{i=1}^N{\alpha_iy_ix_i}=0\\
\frac{\partial \mathcal{L}}{\partial b}=-\sum_{i=1}^N{\alpha_iy_i}=0\\
\frac{\partial \mathcal{L}}{\partial \xi_i}=2C\xi_i-\alpha_i-\beta_i=0\\
\frac{\partial \mathcal{L}}{\partial \alpha_i}=-(y_i(wx_i+b)-1+\xi_i)=0\\
\frac{\partial \mathcal{L}}{\partial \beta_i}=-\xi_i=0
$$
整理上式得
$$
w=\sum_{i=1}^N{\alpha_iy_ix_i}\\
\sum_{i=1}^N{\alpha_i y_i}=0\\
\xi_i=\frac{\alpha_i+\beta_i}{2C}
$$
于是可以得到拉格朗日函数的最小值
$$
\begin{align}
\mathcal{L}_{min}=&\frac{1}{2}(\sum_{i=1}^N{\alpha_iy_ix_i})^2+C\sum_{i=1}^N{(\frac{\alpha_i+\beta_i}{2C})^2}\\
&-\sum_{i=1}^N{\alpha_i(y_i((\sum_{j=1}^N{\alpha_jy_jx_j})\cdot x_i+b)-1+\frac{\alpha_i+\beta_i}{2C})}-\sum_{i=1}^N{\beta_i\frac{\alpha_i+\beta_i}{2C}}\\
=&-\frac{1}{2}\sum_{i=1}^N\sum_{j=1}^N{\alpha_i\alpha_jy_iy_j(x_i\cdot x_j)}+\sum_{i=1}^N{\alpha_i}-\frac{1}{4C}\sum_{i=1}^N{(\alpha_i+\beta_i)^2}
\end{align}
$$
将$\max \mathcal{L}_{min}$转化为最小化形式，可得到对偶问题
$$
W(\alpha,\beta)=\frac{1}{2}\sum_{i=1}^N\sum_{j=1}^N{\alpha_i\alpha_jy_iy_j(x_i\cdot x_j)}-\sum_{i=1}^N{\alpha_i}+\frac{1}{4C}\sum_{i=1}^N{(\alpha_i+\beta_i)^2}\\
s.t.\quad \sum_{i=1}^N{\alpha_i y_i}=0\\
\alpha_i\geq0\\
\beta_i\geq0
$$




### 7.4

$$
\begin{align}
\int K(x,z)g(x)g(z)dxdz&=\int \phi(x)\phi(z)g(x)g(z)dxdz\\
&=\int_x {\int_z {\phi(z)dz}\phi(x)dx}\\
&=(\int_{x} \phi(x)dx)^2\\
&\geq 0\\
即K是正定核函数\qquad \#
\end{align}
$$

