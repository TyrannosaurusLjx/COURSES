function y = objfunc(w, x)
    n = size(w, 1);
    y = 0;
    phi = ones(size(x));
    for i = 1:n
        y = y + w(i) * phi;
        phi = phi .* x;
    end
end