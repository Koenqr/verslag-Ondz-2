import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

# header=[U(v), 0.5*B^2*r^2]
r02=pd.read_csv('r02.csv',header=None,sep=',')
r03=pd.read_csv('r03.csv',header=None,sep=',')
r04=pd.read_csv('r04.csv',header=None,sep=',')
r05=pd.read_csv('r05.csv',header=None,sep=',')

r=[r02,r03,r04,r05]

def fitFunc(x,a):
	return a*x



fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)


for i,r in enumerate(r):
	x=r[1]
	y=r[0]
	#polyfit
	fit=np.polyfit(x,y,1)
	ax.scatter(x,y,label=f'r={0.02+i*0.01:.2f}m')
	ax.plot(x,fit[0]*x+fit[1],label='fit r={}m; a={:.3e}, b={:.3e}'.format(0.02+i*0.01,fit[0],fit[1]))

#fit for all r
x=np.concatenate((r02[1],r03[1],r04[1],r05[1]))
y=np.concatenate((r02[0],r03[0],r04[0],r05[0]))
fit=np.polyfit(x,y,1)
ax.plot(x,fit[0]*x+fit[1],label='fit all r; a={:.3e}, b={:.3e}'.format(fit[0],fit[1]))


ax.grid()
plt.ylabel('U(v)')
plt.xlabel('0.5*B^2*r^2(T^2m^2)')
plt.legend()
plt.savefig('plot.png')
plt.show()
