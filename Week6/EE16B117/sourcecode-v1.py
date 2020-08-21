#author : Mohammed Khandwawala
#date : 9/3/17

import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import sys
import pandas as pd
from tabulate import tabulate

if(len(sys.argv) == 7):
	n = int(sys.argv[1])
	M = int(sys.argv[2])
	nk = int(sys.argv[3])
	u0 = float(sys.argv[4])
	p = float(sys.argv[5])
	Msig = float(sys.argv[6])
else:
	n=100 #spatial grid size
	M = 10 #number of electron injected per turn
	nk = 500 #number of turns to simulate
	u0 = 5 #threshold velocity
	p = 0.25 #probality that ionization will occur
	Msig = 2 #standard deviation of normal distribution

xx = np.zeros(n * M)	#to hold position of the electron
u = np.zeros(n * M)	#to hold velocity of electron
dx = np.zeros(n * M)	#displacement in current turn

I = []		#intensity of light
X = []		#Electron position
V = []		#electron veloctiy

count = 0
ii = np.where(xx > 0)[0]
for k in range(0, nk):
	dx[ii] = u[ii] + 0.5 #incrementing dx for position
	xx[ii] = xx[ii] + dx[ii] #incrementing position
	u[ii] = u[ii] + 1	#incrementing velocity a=1
	
	jj = np.where(xx > n)[0] #selecting position which crossed the tube
	dx[jj] = u[jj] = xx[jj] = 0	#making their position and velocity 0
	kk = np.where(u >= u0)	#selecting electrons with velocity greater than critical
	ll = np.where(np.random.rand(len(kk[0])) <= p)	#selecting electron out of those with sufficient based of their probablity to excite
	kl = kk[0][ll]	# selecting those electron that will excite
	rho = np.random.rand(len(kl))# random time	
	xx[kl] = ( xx[kl] - dx[kl] )  + ( u[kl] - 1 )*rho  + 0.5 * rho ** 2  	#finding exact position of collision between xi-1 and xi
	xx[kl] =  xx	[kl] + (1 - rho) ** 2 #after colision velocity will be zero and it will aagain accelerate.
	u[kl] = (1 - rho)	#making their velocity a*t 
	I.extend(xx[kl].tolist())	#adding it to I,V,X
	
	m = int(np.random.randn() * Msig + M)	#injecting new electrons
	empty = np.where(xx == 0)[0]	#finding empty positions in the xx array
	xx[empty[:min(m,len(empty))]] = 1	#adding new electron there with initial position 1
	u[empty[:min(m,len(empty))]] = 0
	dx[empty[:min(m,len(empty))]] = 0
		
	ii = np.where(xx > 0)[0] #selecting electron in the tube	
	X.extend(xx[ii].tolist())
	V.extend(u[ii].tolist())

#histogram and table(vs position in tube) for I 
data = plt.hist(I,bins=np.arange(0,101,1),rwidth=0.8,color = 'r')
bins = data[1]
xpos = 0.5 * (bins[0:-1] + bins[1:])
df = pd.DataFrame({ "count":data[0], "xpos":xpos})
print tabulate(df ,headers = 'keys' , tablefmt = 'psql')
plt.show()

#histogram of electron pos
plt.hist(X,bins=np.arange(0,101,0.5),rwidth=0.8,color = 'r')
plt.show()

#phase space of electron
plt.plot(X,V,'ro')
plt.xlabel("Position")
plt.ylabel("Velocity")
plt.show()

#plotting in 2-d histogram X,V
plt.hist2d(X,V,(50,50))
plt.colorbar()
plt.show()
	
