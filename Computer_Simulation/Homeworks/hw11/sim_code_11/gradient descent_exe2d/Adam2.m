clear,clc,close all;
syms x y t
eps=1e-6;
eps1=1e-3;
b1=0.9;b2=0.97;mt=[0,0];vt=[0,0];
f = (1.5-x+x*y)^2+(2.25-x+x*y^2)^2+(2.65-x+x*y^3)^2;
g = [diff(f,x),diff(f,y)];
x0=1.75;y0=1.9;
v=[x,y];
v1=[x0,y0];
g0=vpa(subs(g,v,v1));
temp0=vpa(norm(g0));
n=0;
level=[0.5 2.^[0:25]] ;
fcontour(f,[-5,5,-5,5],'LevelList',level);
caxis([0,2000])
title('Adam')
hold on
s=0.1;
while temp0>eps1&&n<=400
    mt=b1*mt+(1-b1)*g0;
    vt=b2*vt+(1-b2)*g0.^2;
    mt_=mt/(1-b1^(n+1));
    vt_=vt/(1-b2^(n+1));
    fval=vpa(subs(f,v,v1));
    d=s*mt_./(sqrt(vt_)+eps);
    plot([v1(1),v1(1)-d(1)],[v1(2),v1(2)-d(2)],'Color',[0,0,0],'LineWidth',2);drawnow;%pause(0.3);
    v1=v1-d;
    g0=vpa(subs(g,v,v1));
    temp0=vpa(norm(g0));
    n=n+1;
end
n
plot(v1(1),v1(2),'ro'),disp(v1)
disp(fval)