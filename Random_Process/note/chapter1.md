Bernoulli分布,Poisson分布,正态分布可加性



1.$X\sim B(n,p),Y\sim V(m,p)\Rightarrow X+Y\sim B(m+n,p)$

2.$X\sim P(\lambda),Y\sim P(\mu)\Rightarrow X+Y\sim P(\lambda+\mu)$  

3.$X\sim N(\mu_1,\sigma_1^2),Y\sim N(\mu_2,\sigma_2^2)\Rightarrow X+Y\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$

---

假设$(X,Y)\sim N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho)$

1.$X\sim N(\mu_1,\sigma_1^2),Y\sim N(\mu_2,\sigma_2^2)$

2.给定$X=x$,则$Y\sim N(\mu_2+\rho\frac{\sigma_2}{\sigma_1}(x-\mu_1),\sigma_2^2(1-\rho^2))$

3.X,Y独立$\Leftrightarrow \rho=0$

4.给定$a,b\in R,aX+bY\sim N(\mu,\sigma^2)$

$\Rightarrow \mu = a\mu_1+b\mu_2,\sigma^2=a^2\sigma_1^2+b^2\sigma_2^2+2ab\rho\sigma_1\sigma_2$

___

k阶矩

$EX^k<\infty\Rightarrow EX^k$的$X$的$k$阶矩

___

$X\sim P(\lambda)$ $\Rightarrow$ $EX=\lambda,EX^2=\lambda+\lambda^2$

$EX(X-1)\cdots(X-k+1)=\lambda^k$

由此可以求出$P(\lambda)$的各阶矩

---

$X\sim N(0,\sigma^2)$ $\Rightarrow$ $m_{2k}=(zk-1)!!\sigma^{2k},m_{2k-1}=0$

---

矩母函数
$iG_X(t)=Ee^{tX},|t|<|t_0|:Ee^{tX}<\infty,|t|<t_0$

$X\sim P(\lambda)$ $\Rightarrow$ $G_X(t)=e^{\lambda(e^t-1)}$

$X\sim N(0,\sigma^2)$ $\Rightarrow$ $G_X(t)=e^{\frac{1}{2}\sigma^2t^2}$

---

Chebyshev不等式

$P(|X-\mu|\geq \varepsilon)\leq \frac{\sigma^2}{\varepsilon^2}$

推广为:$f:R\to R^+$为非负单调不减函数,$Ef(X)<\infty$,那么$P(X>\epsilon)\leq \frac{Ef(X)}{f(\epsilon)}$)

---

协方差和相关系数

$Cov(X,Y)=E(X-\mu_X)(Y-\mu_Y)$

$\rho(X,Y)=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}$=$\frac{Cov(X,Y)}{\sqrt{Var(X)Var(Y)}}$

$(X,Y)$的数字特征包括均值向量和协方差矩阵

$\mu=(EX,EY)$,$\Sigma=\begin{pmatrix}Var(X)&Cov(X,Y)\\Cov(Y,X)&Var(Y)\end{pmatrix}$

---

特征函数

$\phi_X(t)=Ee^{itX}$=$\int_{-\infty}^{\infty}e^{itx}dF_X(x),t\in R$

 密度函数$f_X(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-itx}\phi_X(t)dt$

---

 各种收敛

---

极限定理 1

$\{\xi_n\}$独立同分布,$P(\xi_n=1)=p,P(\xi_n=0)=1-p$,令$S_n=\sum\limits_{i=1}^n\xi_i$那么:

1.$(Bernoulli):\frac{S_n}{n}\overset{p}\to p$

2.$(De Moivre-Laplace):\frac{S_n-np}{\sqrt{np(1-p)}}\overset{d}\to N(0,1)$

3.$(Borel):\frac{S_n}{n}\to p,s.e.$

---
 Poisson极限定理

$\forall n,\{\xi_{n,k}\}_{k=1}^n$独立同分布,$P(\xi_{n,k}=1)=p_n,P(\xi_{n,k}=0)=1-p_n,1\leq k\leq n$,
若:$n\to\infty$时,$p_n\to\infty,np_n\to\lambda\in R^+$,令$S_n=\sum\limits_{k=1}^n\xi_{n,k}$,那么:

$$S_n\overset{d}\to \mathcal{P}(\lambda)$$

---


$\{\xi_n\}$独立同分布,令$S_n=\sum\limits_{i=1}^n\xi_i$那么:

1.$(Khintchine):\frac{S_n}{n}\overset{p}\to \mu,a.e.$ $\iff$ $E|\xi_1|<\infty,E\xi=\mu$

2.$(Feller-Levy):\frac{S_n}{\sqrt{n\sigma^2}}\overset{d}\to N(0,1)$ $\iff$ $E\xi_n=0,Var\xi_n=E\xi_n^2=\sigma^2$







