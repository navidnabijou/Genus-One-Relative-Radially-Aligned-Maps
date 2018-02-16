A.<E,S0,S1,R0,R1,R2,a0,a1,a2,b00,b01,b10,b11,b20,b21,T0,T1,T2> = PolynomialRing(QQ);

I = ideal(T0-R0-a0*E-b00*S0-b01*S1,T1-R1-a1*E-b10*S0-b11*S1,T2-R2-a2*E-b20*S0-b21*S1,E*T0,S0*T0,S1*T0,E*T1,S0*T1,S1*T1,E*T2,S0*T2,S1*T2,T0+T1+T2,R0+R1+R2+S0+S1+E,R0^2+1,R1^2+1,R2^2+1,S0^2+3,S1^2+2,E^2+2,R0*S0-1,R0*R1,R0*E,R0*S1,R0*R2,R1*S0-1,R1*R0,R1*E,R1*S1,R1*R2,S0*R0-1,S0*R1-1,S0*E-1,S0*S1,S0*R2,E*S1-1,E*R2,S1*R2-1)

B=A.quotient(I);

K=ideal(T1*T2-T0*T2)

#isSubset(K,I)

e=B(S0-2);
x=B(T0*(T1-T2)-(3/7));
z=B(T0*(T1-T2)-R0*(T1-T2));
y=B(b10-b20-(2/7));
w=B(R0*(T1-T2)-b10+b20);
print B(S0)==2;
print x==0;
print y==0;
print z==0;
print w==0;
