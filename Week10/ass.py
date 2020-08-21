#author Mohammed Khandwawala
#date 21/04/2018

from pylab import *
import numpy as np
#------------------------------------------Q1-------------------------------
t = linspace(-4*pi,4*pi,257) #timespace -4pi to 4pi in 256 step
t = t[:-1] #removing the last element as it is same as the first
dt = t[1]-t[0]
fmax=1/dt	#sampling frequency
n = arange(256)	#N length DFT
wnd = fftshift(0.54+0.46*cos(2*pi*n/256))
y = sin(sqrt(2)*t) #function for DFT
# y=sin(1.25*t)
WND = fft(wnd) #fft of windowing function(Taken just to observe)
plot(t,wnd)
plot(t,y)
plot(t,y*wnd)
legend(["windowing function","sin($2^{0.5}$t)","Product of both"])
show()
y = y * wnd
y[0] = 0 # the sample corresponding to -tmax should be set zeroo
y = fftshift(y) # make y start with y(t=0) 
Y = fftshift(fft(y))/256.0
w = linspace(-pi*fmax,pi*fmax,257) #frequency space from -fmax pi to fmax pi
w=w[:-1]
plot(w,wnd)
show()
#plotting results
figure()
subplot(2,1,1)
plot(w,abs(Y),'b',w,abs(Y),'bo',lw=2)
xlim([-4,4])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\sin\left(\sqrt{2}t\right)\times w(t)$")
grid(True)
subplot(2,1,2)
ii=where(abs(Y)>1e-3)
plot(w[ii],angle(Y[ii]),'ro',lw=2)
xlim([-4,4])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
show()

#----------------------------------------------Q2----------------------------------------
#Without Windowing
t=linspace(-4*pi,4*pi,257);t=t[:-1]
dt=t[1]-t[0];fmax=1/dt
n=arange(256)
#wnd=fftshift(0.54+0.46*cos(2*pi*n/256))
y=cos(0.86*t)**3
y=y
y[0]=0 # the sample corresponding to -tmax should be set zero
y=fftshift(y) # make y start with y(t=0)
Y=fftshift(fft(y))/256.0
w=linspace(-pi*fmax,pi*fmax,257);w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),'b',w,abs(Y),'bo',lw=2)
xlim([-4,4])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of cos$^{3}(\omega_{o}t)$")
grid(True)
subplot(2,1,2)
ii=where(abs(Y)>1e-3)
plot(w[ii],angle(Y[ii]),'ro',lw=2)
xlim([-4,4])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
show()

#With Windowing
t=linspace(-4*pi,4*pi,513);t=t[:-1]
dt=t[1]-t[0];fmax=1/dt
n=arange(512)
wnd=fftshift(0.54+0.46*cos(2*pi*n/512))
y=cos(0.86*t)**3
y=y*wnd
y[0]=0 # the sample corresponding to -tmax should be set zeroo
y=fftshift(y) # make y start with y(t=0)
Y=fftshift(fft(y))/512.0
w=linspace(-pi*fmax,pi*fmax,513);w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),'b',w,abs(Y),'bo',lw=2)
xlim([-4,4])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of cos$^{3}(\omega_{o}t)$")
grid(True)
subplot(2,1,2)
ii=where(abs(Y)>1e-3)
plot(w[ii],angle(Y[ii]),'ro',lw=2)
xlim([-4,4])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
show()

#-------------------------------------------------------Q3---------------------------------

omega = 0.976881673062# np.random.uniform(0.5,1.5) #randomly distributed omega (As given in problem)
delta = -0.270480948569#np.random.uniform(-1,1)*pi #randomly distributed delta
print omega
print delta
t = linspace(-pi,pi,257)
dt = t[1] - t[0]
fmax = 1/dt
t = t[:-1]
n=arange(256)
wnd= fftshift(0.54+0.46*cos(2*pi*n/256))
y = cos( omega * t + delta )
y[0] = 0
y = fftshift(y)
Y = fftshift(fft(y))/512.0
w=linspace(-pi*fmax,pi*fmax,257)
w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),'b',w,abs(Y),'bo',lw=2)
xlim([-4,4])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of cos$(\omega_{o}t + \delta)$")
grid(True)
subplot(2,1,2)
ii=where(abs(Y)>1e-3)
plot(w[ii],angle(Y[ii]),'ro',lw=2)
xlim([-4,4])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
show()	
maximum = max(abs(Y))
jj = where(abs(Y) == maximum)
print "omega estimation",w[jj]
print "delta estimation",angle(Y[jj])
#--------------------------------------------------Q4-----------------------------
t = linspace(-pi,pi,257)
dt = t[1] - t[0]
fmax = 1/dt
t = t[:-1]
y = cos( omega * t + delta )
y[0] = 0
y = fftshift(y)
y  =  y + 0.1*randn(256)
y = y*wnd
Y = fftshift(fft(y))/256.0
w=linspace(-pi*fmax,pi*fmax,257)
w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),'b',w,abs(Y),'bo',lw=2)
xlim([-4,4])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of cos$(\omega_{o}t + \delta)$")
grid(True)
subplot(2,1,2)
ii=where(abs(Y)>1e-3)
plot(w[ii],angle(Y[ii]),'ro',lw=2)
xlim([-4,4])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
show()	
maximum = max(abs(Y))
jj = where(abs(Y) == maximum)
print "omega estimation",w[jj]
print "delta estimation",angle(Y[jj])

#-------------------------------------------Q5-----------------------------------

t = linspace(-pi,pi,1025)
dt = t[1] - t[0]
fmax = 1/dt
t = t[:-1]
y = cos( 16*(1.5 + t/(2*pi))*t )
plt.plot(t,y)
plt.title(r"cos(16(1.5 + $\frac{t}{2\pi})t$)")
plt.show()
y[0] = 0
y = fftshift(y)
n=arange(1024)
Y = fftshift(fft(y))/1024.0
w=linspace(-pi*fmax,pi*fmax,1025)
w=w[:-1]
figure()
subplot(2,1,1)
plot(w,abs(Y),'b',lw=2)
xlim([-60,60])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of cos$(16 * ( 1.5 + \frac{t}{/2*/pi}) t)$")
grid(True)
subplot(2,1,2)
ii=where(abs(Y)>1e-2)
plot(w[ii],angle(Y[ii]),'ro',lw=2)
xlim([-60,60])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
show()	

#------------------------------------------Q6-------------------------------------------

t = linspace(-pi,pi,1025)
dt = t[1] - t[0]
fmax = 1/dt
t = t[:-1]
y = cos( 16*(1.5 + t/(2*pi))*t )
y = reshape(y,(-1,16))
y[:,0] = 0
y = fftshift(y)
Y = fftshift(fft(y))/16.0 
w=linspace(-pi*fmax,pi*fmax,17)
w=w[:-1]

import mpl_toolkits.mplot3d.axes3d as p3
plt.contour(w,t[::16],abs(Y))
plt.xlabel("$\omega$")
plt.ylabel("time")
plt.show()

W,T = np.meshgrid(t[::16],w)
fig1 = plt.figure(1)
ax = p3.Axes3D(fig1)
plt.title('The 3-D surface plot')
surf = ax.plot_surface(T,W,abs(Y.T),rstride = 1,cstride = 1, cmap = plt.cm.jet)
plt.xlabel("$\omega$")
plt.ylabel("time")
plt.show()


