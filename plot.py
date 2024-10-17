import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

# header=[U(v), 0.5*B^2*r^2]
r02=pd.read_csv('r02.csv',header=None,sep=',')
r03=pd.read_csv('r03.csv',header=None,sep=',')
r04=pd.read_csv('r04.csv',header=None,sep=',')
r05=pd.read_csv('r05.csv',header=None,sep=',')

#print latex tables (has issues (limited digits no scientific notation))
"""
#get latex tables
tables=[r02.to_latex(),r03.to_latex(),r04.to_latex(),r05.to_latex()]

for i,table in enumerate(tables):
	print(f"r0{i+2} table:")
	print(table)
	print("\n\n\n")
"""
r=[r02,r03,r04,r05]

def fitFunc(x,a):
	return a*x

def to_scientific_latex(number, precision=2):
    # Split the number into coefficient and exponent using scientific notation
    coeff, exp = "{:.{p}e}".format(number, p=precision).split("e")
    # Format it into a LaTeX string
    return rf"{coeff.replace('.', ',')} \cdot 10^{{{int(exp)}}}"

	
    


plt.rcParams.update({'text.usetex': True})
fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)


for i,r in enumerate(r):
	x=r[1]
	y=r[0]
	#polyfit
	fit=np.polyfit(x,y,1)
	ax.scatter(x,y,label=f'r={0.02+i*0.01:.2f}m')
	ax.plot(x,fit[0]*x+fit[1],label='fit r={}m; a=${}$, b=${}$'.format(0.02+i*0.01,to_scientific_latex(fit[0]),to_scientific_latex(fit[1])))

#fit for all r
x=np.concatenate((r02[1],r03[1],r04[1],r05[1]))
y=np.concatenate((r02[0],r03[0],r04[0],r05[0]))
fit,cov=np.polyfit(x,y,1,cov=True)
ax.plot(x,fit[0]*x+fit[1],label='fit all r; a=${}$, b=${}$'.format(to_scientific_latex(fit[0]),to_scientific_latex(fit[1])))


print("a={}\pm {}, b={}\pm {}".format(to_scientific_latex(fit[0],3),to_scientific_latex(np.sqrt(cov[0,0]),3),to_scientific_latex(fit[1],3),to_scientific_latex(np.sqrt(cov[1,1]),3)))


ax.grid()
plt.ylabel('$U\mathrm{[v]}$')
plt.xlabel(r'$\frac{1}{2}\cdot B^2\cdot r^2\mathrm{[T^2\cdot m^2]}$')
plt.legend()
plt.savefig('plot.png')
plt.show()
