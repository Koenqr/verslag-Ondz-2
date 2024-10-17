import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

#symbols
B,em,n,mu_0=sp.symbols('B em n mu_0') #mag field, charge/mass ratio, number of windings, permeability of free space
U, d_U=sp.symbols('U d_U') #voltage (0.001 V)
r, d_r=sp.symbols('r d_r') #radius (electrons) (0.005 m)
I, d_I=sp.symbols('I d_I') #current (0.01 A)
R, d_R=sp.symbols('R d_R') #radius (coil) (0.005 m)

#magnetic field
mag_field=sp.Eq(B,(0.715*mu_0*n*I)/R)

charge_mass_ratio=sp.Eq(em,(2*U)/(B**2*r**2))

subbed=charge_mass_ratio.subs(B,mag_field.rhs)

#error propagation formula (accounting for defined errors)
error_prop=sp.sqrt((sp.diff(subbed,U)*d_U)**2+(sp.diff(subbed,R)*d_R)**2+(sp.diff(subbed,r)*d_r)**2+(sp.diff(subbed,I)*d_I)**2)

print(sp.latex(error_prop))


