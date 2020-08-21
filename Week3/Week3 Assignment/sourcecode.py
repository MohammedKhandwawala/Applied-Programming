#author:Mohammed khandwawala
#assignment 3
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

#defining Function cos(cos(x)) and Exp(x)
def exp(x):
	return np.e**x

def coscos(x):
	return np.cos(np.cos(x))

#creating a vector from -2pi to 4pi with 600 pts
x = np.arange(-2*np.pi,4*np.pi,np.pi/100)

#passing x vector to above defined fuctions to get thie value at each point
exp_arr = exp(x)
cos_arr = coscos(x)

#plotting exp(x) between 2pi to 4pi
plt.semilogy(x,exp_arr)
plt.xlabel("x")
plt.ylabel("e$^{x}$")
plt.grid(True)
plt.show()

#plotting cos(cos(x)) between 2pi tp 4pi
plt.scatter(x,cos_arr)
plt.xlabel("x")
plt.ylabel("cos(cos(x))")
plt.grid(True)
plt.show()

#expected output by fourier series for coscos(x)
plt.plot(x,cos_arr)
plt.title("Expected fourier approximation for cos(cos(x)) ")
plt.show()
#expected output by fourier series for exp(x)
x3 = np.arange(0,2*np.pi,np.pi/100)
expec_ex = np.array(list(exp(x3))+list(exp(x3))+list(exp(x3)))
plt.plot(x,expec_ex)
plt.title("Expected fourier approximation for e$^{x}$ ")
plt.show()
#defining a function to multiply cos and sine to parameter function. To be used to calculate fourier series
def four_a(x,f,n):
	return f(x)*np.cos(n*x)
def four_b(x,f,n):
	return f(x)*np.sin(n*x)

#creating zero vectors to store fourier coefficients
#An : for a's
#Bn : for b's
An=np.zeros(26)
Bn=np.zeros(26)

#Defied function calculates and returns fourier coefficients (a's and b's) of the parameter function.
def coeff(f):
	for i in range(26):
		if(i==0):
			An[i] = (quad(four_a,0,2*np.pi,args=(f,i,))[0]/(2*np.pi))#computing integral using quad to canculate a0
		else:
			An[i] = (quad(four_a,0,2*np.pi,args=(f,i,))[0]/(np.pi))#for the rest of the coefficient calculating integral using quad
			Bn[i] = (quad(four_b,0,2*np.pi,args=(f,i,))[0]/(np.pi))
	return An,Bn

#calling function to get coefficients for cos(cos(x))
a_coscos,b_coscos = coeff(coscos)

#plotting cos(cos(x)) coefficients on log-log scale
n = np.arange(0,26)
plt.loglog(n,abs(a_coscos),"r+")
plt.loglog(n[1:],abs(b_coscos[1:]),"r+")
plt.grid(True)
plt.title("Log-Log plot of cos(cos(x)) coefficients")
plt.show()

#creating copy of existing vectors(BUG FIX TEST)
a_coscosnew = np.array(a_coscos)
b_coscosnew = np.array(b_coscos)

#plotting cos(cos(x)) coefficients on semi-log scale
plt.semilogy(n,abs(a_coscos),"r+")
plt.semilogy(n[1:],abs(b_coscos[1:]),"r+")
plt.grid(True)
plt.title("Semi-Log plot of cos(cos(x)) coefficients")
plt.show()

#calling function to get coefficients for Exp(x)
a_exp,b_exp = coeff(exp)

#plotting Exp(x) coefficients on log-log scale
plt.loglog(n,abs(a_exp),"r+")
plt.loglog(n[1:],abs(b_exp[1:]),"r+")
plt.grid(True)
plt.title("Log-Log plot of e$^{x}$ coefficients")
plt.show()

#plotting Exp(x) coefficients on semi-log scale
plt.semilogy(n,abs(a_exp),"r+")
plt.semilogy(n[1:],abs(b_exp[1:]),"r+")
plt.grid(True)
plt.title("Semi-Log plot of e$^{x}$ coefficients")
plt.show()

#creating a vector from 0 to @pi with 400 pts. 
x2 = np.linspace(0,2*np.pi,401)
x2=x2[:-1]

#removing the last element 

#alternative method
#Using the values of the function, pts and coefficient to setup matrix equation and derive the coefficients. 
def coeff_2(f,x):
	b = f(x)
	A = np.zeros((400,51))
	A[:,0]=1
	for k in range(1,26):
		A[:,2*k-1] = np.cos(k*x)
		A[:,2*k] = np.sin(k*x)
	return linalg.lstsq(A,b)[0]#using least square method built-in python function

#determining coefficients of cos(cos(x)) fourier series by second method 
temp = coeff_2(coscos,x2)

#separating a and b coefficients
a2_coscos = np.zeros(26)
a2_coscos[0] = temp[0]
a2_coscos[1:] = temp[1::2]
b2_coscos = temp[2::2]

#plotting log-log of fourier coefficients of cos(cos(x)) by both the methods
plt.loglog(n,abs(a2_coscos),"ro")
plt.loglog(n,abs(a_coscosnew),"gx")
plt.loglog(n[1:],abs(b2_coscos),"ro")
plt.loglog(n[1:],abs(b_coscosnew[1:]),"gx")
plt.grid(True)
plt.legend(["coefficients by least square","coefficients by integral"])
plt.title("Log-Log plot of cos(cos(x)) coefficients")
plt.show()

#determining coefficients of exp(x) fourier series by second method
temp = coeff_2(exp,x2)

#separating a and b coefficients
a2_exp = np.zeros(26)
a2_exp[0] = temp[0]
a2_exp[1:] = temp[1::2]
b2_exp = temp[2::2]


#plotting log-log of fourier coefficients of exp(x) by both the methods
plt.loglog(n,abs(a2_exp),"ro")
plt.loglog(n,abs(a_exp),"gx")
plt.loglog(n[1:],abs(b2_exp),"ro")
plt.loglog(n[1:],abs(b_exp[1:]),"gx")
plt.grid(True)
plt.legend(["coefficients by least square","coefficients by integral"])
plt.title("Log-Log plot of exp(x) coefficients")
plt.show()

#calculating error as maximum absolute difference between the coefficients from both the methods
a_diff_coscos = a_coscosnew - a2_coscos
b_diff_coscos = b_coscosnew[1:] - b2_coscos


plt.plot(n,a_diff_coscos,"ro")
plt.plot(n[1:],b_diff_coscos,"g+")
plt.show()

a_diff_exp = a_exp - a2_exp
b_diff_exp = b_exp[1:] - b2_exp

plt.plot(n,a_diff_exp,"ro")
plt.plot(n[1:],b_diff_exp,"g+")
plt.show()

print "maximum a diff for e(x) ",max(a_diff_exp)
print "maximum b diff for e(x) ",max(b_diff_exp)
print "maximum a diff for coscos(x) ",max(a_diff_coscos)
print "maximum b diff for coscos(x) ",max(b_diff_coscos)

#constructing unified array to store a,b coefficients
coeff_coscos = []
coeff_coscos.append(a_coscosnew[0])
for i in range(1,26):
	coeff_coscos.append(a_coscosnew[i])
	coeff_coscos.append(b_coscosnew[i])

coeff_exp = []
coeff_exp.append(a_exp[0])
for i in range(1,26):
	coeff_exp.append(a_exp[i])
	coeff_exp.append(b_exp[i])

#using fourier coefficients approximating functions cos(cos(x)) and exp(x) by fourier series
x3 = np.linspace(0,2*np.pi,401)
x3=x3[:-1]
B = np.zeros((400,51))
B[:,0]=1

#Constructing matrix with sinnx and cosnx 
for k in range(1,26):
	B[:,2*k-1] = np.cos(k*x3)
	B[:,2*k] = np.sin(k*x3)

#multiplying fourier coefficients with sinosoids to approximate the function
re_coscos = np.matmul(B,coeff_coscos)
re_exp = np.matmul(B,coeff_exp)

plt.plot(x3,re_coscos)
plt.title("Approximation of cos(cos(x)) by fourier series")
plt.grid(True)
plt.show()

plt.plot(x3,re_exp)
plt.title("Approximation of e$^{x}$ by fourier series")
plt.grid(True)
plt.show()

print a_exp,b_exp
print a2_exp,b2_exp
