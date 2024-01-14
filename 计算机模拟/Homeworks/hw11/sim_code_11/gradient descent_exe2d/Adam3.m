clear,clc,close all;

%函数及梯度定义
syms x y z
f=x^2+0.1*y^2+2*z^2;%sin(z)+3*(1-x)^2*exp(-(x^3)-(y+1)^2)-10*(x/5-x^3-y^5)*exp(-x^2-y^2)-1/3*exp(-(x+1)^2-y^2);
g=[diff(f,x),diff(f,y),diff(f,z)];

%初始点以及变量初始化
x0=-2;y0=-2;z0=-2;
v=[x,y,z];v1=[x0,y0,z0];
eps=1e-6;
eps1=1e-3;
b1=0.9;b2=0.999;mt=[0,0,0];vt=[0,0,0];
g0=vpa(subs(g,v,v1));
temp0=vpa(norm(g0));
n=0;
s=0.1;
hold_v=v1;

%迭代
while temp0>eps1&&n<=400
    mt=b1*mt+(1-b1)*g0;
    vt=b2*vt+(1-b2)*g0.^2;
    mt_=mt/(1-b1^(n+1));
    vt_=vt/(1-b2^(n+1));
    fval=vpa(subs(f,v,v1));
    d=s*mt_./(sqrt(vt_)+eps);
    v1=v1-d;
    hold_v=[hold_v;double(v1)];
    g0=vpa(subs(g,v,v1));
    temp0=vpa(norm(g0));
    n=n+1;
end
n
vtkwrite('adam.vtk','polydata','lines',hold_v(:,1),hold_v(:,2),hold_v(:,3))
