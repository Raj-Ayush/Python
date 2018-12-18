# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 07:47:15 2018

@author: ayush
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,2*np.pi,0.1)
plt.xlabel("t=time")
plt.ylabel("Sin(t)")
y=np.sin(x)
plt.plot(x,y)
plt.grid()
plt.stem(x,y,'r')
plt.show()