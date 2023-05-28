clear
clc

% wheel parameters
Mwheel= 0.180;
Rwheel = 0.075;
Jwheel = 0.5*Mwheel*Rwheel^2;    % we assumed inertia of a disk

m = 2;      % chassis mass
l = 0.2;   
Jb = m*l^2;
% center of gravity was assumed lower to ground by
% looking at mass distribution on the chassis (chassis length = 50cm)
% and the inertia was assumed as a point mass at COG

%motor parameters
stall_current = 1.06; % A
stall_torque = 186*9.80665*10^-5; % g.cm to N.m
no_load_speed = 5600; % rpm
no_load_current = 0.025; % A

Kt = stall_torque/stall_current; % Nm/A
Ra = 12/stall_current; % voltage/current at stall
Ke = (12 - no_load_current*Ra)/(no_load_speed*2*pi*60); %
n = 34;%
g = 9.81;   %


H = Jwheel + m + Mwheel*Rwheel;
A = (2*Kt*Ke*n^2)/(Ra*Rwheel*H);
B = (2*l*m*Kt*Ke*n^2)/(Ra*Jb*H);
C = (-2*Kt*Ke*n^2)/(Ra*Rwheel*H);
D = (-2*l*m*Kt*Ke*n^2)/(Ra*Rwheel*Jb*H);
E = (2*Kt*n)/(Ra*Rwheel*H);
F = (2*l*m*Kt*n)/(Ra*Jb*H);
G = (g*l^2*m^2)/(Jb*H);
I = (-2*Kt*Ke*n^2)/(Ra*Jb);
J = (2*Kt*Ke*n^2)/(Rwheel*Ra*Jb);
K = (-2*Kt*n)/(Ra*Jb);
L = (g*l*m)/Jb;


SS_A = [0 0 1 0;0 0 0 1; 0 G C+D A+B;0 L J I];
SS_B = [0;0;E+F;K];
SS_C = [1 0 0 0;0 1 0 0];
SS_D = [0;0];
