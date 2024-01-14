# 二项分布

$$\xi \sim B(n,p)$$

<ol>
<li>$n$是试验次数</li>

<li>$p$是每次试验成功的概率</li>

<li>$P(\xi=k)=C_n^kp^k(1-p)^{n-k}$</li>

<li>$F(x)=P(\xi \leq x)=\sum_{k=0}^{[x]}C_n^kp^k(1-p)^{n-k}$</li>

<li>$E\xi=np$</li>

<li>$Var\xi=D(\xi)=np(1-p)$</li>

<li>特征函数:$f(t)=(1-p+pe^{it})^n$</li>
$here:f(t)=Ee^{it\xi}=\sum\limits_{k=0}^nC_n^kp^kq^{n-k}e^{itk}= \sum\limits_{k=0}^nC_n^k (pe^{it})^k q^{n-k}=( pe^{it}+q )^n$

<li>$let:b(k;n,p)=C_n^kp^kq^{n-k} $
    
<ol>$poisson定理$:$\lim\limits_{n\to\infty}b(k;n,p)=\frac{\lambda^k}{k!}e^{-\lambda}$,其中$\lambda=np_n,n\to\infty$

通常,当p与n无关,但是n很大,p很小,但是np不是很大的时候这个式子可以用于计算对应的二项式的值

</ol>

</ol>

应用场景:在对某一群体做某一数量估计的时候,调查得到单个个体的概率,然后就可以二项分布计算,比如知道一个病的感染率在0.2,讨论一个学校100人会有多少人感染及对应的概率

