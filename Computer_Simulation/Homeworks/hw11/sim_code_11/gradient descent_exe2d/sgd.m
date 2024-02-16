clear,clc,close all;
syms x y t
eps=1e-6;
f = (1.5-x+x*y)^2+(2.25-x+x*y^2)^2+(2.65-x+x*y^3)^2;
g = [diff(f,x), diff(f,y)];
x0=1.75;y0=1.9;
v=[x,y];
v1=[x0,y0];
g0=vpa(subs(g,v,v1));
temp0=vpa(norm(g0));
n=0;
level=[0.5 2.^[0:25]] ;
fcontour(f,[-5,5,-5,5],'LevelList',level);
caxis([0,2000])
title('sgd')
hold on
s=0.002;
while temp0>eps&&n<=400
    d=-g0;
    fval=vpa(subs(f,v,v1));
    plot([v1(1),v1(1)+s*d(1)],[v1(2),v1(2)+s*d(2)],'Color',[0,0,0],'LineWidth',2);drawnow;%pause(0.3);
    v1=v1+s*d;
    g0=vpa(subs(g,v,v1));
    temp0=vpa(norm(g0));
    n=n+1;
end
n
plot(v1(1),v1(2),'ro'),disp(v1)
disp(fval)