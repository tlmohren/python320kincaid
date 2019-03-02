import numpy as np

def m_v(n):
    '''Alternate function to create pendulum masses'''
    xs = np.arange(n)
    ys = np.array([[(0.5+2*x)/(2*sum(xs)) for x in xs][::-1]]).T
    return ys

def len_v(n):
    '''Alternate function to create pendulum lengths'''
    xs = np.arange(n)
    ys = np.array([[1+x**2 for x in xs][::-1]]).T
    return ys