syms Mwheel Rwheel Jwheel Jb m l theta

Mwheel = [Mwheel*Rwheel 0 1 0 -1; Jwheel*Rwheel 0 0 0 +Rwheel; -m -m*l 1 0 0; 0 m*l 0 1 0; 0 Jb 0 0 0]
det(Mwheel);
%pretty(det(M));

inv_M = inv(Mwheel);
%pretty(inv_M);

extractor = [1 0 0 0 0; 0 1 0 0 0];

syms Twheel g

b = [0; 2*Twheel; 0; m*g; m*g*l*theta-2*Twheel];

%answer = extractor * inv_M * b;
%pretty(answer);

answer = (extractor/Mwheel) * b;
pretty(answer)

syms Kt Ke Ra dtheta n dx Vs

Twheel = dtheta*(Kt*Ke*n^2)/Ra - dx*(Kt*Ke*n^2)/(Ra*Rwheel) + Vs*(Kt*n)/Ra;
pretty(Twheel)

answer = (extractor/Mwheel) * b;
pretty(answer)

