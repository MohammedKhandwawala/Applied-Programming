#Author: Mohammed Khandwawala
#Week 4
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg,special

#defining approximate bessel function
def J(x,v): 	
	return special.jv(1,x)

#creating a vector of 41 values from 0 - 20.
x = np.linspace(0.5,20,40)

#calculating bessel function for v = 1
jx1 =  J(x,1)

#plotting J1x
plt.plot(x,jx1)
plt.ylabel("J$_{v}$(x)")
plt.xlabel("x")
plt.grid(True)
plt.title("x vs bessel function for v=1")
plt.show()

#Defining function to approximate bessel function as weighted sum of sinusoids
#To Calculate weight we will use least sqaures.
#Defining function to compute sinusoid matrix as of first model
def sincos (x):
	return [np.cos(x),np.sin(x)]
##Defining function to compute sinusoid divide by root x matrix as of second model
def sincos2 (x):
	return [np.cos(x)/np.sqrt(x),np.sin(x)/np.sqrt(x)]

#computing v from weights by first calculating phase and then comparing
#To store v from first method
v=[]
#To store v from second method
v_2=[]
for i in range(0,37):
	x1 = x[i:40]
	#to get matrix with sinusoids 
	M1_1 = np.transpose(sincos(x1))
	#to get A,B using least square by matrix approach	
	M3_1 = J(x1,1)
	coeff = linalg.lstsq(M1_1,M3_1)[0]
	phi = coeff[0]/np.sqrt(coeff[0]**2+coeff[1]**2)
	v.append((2/np.pi)*(np.arccos(phi)-np.pi/4))

for i in range(0,37):
	x1 = x[i:40]
	#creating matrix with sinusoids by root x 
	M1_2 = np.transpose(sincos2(x1))
	print M1_2
	#to get A,B using least square by matrix approach
	M3_2 = J(x1,1)
	print M3_2
	coeff2 = linalg.lstsq(M1_2,M3_2)[0]
	phi_2 = coeff2[0]/np.sqrt(coeff2[0]**2+coeff2[1]**2)
	print phi_2
	v_2.append((2/np.pi)*(np.arccos(phi_2)-np.pi/4))

#to get back the function by multipling Obtained coefficients and sinusoid matxix.(As a verification of method) 
#plt.plot(x[40-len(np.matmul(M1_2,coeff2)):40],np.matmul(M1_2,coeff2))
#plt.show()

#plotting obtained value of v
plt.plot(v,"go")
plt.plot(v_2,"bo")
plt.title("Value of v computed")
plt.legend(["model (b)","model (c)"])
plt.show()
#defining a function to compute v by taking x , model and noise.
def calcnu(x,xo,color,eps,model):
	if model == "b" :
		v=[]
		for i in range(0,(len(x)/20)*xo+1):
			x1 = x[i:len(x)]
			M1_1 = np.transpose(sincos(x1))
			M3_1 = J(x1,1)
			coeff = linalg.lstsq(M1_1,M3_1+eps*np.random.randn(len(x1)))[0] 
			#adding noise to the functional values
			phi = coeff[0]/np.sqrt(coeff[0]**2+coeff[1]**2)
			#computing phase and than obtaining v
			v.append(((2/np.pi)*(np.arccos(phi)-np.pi/4)))
	if model == "c" :
		v=[]
		for i in range(0,(len(x)/20)*xo+1):
			x1 = x[i:len(x)]
			M1_2 = np.transpose(sincos2(x1))
			M3_2 = J(x1,1)
			coeff2 = linalg.lstsq(M1_2,M3_2+eps*np.random.randn(len(x1)))[0] 
			#adding noise to the functional values
			phi_2 = coeff2[0]/np.sqrt(coeff2[0]**2+coeff2[1]**2)
			#computing phase and than obtaining v
			v.append((2/np.pi)*(np.arccos(phi_2)-np.pi/4))
	plt.plot(x[0:(len(x)/20)*xo+1],v,color)

#calling the above funtion to perform the same 	
calcnu(x,18,"go",0,"b")
calcnu(x,18,"bo",0,"c")
#now adding noise to see the effect
calcnu(x,18,"ro",0.01,"c")
plt.grid(True)
plt.legend(["e = 0, model (b)","e = 0, model (c)","e = 1.0e-02, model (c)"])
plt.show()

#checking variation with number of measurements

x_2 = np.linspace(0.5,20,40)
x_3 = np.linspace(0.5,20,1000)
#for model (b)
calcnu(x_2,18,"r^",0.005,"b")
calcnu(x_3,18,"b+",0.005,"b")

plt.title("Variation in (b) model with number of measurements with noise")
plt.grid(True)
plt.legend(["with 40 measurements","with 1000 measurements"])
plt.show()
#for model (c)	
calcnu(x_2,18,"r^",0.005,"c")
calcnu(x_3,18,"b+",0.005,"c")

plt.title("Variation in (c) model with number of measurements with noise")
plt.grid(True)
plt.legend(["with 40 measurements","with 1000 measurements"])
plt.show()	

#checking out effect of noise
#for model (b)
calcnu(x,18,"go",0,"b")
calcnu(x,18,"b^",0.05,"b")
calcnu(x,18,"c+",0.03,"b")
calcnu(x,18,"rx",0.01,"b")
plt.grid(True)
plt.title("Variation in (b) model with noice")
plt.legend(["e = 0, model (b)","e = 0.05, model (b)","e = 0.03, model (b)","e = 0.01, model (b)"])
plt.show()

#for model (c)
calcnu(x,18,"go",0,"c")
calcnu(x,18,"b^",0.05,"c")
calcnu(x,18,"c+",0.03,"c")
calcnu(x,18,"rx",0.01,"c")
plt.grid(True)
plt.title("Variation in (c) model with noise")
plt.legend(["e = 0, model (c)","e = 0.05, model (c)","e = 0.03, model (c)","e = 0.01, model (c)"])
plt.show()

#checking the affect of varying noise by fitting 1000 points
#for model(b)
calcnu(x_3,18,"b^",0.05,"b")
calcnu(x_3,18,"c+",0.03,"b")
calcnu(x_3,18,"rx",0.01,"b")

plt.grid(True)
plt.title("Variation in (b) model with noise 1000 points")
plt.legend(["e = 0.05, model (b)","e = 0.03, model (b)","e = 0.01, model (b)"])
plt.show()

#for model (c)
calcnu(x_3,18,"b^",0.05,"c")
calcnu(x_3,18,"c+",0.03,"c")
calcnu(x_3,18,"rx",0.01,"c")

plt.grid(True)
plt.title("Variation in (c) model with noise 1000 points")
plt.legend(["e = 0.05, model (c)","e = 0.03, model (c)","e = 0.01, model (c)"])
plt.show()
