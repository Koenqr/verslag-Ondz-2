import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

#symbols
B,em,n,mu_0=sp.symbols('B em n mu_0') #mag field, charge/mass ratio, number of windings, permeability of free space
U, d_U=sp.symbols('U d_U') #voltage (0.001 V)
r, d_r=sp.symbols('r d_r') #radius (electrons) (0.005 m)
I, d_I=sp.symbols('I d_I') #current (0.01 A)
R, d_R=sp.symbols('R d_R') #radius (coil) (0.0005 m)

#magnetic field
mag_field=sp.Eq(B,(0.715*mu_0*n*I)/R)

charge_mass_ratio=sp.Eq(em,(2*U)/(B**2*r**2))

#error in mag field formula propegation
d_B=sp.sqrt((sp.diff(mag_field.rhs,I)*d_I)**2+(sp.diff(mag_field.rhs,R)*d_R)**2)
d_B=sp.simplify(d_B)
print(f'd_B={sp.latex(d_B)}',"\n\n\n")
#get formula with given values
d_B=d_B.subs({d_I:0.01,d_R:0.0005,R:0.2,n:154,mu_0:1.2566370614e-6})
print(f'd_B={sp.latex(sp.simplify(d_B))}',"\n\n\n")

d_em=sp.sqrt((sp.diff(charge_mass_ratio.rhs,U)*d_U)**2+(sp.diff(charge_mass_ratio.rhs,B)*d_B)**2+(sp.diff(charge_mass_ratio.rhs,r)*d_r)**2)
d_em=sp.simplify(d_em)
d_em=d_em.subs({d_U:0.001,d_r:0.005,B:mag_field.rhs})
d_em=d_em
d_em=sp.simplify(d_em).subs({d_I:0.01,d_R:0.0005,R:0.2,n:154,mu_0:1.2566370614e-6})
print(f'd_em={sp.latex(d_em)}',"\n\n\n")