clear
m = 1000;
x = 10 * rand(m, 1);
eta = 1e-3;
T = 10000;
res = zeros(T + 1, 1);
noise = randn(m, 1);
y = realfunc(x) + 0.01 * noise;
w = rand(3, 1);
res(1) = norm(resfunc(w, x, y));
res_m = res(1);
w_m = w;
% w = [0; 0.00; 1.00];
wmat = zeros(3,T+1);
for i = 0:T
    s = mod(i, m) + 1;
    p = Dresfunc(w, x(s), y(s));
    w = w - eta * p;
    wmat(:,i+1) = w;
    res(i + 1) = norm(resfunc(w, x, y));
    if (res(i + 1) < res_m)
        res_m = res(i + 1);
        w_m = w;
    end
end
