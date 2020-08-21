#author:Mohammed Khandwawala
#date 1/3/17
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from  scipy import linalg	

# declaring the constants 
Nx = 25	# size of the grid
Ny = 25
radius = 8; # radius of the wire
Niter = 700;

# creating vectors x,y for 2-D coordinates
print -Nx/(2*25.0),Ny/(2*25.0)
x = np.linspace(-Nx/(2*25.0),Ny/(2*25.0),25)
y = np.linspace(-Nx/(2*25.0),Ny/(2*25.0),25)

#Y,X coordinates of the grid which we will create
Y,X = np.meshgrid(x,y)

#selecting coordinates inside the circular conductor
ii = np.where(X*X+Y*Y<=(0.35)**2)

#creating grid and marking potential inside the circle 1
phi = np.zeros((Nx,Ny))
phi[ii] = 1

fig1 = plt.figure(1)
ax = p3.Axes3D(fig1)
plt.title('The 3-D surface plot of potential')
surf = ax.plot_surface(Y,X,phi.T,rstride = 1,cstride = 1, cmap = plt.cm.jet)
plt.show()

plt.contour(-Y,-X,phi)
plt.plot(x[ii[0]],y[ii[1]],'ro')
plt.show()

# creaing an array to store error
errors = np.zeros(Niter)
for k in range(Niter):
	oldphi = phi.copy()
	phi[1:-1,1:-1] = 0.25*(phi[1:-1,0:-2]+phi[1:-1,2:]+phi[0:-2,1:-1]+phi[2:,1:-1]) #updating potential as mean of its neighbors
	phi[1:-1,0] = phi[1:-1,1] # Boundary Conditions
	phi[1:-1,-1] = phi[1:-1,-2]
	phi[0,:] = phi[1,:]
	phi[-1,:] = 0 # lower plate potential is 0
	phi[ii] = 1.0		
	errors[k] = (abs(phi-oldphi)).max(); #error measurment 
#taking 50th sample of error
errors50 = errors[::50]

#3-D surface plot of potential
fig1 = plt.figure(1)
ax = p3.Axes3D(fig1)
plt.title('The 3-D surface plot of potential')
surf = ax.plot_surface(-Y,-X,phi.T,rstride = 1,cstride = 1, cmap = plt.cm.jet)
plt.show()

#contour plot of potentials
plt.contour(-Y,-X,phi)
plt.title("Contour Plot of Potential")
plt.plot(y[ii[0]],x[ii[1]],'ro')
plt.show()

#vector plot of the electric field
Jx = np.zeros((Nx,Ny))
Jy = np.zeros((Nx,Ny))
Jx[1:-1,1:-1] = -0.5*(phi[1:-1,:-2]-phi[1:-1,2:])
Jy[1:-1,1:-1] = 0.5*(phi[:-2,1:-1]-phi[2:,1:-1])
plt.quiver(y,x,-Jx[::-1,:],-Jy[::-1,:])
plt.plot(y[ii[0]],x[ii[1]],'ro')
plt.show()

plt.semilogy(errors)
plt.title("semilog plot of error vs iterations")
plt.show()

#fitting error model
#creating matrix of coeff 
A = np.zeros((Niter/50,2))
A[:,0] = 1
A[:,1] = np.arange(1,Niter+1,50)
#finding unknown variable to fit error
fit_1 = linalg.lstsq(A,np.log(errors50))[0]

#fitting error model excluding first 500 points
A = np.zeros(((Niter-500)/50,2))
A[:,0] = 1
A[:,1] = np.arange(501,Niter+1,50)
fit_2 = linalg.lstsq(A,np.log(errors50[10:]))[0]

#printing coeffs obtained by both the model
print fit_1
print fit_2

#fitting the obtained coefficients with the orignsl error.
c = np.ones(Niter)
xiter = np.arange(1,Niter+1)
fit_1_v = np.exp(c*fit_1[0] + (xiter)*fit_1[1])#error = exp(A + Bk)
fit_2_v = np.exp(c*fit_2[0] + (xiter)*fit_2[1])

plt.semilogy(xiter[::50],errors[::50],"ro")
plt.semilogy(xiter[::50],fit_1_v[::50],"g^")
plt.semilogy(xiter[::50],fit_2_v[::50],"b+")
plt.xlabel("Interations")
plt.ylabel("Log(Error)")
plt.title("Plot of log of error and model fitting of error for Niter ="+str(Niter))
plt.legend(["Orignal error","Model fit (all values)","Model fit (excluding first 500)"])
plt.show()

print "A  ",np.exp(fit_2[0])
print "B ",fit_2[1]

print "Max error = -A/B exp(B(Niter + 1))" , np.exp(fit_2[1]*(Niter+1))*(-np.exp(fit_2[0])/fit_2[1])
print "Max Error times half life",np.exp(fit_2[1]*(Niter+1))*(-np.exp(fit_2[0])/fit_2[1])*fit_2[1]
print "Error in last step",errors[-1]

#taking sigma and kappa 1
sigma = 1
kappa = 1

# calculating heating
dx = Nx/24
temp = np.zeros((Nx,Ny))
temp[ii] = 300 
temp[-1,:] = 300
for k in range(Niter):
	#specifying initial conditions
	temp[1:-1,1:-1] = 0.25*(temp[1:-1,0:-2]+temp[1:-1,2:]+temp[0:-2,1:-1]+temp[2:,1:-1]+(dx**2/(sigma*kappa))*((Jx[1:-1,1:-1]**2+Jy[1:-1,1:-1]**2))) #updating potential as mean of its neighbors
	temp[1:-1,0] = temp[1:-1,1] # Boundary Conditions
	temp[0,:] = temp[1,:]
	temp[1:-1,-1] = temp[1:-1,-2]
	temp[-1,:] = 300
	temp[ii] = 300	

fig1 = plt.figure(1)
ax = p3.Axes3D(fig1)
plt.title('The 3-D surface plot of temperature')
surf = ax.plot_surface(-Y,-X,temp.T,rstride = 1,cstride = 1, cmap = plt.cm.jet)
plt.show()


