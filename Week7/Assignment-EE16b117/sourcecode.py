#author Mohammed Khandwawala
#date 14/03/2017

import scipy.signal as sp
import numpy as np
import matplotlib.pyplot as plt

n = input("Enter Problem Number :")
def problem(n):
	if n == 1:
		p1 = np.poly1d([1,0.5]) #polynomial s + 1/2
		p2 = np.poly1d([2,1,2.5]) #polynomial s^2 + s + 5/2
		p3 = np.poly1d([2,0,2.25]) #polynomial s^2 + 2.25
		p2p3 = np.polymul(p2,p3) # multiply p2,p3 (the denominator)
		hs = sp.lti(p1,p2p3)	#numerator divided by denominator (defining transfer funtion)
		t,x = sp.impulse(hs,None,np.linspace(0,50,1000)) #comuting impulse response of the s domain transfer function
		plt.plot(t,x) #plotting time domain signal with x
		plt.xlabel("Time in seconds")
		plt.ylabel("x(t) time domain signal")
		plt.title("solution to d$^{2}$x/dt$^{2}$ + x = cos(1.5t)e$^{-0.5t}u_{o}$(t)")
		plt.show()
	if n == 2:
		p1 = np.poly1d([1,0.05]) #polynomial s + 1/2
		p2 = np.poly1d([2,0.1,2.25+0.0025]) #polynomial s + 1/2
		p3 = np.poly1d([2,0,2.25]) #polynomial s^2 + 1/2
		p2p3 = np.polymul(p2,p3) # multiply p2,p3 (the denominator)
		hs = sp.lti(p1,p2p3) #numerator divided by denominator (defining transfer funtion)
		t,x = sp.impulse(hs,None,np.linspace(0,50,100)) #comuting impulse response of the s domain transfer function
		plt.plot(t,x) #plotting time domain signal with x
		plt.xlabel("Time in seconds")
		plt.ylabel("x(t)")
		plt.title("solution to d$^{2}$x/dt$^{2}$ + x = cos(1.5t)e$^{-0.05t}u_{o}$(t)")
		plt.show()
	if n == 3:
		t = np.linspace(0,50,10000) #calculating for 50 sec
		p1 = np.poly1d([1]) # numerator 1
		p2 = np.poly1d([1,0,2.25])	#denominator polynomial s^2 + 2.25
		H = sp.lti(p1,p2) #numerator by denominator
		for var in np.arange(1.4, 1.6,0.05): #changing frequency of the cosine
			ft = np.cos(var*t)*np.exp(-0.05*t) # input excitation
			t,x,svec = sp.lsim(H,ft,t)  #response of the input excitation
			plt.plot(t,x) #plotting its response
		plt.legend(["1.4","1.45","1.50","1.55","1.6"])	#plot of input response for different frequencies.
		plt.title("Response for different excitaion frequencies.")
		plt.xlabel("Time")
		plt.ylabel("x(t)")	
		plt.show()
		omega,s,phi = H.bode() #plotting phase and magnitude response
		f, axarr = plt.subplots(2,sharex = True)
		axarr[0].set_title("Magnitude Plot")
		axarr.flat[0].set(ylabel = "Magnitude in dB")
		axarr[0].semilogx(omega,s)
		axarr[1].set_title("Phase Plot")
		axarr.flat[1].set(xlabel ="Angular frequency", ylabel = "Phase")
		axarr[1].semilogx(omega,phi)
		plt.show()
	if n == 4:
		#solving coupled equations
		px1 = np.poly1d([1,0,2]) #polynomial s^2 + 2		
		px2 = np.poly1d([1,0,3,0]) #polynomial s^3 + 3s
		X = sp.lti(px1,px2) #transfer function for x
		t1,x = sp.impulse(X,None,np.linspace(0,20,100)) #for 20 sec
		plt.plot(t1,x)
		py1 = np.poly1d([2])	#polynomial 2	
		py2 = np.poly1d([1,0,3,0]) #polynomial s^3 + 3s
		Y = sp.lti(py1,py2)
		t2,y = sp.impulse(Y,None,np.linspace(0,20,100))#for 20 sec
		plt.plot(t2,y)
		plt.xlabel("time")
		plt.legend(["x(t)","y(t)"])
		plt.show()
	if n == 5:
		px1 = np.poly1d([1]) #numerator 1
		px2 = np.poly1d([1e-12,1e-4,1]) #deominator 10^-12s^2 + 10^-4 +1 
		X = sp.lti(px1,px2) #numerator by denomiantor
		omega,s,phi = X.bode() #plotting frequency and magnitude response
		f, axarr = plt.subplots(2,sharex = True)
		axarr[0].set_title("Magnitude Plot")
		axarr.flat[0].set(ylabel = "Magnitude in dB")
		axarr[0].semilogx(omega,s)
		axarr[1].set_title("Phase Plot")
		axarr.flat[1].set(xlabel ="Angular frequency", ylabel = "Phase")
		axarr[1].semilogx(omega,phi)
		plt.show()
	if n == 6:
		#solving for response of rlc network for an input signal cos(10^3t)u(t) - cos(10^6t)u(t)
		px1 = np.poly1d([1])
		px2 = np.poly1d([1e-12,1e-4,1])
		X = sp.lti(px1,px2)
		t1 = np.linspace(0,10e-3,10000) #for time 10ms
		ft = np.cos(1e3*t1)-np.cos(1e6*t1)
		t1,y,svec = sp.lsim(X,ft,t1)
		plt.xlabel("Time")
		plt.ylabel("Output Voltage")
		plt.plot(t1,y)
		plt.show()
problem(n)
