%% Intialise

g = [];
anchor1 = [0;0];
anchor2 = [0;3];
anchor3 = [3.5;0];
anchor4 = [3.5;3];
anchor5 = [1.75;1.5];
anchor = [anchor1 anchor2 anchor3 anchor4 anchor5];
count = 0;

for x = 0:.35:3.5  
    for y = 0:.3:3
        for z = 1:1:length(anchor(1,:))
       if isequal([x;y],anchor(:,z))
           count = 1;
       end
       end
        if count == 0
         g = [g [x;y]];
        end
        count = 0;
    end
end


C = [];

for i = 1:1:length(g(1,:))
    J_c = 0;
    for j = 1:1:length(anchor(1,:))
        phi = atan((g(1,i)-anchor(1,j))/(g(2,i)-anchor(2,j)));
        D = sqrt((anchor(1,j)-g(1,i))^2 + (anchor(2,j)-g(2,i))^2);
        J_r = [cos(phi)^2 cos(phi)*sin(phi);cos(phi)*sin(phi) sin(phi)^2];
        J_c = J_c + J_r*lambda(D);
    end
    C = [C inv(J_c)];
end

DC = 0;
DistC = 0;
for i=0.1:0.1:4
   DistC = 1/lambda(i);
   DC = [DC DistC];
end

figure(1)
rectangle('Position',[0 0 3.5 3],'Linestyle','-.');
axis([-.5 4 -.5 3.5]);
hold on
grid on
%grid minor
set(gca,'xtick',[0:.35:3.5]);
set(gca,'ytick',[0:.30:3]);
xlabel('X (m)');
ylabel('Y (m)');
title('300\sigma Plots for Anchor Configuration');

%% Anchor Points

for i = 1:1:length(anchor(1,:))
    plot(anchor(1,i), anchor(2,i),'+','LineWidth',2,'MarkerSize',10);
end

%% Plots
size = 100;

for i = 1:1:length(g(1,:))
hold on;
if(~isnan(C(1,2*i)))
n = 100; % Number of grid points
phi = linspace(0,2*pi,100); % Create grid in interval [0,2*pi]   
mu = g(:,i); % Mean of a 2
P = C(:,2*i-1:2*i);
x = repmat(mu,1,n) + size*3*sqrtm(P)*[cos(phi);sin(phi)];
plot(x(1,:),x(2,:),'-g','linewidth',2);
end
end

temp = 0:0.1:4
figure(2)
plot(temp,DC,'-r','linewidth',2)
xlabel('Distance (m)')
ylabel('Variance (m^2)')
grid on
title('CRB on Distance Ranging')