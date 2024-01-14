function M = Ising(T)    % T is the tempure.  +-+-+   Ising area.
    nTrials = 10000;    % for stat.          |3|4|   N = 2.
    startup = 3000;    % for steady.         +-+-+   free boundary.
    d = zeros(1, nTrials);   % results.       |1|2|
    beta = 1/T;              %                +-+-+
    M = 0;
    s = 2 * round(rand(1, 4)) - 1;   % randomly set 1 or -1.
    Es = s(1) * s(2) + s(3) * s(4);
    Es = Es + s(1) * s(3) + s(2) * s(4);
    Es = - Es;
    for t = 1:nTrials
        k = fix(1 + 4 * rand);  % randomly pick 1 ~ 4.
        y = s;         % y is the suggestion dist in s' neighbour.
        y(k) = -s(k);  % randomly flip the status on one point.
        Ey = y(1) * y(2) + y(3) * y(4);
        Ey = Ey + y(1) * y(3) + y(2) * y(4);
        Ey = - Ey;
        h = min(1, exp(-beta * (Ey - Es)));
        if (rand < h)
            s = y;
        end
        if (t > startup)
            Ms = s(1) + s(2) + s(3) + s(4);  % cheating!
            M = M + Ms;                      % this is not Boltzmann dist.
            d(t - startup) = Ms;
        end
    %    if(mod(t, 50000)==0) fprintf('Round %d ...\n', t); end
    end
 %   x = -4:1:4;
 %   hist(d, x);
    M = (M / nTrials) / 4;
end

M = zeros(1, 4);
n_try = 100;
n_verbose = 10;
idx = 0;
for T = [1, 10, 100, 1000]
    idx = idx + 1;
    fprintf('Case with Temeperature T = %d ...\n', k);
    for k = 1:n_try
        if(mod(k, n_verbose)==0) fprintf('   Try round %d ... \n', k); end
        M(idx) = M(idx) + Ising(k);
    end
    M(idx) = M(idx) / n_try;
    fprintf('Finish simulation for case T = %d, M = %f\n', T, M(idx));
end

plot(M) # show the simulated magnetic value in a plot
