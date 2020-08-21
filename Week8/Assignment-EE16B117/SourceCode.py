#author : Mohammed Khandwawala
#date: 22/03/18

from sympy import *
import pylab as p
import scipy.signal as sp
import numpy as np
import matplotlib.pyplot as plt
#input to this fuction are symbolic variables.
#problem1
#declaring function to return Vout in symbolic equation
def LOWPASS(R1, R2, C1, C2, G, Vi):
	s = symbols('s')
	#Matrix Equations are obtained using modified nodal analysis
	A = Matrix([[0,0,1,-1/G],[-1/(1+s*R2*C2),1,0,0],[0,-G,G,1],[-1/R1-1/R2-s*C1,1/R2,0,s*C1]])
	b = Matrix([0,0,0,-Vi/R1])
	V = A.inv() *b
	return(A,b,V)

s = symbols('s')
A,b,V = LOWPASS	(10000.0,10000.0,1e-9,1e-9,1.586,1) #passing given values R1,R2,C1,C2,G and Vi given
Vo = V[3] #obtaining expresion of Vout(symbolic)
w = p.logspace(0,8,801) #logarithmic range from 0 to 10**8
hf = lambdify(s,Vo,"numpy") #converts symbolic expression to lambda function
t=np.linspace(0,50,1000) #simulating for 50s
ss = 1j*w
v = hf(ss) #substituting s with jw in lambda function equation
p.loglog(w,abs(v),lw=2)	
p.grid(True)
p.title("|H(jw)| on log-log scale of Low-Pass filter")
p.show()

Vo = simplify(Vo)	#simplifying transfer function
NUM,DEN = fraction(Vo)	#saperating numerator and denominator

print Vo

NUM = poly(NUM,s)	#numerator polynomial
DEN = poly(DEN,s)	#denominator polynomial

N = list(NUM.coeffs())	#obtaining the coefficients of numerator polynomial in list
D = list(DEN.coeffs())  #obtaining the coefficients of denominator polynomial in list



H = sp.lti([float(N[0])],[float(D[0]),float(D[1]),float(D[2])])
t = np.linspace(0,4*10**-3,1000)
Vi = np.sin(2000*np.pi*t) + np.cos(2*10**6*np.pi*t)
t,V_out,svec = sp.lsim(H,Vi,t)
plt.plot(t,V_out) 
plt.grid("True")
plt.title("Output of the Low-Pass filter to input sinusoids (sin(2000$\pi$t) + cos(2000000$\pi$t))")
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#similarly solving for high pass filter circuit to obtain the output function of High-Pass filter
def HIGHPASS(R1, R3, C1, C2, G, Vi):
	s = symbols('s')
	A = Matrix([[0,0,1,-1/G],[0,-G,G,1],[-s*C2/(1+s*C2*R3),1/R3,0,0],[s*C1+s*C2+1/R1,-s*C2,0,-1/R1]])
	b = Matrix([0,0,0,s*C1*Vi])
	V = A.inv()*b
	return(A,b,V)

s = symbols('s')
A,b,V = HIGHPASS(10000.0,10000.0,1e-9,1e-9,1.586,1)
Vo = V[3]
w = p.logspace(0,8,801)
hf = lambdify(s,Vo,"numpy")
ss = 1j*w
v1 = hf(ss)
p.loglog(w,abs(v1),lw=2)
p.grid(True)
p.title("|H(jw)| on log-log scale of High-Pass filter")
p.show()

Vo = simplify(Vo)
NUM,DEN = fraction(Vo)

print Vo

NUM = poly(NUM,s)
DEN = poly(DEN,s)

N = list(NUM.coeffs())
D = list(DEN.coeffs())


#passing sinusoids to the High Pass filter of two different frequencies to observe the output
H = sp.lti([float(N[0]),0.0,0.0],[float(D[0]),float(D[1]),float(D[2])])
t = np.linspace(0,4*10**-5,1000)
Vi = np.sin(2000*np.pi*t) + np.cos(2*10**6*np.pi*t)
t,V_out,svec = sp.lsim(H,Vi,t)
plt.plot(t,V_out) 
plt.grid(True)
plt.title("Output of the High-Pass filter to input sinusoids (sin(2000$\pi$t) + cos(2000000$\pi$t))")
plt.show()
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Response of the filter to damped sinusoid
A,b,V = HIGHPASS(10000.0,10000.0,1e-9,1e-9,1.586,1)
Vo = V[3]
w = p.logspace(0,8,801)
hf = lambdify(s,Vo,"numpy")
ss = 1j*w
v1 = hf(ss)

Vo = simplify(Vo)
NUM,DEN = fraction(Vo)


NUM = poly(NUM,s)
DEN = poly(DEN,s)

N = list(NUM.coeffs())
D = list(DEN.coeffs())



#passing damped sinusoid to obtain the output of the signal 
H = sp.lti([float(N[0]),0.0,0.0],[float(D[0]),float(D[1]),float(D[2])])
t = np.linspace(0,4*10**-5,1000)
Vi = (np.sin(2000*np.pi*t) + np.cos(2*10**6*np.pi*t))*np.exp(-100000*t)
t,V_out,svec = sp.lsim(H,Vi,t)
plt.plot(t,V_out)
plt.title("High-Pass filters response to damped sinusoid (sin(2000$\pi$t) + cos(2000000$\pi$t))e$^{-100000t}$") 
plt.grid(True)
plt.show()

#------------------------------------------------------------------------------------------------------------------------------------------------------
#Calculaing unit step response to Low-Pass filter both in s and time domain
A,b,V = LOWPASS	(10000.0,10000.0,1e-9,1e-9,1.586,1/s)
Vo = V[3]
w = p.logspace(0,8,801)
hf = lambdify(s,Vo,"numpy")
t=np.linspace(0,50,1000)	
ss = 1j*w
v = hf(ss)
p.loglog(w,abs(v),lw=2)
p.grid(True)
p.title("Step-response of the Low-Pass filter (s - domain)")
p.show()

A,b,V = LOWPASS	(10000.0,10000.0,1e-9,1e-9,1.586,1)
Vo = V[3]
w = p.logspace(0,8,801)
hf = lambdify(s,Vo,"numpy")
t=np.linspace(0,50,1000)	
ss = 1j*w
v = hf(ss)

Vo = simplify(Vo)
NUM,DEN = fraction(Vo)


NUM = poly(NUM,s)
DEN = poly(DEN,s)

N = list(NUM.coeffs())
D = list(DEN.coeffs())


H = sp.lti([float(N[0])],[float(D[0]),float(D[1]),float(D[2])])
t = np.linspace(0,4*10**-3,100000)
Vi = np.ones(100000)
t,V_out,svec = sp.lsim(H,Vi,t)
plt.title("Step-response of the Low-Pass filter (in-time)")
plt.plot(t,V_out) 
plt.grid(True)
plt.show()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Calculaing unit step response to High-Pass filter both in s and time domain
A,b,V = HIGHPASS(10000.0,10000.0,1e-9,1e-9,1.586,1/s)
Vo = V[3]
w = p.logspace(0,8,801)
hf = lambdify(s,Vo,"numpy")
ss = 1j*w
v1 = hf(ss)
p.loglog(w,abs(v1),lw=2)
p.grid(True)
p.title("Step-response of the High-Pass filter (s - domain)")
p.show()

A,b,V = HIGHPASS(10000.0,10000.0,1e-9,1e-9,1.586,1)
Vo = V[3]
w = p.logspace(0,8,801)
hf = lambdify(s,Vo,"numpy")
ss = 1j*w
v1 = hf(ss)

Vo = simplify(Vo)
NUM,DEN = fraction(Vo)


NUM = poly(NUM,s)
DEN = poly(DEN,s)

N = list(NUM.coeffs())
D = list(DEN.coeffs())


H = sp.lti([float(N[0]),0.0,0.0],[float(D[0]),float(D[1]),float(D[2])])
t = np.linspace(0,4*10**-3,100000)
Vi = np.ones(100000)
t,V_out,svec = sp.lsim(H,Vi,t)
plt.title("step response of the High-Pass filter (in-time)")
plt.grid(True)
plt.plot(t,V_out) 
plt.show()
print sum(V_out)
