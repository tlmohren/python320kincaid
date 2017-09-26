# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:57:46 2017

@author: Thomas
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.fftpack

sample_rate, bird_signal_int = scipy.io.wavfile.read("birds001.wav")
bird_signal_float = np.array(bird_signal_int,dtype=float)

def plot_frequency_spectrum(signal,sampling_rate):
     N = len(signal)
     yf =scipy.fftpack.fft(signal)
     xf = np.arange(0.0,N//2,1) /N*sampling_rate
     yf_norm = 2.0/N*np.abs(yf[:N//2])
     return xf,yf_norm

t = np.arange(0,len(bird_signal_float)/sample_rate,1/sample_rate)
freq,amp = plot_frequency_spectrum( bird_signal_float ,sample_rate)

plt.figure()
plt.subplot(211)
plt.plot(t,bird_signal_float)
plt.subplot(212)
plt.plot(freq,amp)
plt.xlim( freq[[0,amp.argsort()[-2]]]*2)


#%% test function with baseline 
sample_rate_test = 1000
t_test = np.arange(0,10,1/sample_rate_test)
y_test = 3*np.sin(2*np.pi*t_test)+ 0.5*np.sin(2*np.pi* 3.5*t_test)
f_test,a_test = plot_frequency_spectrum(y_test,sample_rate_test)
 
plt.figure()
plt.subplot(211)
plt.plot(t_test,y_test)
plt.subplot(212)
plt.plot(f_test,a_test)
plt.xlim( f_test[[0,a_test.argsort()[-2]]]*2)