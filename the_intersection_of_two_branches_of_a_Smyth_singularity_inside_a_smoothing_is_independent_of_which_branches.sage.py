
# This file was *autogenerated* from the file the_intersection_of_two_branches_of_a_Smyth_singularity_inside_a_smoothing_is_independent_of_which_branches.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7)
A = PolynomialRing(QQ, names=('E', 'S0', 'S1', 'R0', 'R1', 'R2', 'a0', 'a1', 'a2', 'b00', 'b01', 'b10', 'b11', 'b20', 'b21', 'T0', 'T1', 'T2',)); (E, S0, S1, R0, R1, R2, a0, a1, a2, b00, b01, b10, b11, b20, b21, T0, T1, T2,) = A._first_ngens(18);

I = ideal(T0-R0-a0*E-b00*S0-b01*S1,T1-R1-a1*E-b10*S0-b11*S1,T2-R2-a2*E-b20*S0-b21*S1,E*T0,S0*T0,S1*T0,E*T1,S0*T1,S1*T1,E*T2,S0*T2,S1*T2,T0+T1+T2,R0+R1+R2+S0+S1+E,R0**_sage_const_2 +_sage_const_1 ,R1**_sage_const_2 +_sage_const_1 ,R2**_sage_const_2 +_sage_const_1 ,S0**_sage_const_2 +_sage_const_3 ,S1**_sage_const_2 +_sage_const_2 ,E**_sage_const_2 +_sage_const_2 ,R0*S0-_sage_const_1 ,R0*R1,R0*E,R0*S1,R0*R2,R1*S0-_sage_const_1 ,R1*R0,R1*E,R1*S1,R1*R2,S0*R0-_sage_const_1 ,S0*R1-_sage_const_1 ,S0*E-_sage_const_1 ,S0*S1,S0*R2,E*S1-_sage_const_1 ,E*R2,S1*R2-_sage_const_1 )

B=A.quotient(I);

K=ideal(T1*T2-T0*T2)

#isSubset(K,I)

e=B(S0-_sage_const_2 );
x=B(T0*(T1-T2)-(_sage_const_3 /_sage_const_7 ));
z=B(T0*(T1-T2)-R0*(T1-T2));
y=B(b10-b20-(_sage_const_2 /_sage_const_7 ));
w=B(R0*(T1-T2)-b10+b20);
print B(S0)==_sage_const_2 ;
print x==_sage_const_0 ;
print y==_sage_const_0 ;
print z==_sage_const_0 ;
print w==_sage_const_0 ;
