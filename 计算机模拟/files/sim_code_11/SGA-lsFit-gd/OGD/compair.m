hold off;
xi = 0:0.01:10;
plot(xi, objfunc(w, xi), 'LineWidth',2);
hold on;
s = floor(m / 100);
plot(x(1:s:end), y(1:s:end), 'r*');