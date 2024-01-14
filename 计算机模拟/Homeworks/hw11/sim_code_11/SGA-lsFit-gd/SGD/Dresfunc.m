function D = Dresfunc(w, x, y, ms)
    n = size(w, 1);
    D = zeros(n, 1);
    m = size(x, 1);
    picked = zeros(size(x));
    for k = 1:ms
        while (1)
            s = randi(m, 1, 1);
            if picked(s) == 1
                continue;
            end
            picked(s) = 1;
            break;
        end
        Ri = objfunc(w, x(s)) - y(s);
        phi = 1;
        for i = 1:n
            D(i) = D(i) + phi * Ri;
            phi = phi * x(s);
        end
    end
    D = D / ms;
    D = D / norm(D);
end