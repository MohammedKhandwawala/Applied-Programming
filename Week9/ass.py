#name = Mohammed Khandwawala
#date 5th April 2018
from pylab import *

# to just calculate the accuracy of pythons fft function
x = rand(1000000)
X = fft(x)	# calculating fft of randomly generated signal
y = ifft(X)	#and then taking its inverse
c_[x,y]
print abs(x-y).max()	#printing the erro


x=linspace(0,2*pi,129)	#for input sin(5t) we will take time from 0 to 2pi
x=x[:-1]	#removing last value as it will be incuded in next period
y=sin(5*x)	#input
Y=fftshift(fft(y))/128.0 #computing fft and deviding by the scaling factor N.
w=linspace(-64,63,128) 	#frequency domain from -64 to 64
figure()
subplot(2,1,1)	
plot(w,abs(Y),lw=2) 
xlim([-10,10])	#plotting magnitude response between -10 and 10
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\sin(5t)$")
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2) #plotting phase response between -10 and 10
ii=where(abs(Y)>1e-3)
plot(w[ii],angle(Y[ii]),'go',lw=2)
xlim([-10,10])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$k$",size=16)
grid(True)
show()

#------------------------------------------------------------------------

t=linspace(-4*pi,4*pi,513)	#for input (1+0.1cos(t))*cos(10t) we will take time from 0 to 2pi
t=t[:-1]	#removing last value as it will be incuded in next period
y=(1+0.1*cos(t))*cos(10*t) #input
Y=fftshift(fft(y))/512.0 #computing fft and deviding by the scaling factor N.
w=linspace(-64,64,513);w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-15,15])	#plotting magnitude response between -10 and 10
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\left(1+0.1\cos\left(t\right)\right)\cos\left(10t\right)$")
grid(True)
subplot(2,1,2)
ii=where(abs(Y)>1e-6)
plot(w[ii],angle(Y[ii]),'go',lw=2)
xlim([-15,15]) #plotting phase response between -10 and 10
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$k$",size=16)
grid(True)
show()

#------------------------------------------------------------------------------

t=linspace(-4*pi,4*pi,513)	#for input sin(t)**3 we will take time from 0 to 2pi
t=t[:-1]	#removing last value as it will be incuded in next period
y=sin(t)**3 #input
Y=fftshift(fft(y))/512.0 #computing fft and deviding by the scaling factor N.
w=linspace(-64,64,513);w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-15,15])	#plotting magnitude response between -15 and 15
ylabel(r"$|Y|$",size=16)
title("Spectrum of sin$^{3}$(t)")
grid(True)
subplot(2,1,2)
ii=where(abs(Y)>1e-6)
plot(w[ii],angle(Y[ii]),'go',lw=2)
xlim([-15,15])	#plotting phase response between -15 and 15
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$k$",size=16)
grid(True)
show()

#------------------------------------------------------------------------------

t=linspace(-4*pi,4*pi,513)	#for input cos(t)**3 we will take time from 0 to 2pi
t=t[:-1]	#removing last value as it will be incuded in next period
y=cos(t)**3	#input
Y=fftshift(fft(y))/512.0 #computing fft and deviding by the scaling factor N.
w=linspace(-64,64,513);w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-15,15]) #plotting magnitude response between -15 and 15
ylabel(r"$|Y|$",size=16)
title("Spectrum of cos$^{3}$(t)")
grid(True)
subplot(2,1,2)
ii=where(abs(Y)>1e-6)
plot(w[ii],angle(Y[ii]),'go',lw=2)
xlim([-15,15]) #plotting phase response between -15 and 15
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$k$",size=16)
grid(True)
show()

#---------------------------------------------------------------------

t=linspace(-16*pi,16*pi,2049)	#for input cos(20t+5sin(t)) we will take time from 0 to 2pi
t=t[:-1]	#removing last value as it will be incuded in next period
y=cos(20*t + 5*cos(t)) #input
Y=fftshift(fft(y))/2048.0 #computing fft and deviding by the scaling factor N.
w=linspace(-64,64,2049)
w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-30,30])
ylabel(r"$|Y|$",size=16)
title("Spectrum of cos(20*t + 5*cos(t))")
grid(True)
subplot(2,1,2)
ii=where(abs(Y)>1e-3)
plot(w[ii],angle(Y[ii]),'go',lw=2)
xlim([-30,30]) #plotting phase response between -10 and 10
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$k$",size=16)
grid(True)
show()

#---------------------------------------------------------------------


t=linspace(-2**5*pi, 2**5*pi, 10001)	#for input e^(t*t/2) we will take time from 0 to 2pi
t=t[:-1]	#removing last value as it will be incuded in next period
y=exp(-t*t/2)	#input
plot(t,y)
plot(t,ifftshift(y))
Y = fftshift(fft(ifftshift(y)))*(2*(2**5*pi))/10000.0		 #computing fft and deviding by the scaling factor N.
w=linspace(-2**5*pi,2**5*pi,10001)
w=w[:-1]
Y_exp = exp(-(w)**2/2)*sqrt(2*pi)
figure()
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-10,10])	#plotting magnitude response between -9000 and 9000
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $e^{-\frac{t^{2}}{2}}$")
grid(True)
subplot(2,1,2)
ii=where(abs(Y)>1e-6)
plot(w[ii],angle(Y[ii]),'go',lw=2)
xlim([-10,10])	#plotting phase response between -9000 and 9000
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$k$",size=16)
grid(True)
show()
error = (abs(Y) - Y_exp) #taking difference between obained and expected 
print max(error)
semilogy(w,error,'go')
show()

