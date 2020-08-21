#author:mohammed khandwawala(e16b117)
import numpy as np
import math
n = [0.2]
alpha = np.pi
for k in range(1, 1000):
        val = ((n[k-1] + np.pi)* 100.0) - int ((n[k-1] + np.pi)* 100.0)
        p = str(val)
        print p[0:6]
        n.append(val)        

