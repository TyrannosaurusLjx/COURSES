# 几何分布

$\xi$的取值为正整数,并且相应的概率为:$P(\xi=k)=pq^{k-1} ,p+q=1$

在伯努利概型中,直到首次成功的试验次数就服从几何分布

<ol>

<li>特征函数$f(t)=\frac{pe^{it}}{1-qe^{it}} $

$here:f(t)=\sum\limits_{k=1}^\infty pq^{k-1}e^{itk}=\frac{p}{q}\sum\limits_{k=1}^\infty (qe^{it})=\frac{p}{q}\lim\limits_{k\to\infty} \frac{qe^{it}(1-q^ke^{itk})}{1-qe^{it}}=\frac{pe^{it}}{1-qe^{it}}$
</li>

<li>无记忆性,即$P(\xi>n+m|\xi>n)=P(\xi>m)$

</ol>

