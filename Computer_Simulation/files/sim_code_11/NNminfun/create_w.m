function [ W ] = create_w( n_levels )
%CREATE_W Summary of this function goes here
%   Detailed explanation goes here
    n_level = numel(n_levels) - 1;
    W = cell(n_level,1);
    for i=1:n_level
       W{i} = 2*rand(n_levels(i+1), n_levels(i)) - 1; 
    end

end
