clear all
close all
clc

%% initialization
% input x & y
x1 = [1 3 2104];        y1 = 400;
x2 = [1 3 1600];        y2 = 330;
x3 = [1 3 2400];        y3 = 369;
x4 = [1 2 1416];        y4 = 232;
x5 = [1 4 3000];        y5 = 540;

X = [x1;x2;x3;x4;x5];
Y = [y1;y2;y3;y4;y5];

N = 5;      % the number of sample

% parameter
theta_new = zeros(length(x1),1);

% iteration number
itn = 2e2;

% tolerance
tol = 1e-20;

% learning rate(stepsize)
alpha_BGD = 0.00000001;
alpha_SGD = 0.0000001;
%% main function

i = 1;       %itn index
theta_old = theta_new; 
error = 1.0;
k = 1; % SGD sample index

enenrgy = zeros(itn,1);

option = input('Enter the case(number) you want: \n 1 -> BGD. \n 2 -> SGD.\n ' )

while((i <= itn) && (error >= tol))

    switch option        

        case 1            
            % BGD
            sum_temp = 0;
                for jj = 1:N
                    sum_temp = sum_temp + ( Y(jj) - X(jj,:)*theta_old )*X(jj,:)';
                end
            theta_new = theta_old + alpha_BGD*sum_temp;

        case 2
            % SGD            
            theta_new = theta_old + alpha_SGD*( Y(k) - X(k,:)*theta_old )*X(k,:)';  

            if k == 5
                k = 1;
            else
                k = k+1;
            end

       end


    error = norm(X*theta_new-Y)^2;
    theta_old = theta_new;

    energy(i) = error;


    i = i + 1;
end

figure,plot(1:length(energy),energy),title('error(energy)');
itn = i-1
theta = theta_new