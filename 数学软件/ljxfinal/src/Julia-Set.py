from pylab import *
from numpy import NaN


c = complex(input('输入参数c的值'))


def m(z):
    global c
    for n in range(1, 100):
        z = z**5 + c
        if abs(z) > 2:
            return n
    return NaN


X = arange(-2, 2, .002)
Y = arange(-1, 1, .002)
Z = zeros((len(Y), len(X)))


for iy, y in enumerate(Y):
    for ix, x in enumerate(X):
        Z[iy,ix] = m(x + 1j * y)


imshow(Z, cmap = plt.cm.prism, interpolation = 'none', extent = (X.min(), X.max(), Y.min(), Y.max()))
xlabel("Julia Set")
ylabel("maked by luojunxun")
savefig("julia with c = {}.eps".format(c))
show()
