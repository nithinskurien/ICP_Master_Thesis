n = 100; % Number of grid points
phi = linspace(0,2*pi,100); % Create grid in interval [0,2*pi]
i=4
 if(~isnan(C(1,2*i)))
mu = g(:,i) % Mean of a 2
P = C(:,2*i-1:2*i)
x = repmat(mu,1,n)+3*sqrtm(P)*[cos(phi);sin(phi)]; % Equation(12) in HA1 document
plot(x(1,:),x(2,:),'-g','linewidth',2);
end
