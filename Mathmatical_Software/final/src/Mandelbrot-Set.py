from pylab import *
from numpy import NaN



def m(a):
    z = 0
    for n in range(1, 100):
        z = z**2 + a
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
xlabel("Mandelbrot Set")
ylabel("maked by luojunxun")
savefig("Mandelbrot-set.png")
show()
