from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
from tabulate import tabulate

def taninf(x):
	return 1/(1+x**2)

x = np.arange(0,5.1,0.1)

val = taninf(x)

plt.scatter(x,val)
plt.title(r"Plot of $1/(1+t^{2})$")
plt.show()


integration = []

for i in range(0,len(x)):
	temp = quad(taninf,0,x[i])
	integration.append(temp[0])



plt.scatter(x,val,c='red')
plt.plot(x,integration,c="black")
plt.legend(("quadfn",r"Plot of $1/(1+t^{2})$"))
plt.show()

atan = np.arctan(x)

table = pd.DataFrame({"x":x,"Quad Integral":integration,"arctan(x) value ": atan})
print tabulate(table, headers='keys', tablefmt="psql",floatfmt=("d",".5f",".5f",".1f"))

plt.scatter(x,integration,c='red')
plt.plot(x,atan,c="black")
plt.legend(("quadfunction",r"tan$^{-1}$(x)"))
plt.show()

integration = np.array(integration)
error = abs(integration - atan)

plt.semilogy(x,error,"ro")
plt.title("Error between quad function and arctan(x) value")	
plt.show()

h=0.1
n=5/h

pts = np.arange(0,5,h)
tanval = taninf(pts)
c_sum = np.cumsum(tanval)
trapz = h*(c_sum-(tanval[0]+tanval)/2)
plt.scatter(pts,trapz)
plt.title(r"Plot of $\int_{0}^{5}$ $1/(1+t^{2})$ dx using trapz")
plt.show()


H = []
estimated_error = []
exact_error = []


h = 0.1
for i in range(9):
	pts_2 = np.arange(0,5,h)
	tanval_2 = taninf(pts_2)
	act_val = np.arctan(pts_2)
	c_sum_2 = np.cumsum(tanval_2)
	trapz_2 = h*(c_sum_2-(tanval_2[0]+tanval_2)/2)	
	if(i!=0):
		es_err = abs(trapz - trapz_2[::2])
		estimated_error.append(max(es_err))
	ex_err = abs(trapz_2 - act_val)
	exact_error.append(max(ex_err))
	H.append(h)
	trapz = np.array(trapz_2)
	h=h/2
plt.loglog(H[1:],estimated_error,"g+")
plt.loglog(H,exact_error,"ro")
plt.legend(("Estimated Error","Exact Error"))
plt.show()
