function y = BP_predict( input, W, theta)
%BP_ Summary of this function goes here
%   Detailed explanation goes here
    
 
    n_w = numel(W);
    y = input;
    for i=1:(n_w)
        y = sigmoid(W{i}*y+theta{i});           
    end

end