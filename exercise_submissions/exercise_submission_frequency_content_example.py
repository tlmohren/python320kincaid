# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:57:46 2017

@author: Thomas
"""

#matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

N = 1001
T = 1.0 / 100.0
x = np.linspace(0.0, N*T, N)
y = 2.6*np.sin(4.0 * 2.0*np.pi * x) + \
      1.5*np.sin(9.0 * 2.0*np.pi* x)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()