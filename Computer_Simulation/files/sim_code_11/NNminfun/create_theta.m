function [ theta ] = create_theta( levels )
%CREATE_THETA Summary of this function goes here
%   Detailed explanation goes here
    n_level = numel(levels) - 1;
    theta = cell(n_level, 1);

    for i=1:n_level
       theta{i} = 2*rand(levels(i+1),1) - 1; 
    end

end