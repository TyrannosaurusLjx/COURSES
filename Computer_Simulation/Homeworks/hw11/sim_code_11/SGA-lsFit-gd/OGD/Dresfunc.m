function D = Dresfunc(w, xi, yi)
    n = size(w, 1);
    phi = 1;
    D = zeros(n, 1);
    Ri = objfunc(w, xi) - yi;
    for i = 1:n
        D(i) = phi * Ri;
        phi = phi * xi;
    end
    D = D / norm(D);
end