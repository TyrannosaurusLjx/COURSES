# 概率空间

## 

#### 概率空间三要素:
1.样本空间$\Omega$,样本点$\omega$的全体;
2.事件域$\mathcal{F}$:满足

<ol>
<li> $\Omega \in \mathcal{F}$ </li>  
<li> 若$A \in \mathcal{F}$,则$A^c \in \mathcal{F}$</li>  
<li> 若$A_1,A_2,\cdots \in \mathcal{F}$,则$\bigcup_{i=1}^{\infty}A_i \in \mathcal{F}$</li>  
</ol>
3.概率$P$:定义在$\mathcal{F}$上的实函数,$A(\in\mathcal{F})
 \rightarrow P(A) $满足
<ol>
<li> (非负性) $P(A) \geq 0$ </li>
<li> (规范性)$P(\Omega) = 1$ </li>
<li> (可列可加性)若$A_1,A_2,\cdots \in \mathcal{F}$,且$A_i \cap A_j = \emptyset(i \neq j)$,则$P(\bigcup_{i=1}^{\infty}A_i) = \sum_{i=1}^{\infty}P(A_i)$</li>

</ol>

#### 概率空间的性质:
1. $P(\emptyset) = 0$
2. $P(A^c) = 1 - P(A)$
3. $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
4. 若$A \subset B$,则$P(B-A)=P(B)-P(A),如若不然P(B-A)=P(B)-P(A\cap B) $
5. 多还少补定理(感觉这个定理没什么用,直接现场推导)
6. 次可加性:$P(\bigcup_{i=1}^{\infty}A_i) \leq \sum_{i=1}^{\infty}P(A_i)$两两无交时取等

#### 概率测度的连续性
如果事件集合$\{A_n\}$极限存在,即$A_n \rightarrow A$,则有$\lim\limits_{n\to\infty}P(A_n)=P(\lim\limits_{n\to\infty}A_n)=P(A)  $
所以我们说概率测度有连续性,它和求极限可交换(积分微分同理)


## 条件概率
$$P(A|B)=\frac{P(AB)}{P(B)} $$

$P(AB)=P(A)P(A|B) $

#### 全概率公式
$$P(A)=\sum_{i=1}^{\infty}P(A|B_i)P(B_i)$$
这里$B_i$是一个完备事件组,即$\bigcup_{i=1}^{\infty}B_i=\Omega$,则表明可以分开计算不同情况下的概率,然后加起来就是总的概率

#### 贝叶斯公式
$$P(B_i|A)=\frac{P(B_i)P(A|B_i)}{\sum_{i=1}^{\infty}P(A|B_i)P(B_i)}$$
 $P(B_i)$称为先验概率,现在A发生了,对$B_i$发生的可能性大小有了新的认识,得到条件概率:$P(B_i|A)$称为后验概率,

### 独立性
$A,B$独立,当且仅当$P(AB)=P(A)P(B)$

多个事件独立性:以三个事件$ABC$举例
<ol>
<li>$P(A)P(B)=P(AB) $
<li>$P(A)P(C)=P(AC) $
<li>$P(B)P(C)=P(BC) $
</ol>
则ABC两两独立,但若说ABC相互独立还需要加上
$P(ABC)=P(A)P(B)P(C)$

#### summary:
    可以讨论试验的独立性,n次独立重复试验就是独立的,但是比如不返回的抽签就是不独立的
    