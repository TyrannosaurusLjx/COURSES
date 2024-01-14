set terminal tikz
set output "1.tex"

set xlabel "$x$ axis"
set ylabel "$y$ axis"
plot [-2:4] [-3:5] x**2-2*x-1,x**2-2*x+1,x**2-2*x+3,0
