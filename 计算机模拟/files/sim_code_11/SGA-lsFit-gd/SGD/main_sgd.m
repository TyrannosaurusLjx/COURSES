clear
m = 1000;
x = 10 * rand(m, 1);
eta = 1e-3;
T = 10000;
res = zeros(T + 1, 1);
noise = randn(m, 1);
y = realfunc(x);% + 0.1 * noise;
w = rand(3, 1);
res(1) = norm(resfunc(w, x, y));
res_m = res(1);
w_m = w;
%w = [0; 0.00; 1.00];
for i = 0:T
    s = mod(i, m) + 1;
    p = Dresfunc(w, x, y, 10);
    w = w - eta * p;
    res(i + 1) = norm(resfunc(w, x, y));
    if (res(i + 1) < res_m)
        res_m = res(i + 1);
        w_m = w;
    end
end
