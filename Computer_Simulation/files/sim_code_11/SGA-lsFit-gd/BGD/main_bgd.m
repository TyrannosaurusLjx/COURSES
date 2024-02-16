clear; clc;

% let h(x) = w(1) + w(2)*x + w(3)*x^2 approximate y(x) = x^2 + noise on [0,10]
realfunc = @(x) x.*x;
m = 1000;
noise = randn(m, 1);
x = 10 * rand(m, 1);
y = realfunc(x) + 0.1 * noise;

w = rand(1,3);  % w = [0; 1.00; 0.00];
resfunc  = @(w,x,y) (w(1) + w(2)*x + w(3)*x.*x) - y;   % h(x) - y(x)
Dresfunc = @(w,x,y) [resfunc(w,x,y), resfunc(w,x,y).*x, resfunc(w,x,y).*x.*x];

eta = 1e-3;
T = 1000;
res = zeros(T + 1, 1);
res(1) = norm(resfunc(w, x, y));
for i = 1:T
    p = Dresfunc(w, x, y);
    w = w - eta * sum(p)/norm(p);
    res(i + 1) = norm(resfunc(w, x, y));
end

xi = 0:0.01:10;  s = floor(m / 100);
h = (w(1) + w(2)*xi + w(3)*xi.*xi);
subplot(1,2,1); plot(xi, h, 'LineWidth', 2, x(1:s:end), y(1:s:end), 'r*');
subplot(1,2,2); plot(res);
