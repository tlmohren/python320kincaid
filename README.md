# python320kincaid
Python study group depository

### Depository structure
    python320kincaid/
        |- README.md
        |- exercises/
            |- exercise_frequency_content.md
            |- data/
                |- birds001.wav
                |- iris.csv
                |- fantail-02.mp3
        |- exercise_submissions/
            |- exercise_frequency_content.md
            |- exercise_iris.md

### Jake vanderPlas online books: 

[Whirlwind intro to python](https://github.com/jakevdp/WhirlwindTourOfPython)

[Python for data Science](https://jakevdp.github.io/PythonDataScienceHandbook/index.html)


### Other sources 

[Project Euler, math exercises](https://projecteuler.net/archives)

[A gallery of interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)

### Amazing functions of the week:
np.allclose()
%debug
```python
In[1]: x = np.sin( np.pi )
In[2]: x == 0
Out[2]: False
In[3]: np.allclose(0,x)
Out[3]: True
```
In[1]: def plot_frequency_spectrum(signal,sampling_rate):
     N = len(signal)
     yf =scipy.fftpack.fft(signal)
     xf = np.arange(0.0,N//2,1) /N*sampling_rate
     yf_norm = 2.0/N*np.abs(yf[:N//2])
     return xf,yf_norm

