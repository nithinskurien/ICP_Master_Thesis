function lam = lambda(dist)
Pt = 3.981e-5;
k = 1;
Do = 1;
kb = 1.380e-23;
T = 293;
B = 2.2e9;

Pn = 4*kb*T*B;
Ps = Pt*k*(Do/dist)^2;
SNR = Ps/Pn;

lam = 3.8e9/(sqrt(8)*pi*sqrt(SNR)*B);
lam = 1/lam^2;
end