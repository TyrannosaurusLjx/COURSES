clear
clc
%formula of real function
f = @(x1,x2,x3)x1^2+ x2^2 + x3^2;
nabla_f = [2,2,2]';

%inputs
inputs = 1;
%begin a NN
%set networks
[in,~] = size(inputs);
[out,~] = size(nabla_f);
n_levels = [in,2,out];

%feedforward NN
%define w0 and theta0
W = create_w(n_levels);
theta = create_theta(n_levels);

%set loop parameters
np = 1;
perf = 1;
Iter = 200;
Perf = zeros(1,Iter);
step =  0.1;
n_l = length(n_levels);
n_w = numel(W);
n = numel(inputs);

while(np < Iter && perf > 1e-7)
  z =  cell(n_w,1);
  DW = cell(n_w,1);
  DTheta = cell(n_w,1);
  K = cell(n_w,1);
  for i = 1:n_w
     if i == 1
       z{i} = W{i}*inputs + theta{i};
       K{i} = inputs;
     else
       z{i} = W{i}*sigmoid(z{i-1}) + theta{i};
       K{i} = sigmoid(z{i-1});
     end
  end
  outputs = BP_predict(inputs, W, theta);
  perf = f(outputs(1),outputs(2),outputs(3))
  Perf(np) = perf;
  %backpropagation
  for i = n_w:-1:1
    if i == n_w
        delta{i} = nabla_f.*Dsigmoid(z{i});
    else
        delta{i} = W{i+1}'*delta{i+1}.*Dsigmoid(z{i});
    end
  end

  %update W and theta, here W and theta are cell array!
  for i = 1:n_w
    W{i} = W{i} - step*delta{i}*K{i}';
    theta{i} = theta{i} - step * delta{i};
  end
  np = np + 1;
end

plot(Perf);
outputs = BP_predict(inputs, W, theta)
minfun = f(outputs(1),outputs(2),outputs(3))