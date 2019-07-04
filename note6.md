1. P96加上第三个约束条件后的概率分布是多少？
2. P109的约束条件为什么是“经验概率密度=真实概率密度”，而不是期望相等？
3. 逻辑斯蒂分布属于指数分布族吗？

# 第6章 逻辑斯蒂回归与最大熵模型

## 逻辑斯蒂回归（Logistic Regression）

### 定义

> 惊天骗局！逻辑斯蒂回归是分类模型，而不是回归模型。

$$
\begin{align}
P(Y=1|x)=\frac{\exp(w\cdot x+b)}{1+\exp(w\cdot x+b)}\\
P(Y=0|x)=\frac{1}{1+\exp(w\cdot x+b)}
\end{align}
$$

### 特点

$$
\log{\frac{P(Y=1|x)}{1-P(Y=1|x)}=w\cdot x+b}
$$

​	输出Y=1的对数几率是输入x的线性函数。通过逻辑斯蒂回归模型定义可以将线性函数$w\cdot x+b$转换为概率。

### 模型参数估计

​	对数似然函数为
$$
\begin{align}
L(w)&=\sum_{i=1}^N[y_i\log{\pi(x_i)}+(1-y_i)\log(1-\pi(x_i))]\\
&=\sum_{i=1}^N[y_i\log{\frac{\pi(x_i)}{1-\pi(x_i)}}+\log{1-\pi(x_i)}]\\
&=\sum_{i=1}^N[y_i(w\cdot x_i)-\log(1+\exp(w\cdot x_i)]
\end{align}
$$
​	对于这样的无约束优化问题，可以使用梯度下降法或拟牛顿法求解。

### 多项逻辑斯蒂回归

$$
P(Y=k|x)=\frac{\exp(w_k\cdot x+b)}{1+\sum_{k=1}^{K-1}\exp(w_k\cdot x+b)}\\
P(Y=K|x)=\frac{1}{1+\sum_{k=1}^{K-1}\exp(w_k\cdot x+b)}
$$

## 最大熵模型

​	在上一节中，我们从logistic分布推导出了logistic回归模型。这一节，我们将从最大熵原理出发，推导得到最大熵模型。

### 最大熵原理

- 最大熵原理认为，学习概率模型时，在所有可能的概率模型中，熵最大的模型是最好的模型。
- 直观理解：要选择的概率模型首先必须满足已有的事实，即**约束条件**。在没有更多信息的情况下，那些不确定的部分都是“**等可能的**”。（即不做任何预设）

### 最大熵模型

​	最大熵模型中，用特征函数$f(x,y)​$描述输入x与输出y之间的某一个事实
$$
\begin{equation}
f(x,y)=\left\{ \begin{array}{**lr**} 1,\quad & x与y满足某一事实 \\ 
0, & 否则\\ 
\end{array} \right.
\end{equation}
$$
​	**约束条件**为特征函数关于经验分布$\widetilde{P}(Y|X)$的期望值与关于模型$P(Y|X)$与经验分布$\widetilde{P}(X)$的期望值相等，即
$$
E_p(f_i)=E_{\widetilde{P}}(f_i)\\
E_p(f_i)=\sum_{x,y}{\widetilde{P}(x,y)f(x,y)}\\
E_{\widetilde{P}}(f_i)=\sum_{x,y}{\widetilde{P}(x)P(y|x)f(x,y)}
$$
​	而最优化的**目标**是最大熵，即
$$
\max_{P\in \mathcal{C}}{H(P)=-\sum_{x,y}{\widetilde{P}(x)P(y|x)\log P(y|x)}}
$$
​	由此，我们得到约束最优化问题
$$
\max_{P\in \mathcal{C}}{H(P)=-\sum_{x,y}{\widetilde{P}(x)P(y|x)\log P(y|x)}}\\
s.t.\quad E_p(f_i)=E_{\widetilde{P}}(f_i)\\
\sum_y{P(y|x)}=1
$$
​	通过对偶问题求解原始问题，我们最终可以得到
$$
P_w(y|x)=\frac{1}{Z_w(x)}\exp(\sum_{i=1}^n{w_if_i(x,y)})\\
Z_w(y|x)=\sum_y\exp(\sum_{i=1}^n{w_if_i(x,y)})
$$
​	这个模型的形式与logistic回归模型非常接近，两者都是**对数线性模型**。不同之处在于，最大熵模型引入了特征函数$f(x,y)$。因此，我们可以**将最大熵模型看做是多项logistic回归的推广**。

### 极大似然估计

​	在logistic回归中，我们使用极大似然估计来进行参数估计，那么最大熵模型可以使用这种方法来估计参数吗？答案是肯定的。实际上，**对偶问题的极大化等价于最大熵模型的极大似然估计**。（证明见P102）

​	最大熵模型的对数似然函数为
$$
\begin{align}
L_{\widetilde P}(P_w)&=\log{\prod_{x,y}{P(y|x)^{\widetilde P(x,y)}}}\\
&=\sum_{x,y}{\widetilde P(x,y)\log P(y|x)}\\
&=\sum_{x,y}{\widetilde P(x,y)\sum_{i=1}^n{w_if_i(x,y)}-\sum_x{\widetilde P(x)\log{Z_w(x)}}}
\end{align}
$$

## 模型学习的最优化算法

​	逻辑斯蒂回归模型、最大熵模型学习归结为以似然函数为目标函数的最优化问题，通常通过迭代算法求解，如改进的迭代尺度法、梯度下降法、牛顿法或拟牛顿法。

### 改进的迭代尺度法（IIS）

​	IIS的基本思想：希望找到一个新的参数向量$w+\delta$，使得模型的对数似然函数增大。为了找到适当的$\delta$，IIS优化对数似然改变量$L(w+\delta)-L(w)$的下界。

### 拟牛顿法

​	直接运用拟牛顿法（P441）。