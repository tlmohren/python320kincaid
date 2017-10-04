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

### Function of the week:
np.allclose()

```python
x = np.sin( np.pi )
x == 0
Out[2]: False
np.allclose(0,x)
Out[3]: True
```
### Magic command(%) of the week: 
%debug
```python
def plot_frequency_spectrum(signal,sampling_rate):
     N = len(signal)
     yf =scipy.fftpack.fft(signal)
     xf = np.arange(0.0,N//2,1) /N*sampling_rate
     yf_norm = 2.0/N*np.abs(yf[:N//2])
     return xf,yf_norm
plot_frequency_spectrum(np.sin(range(10)),(10,10))
Out[2]: ValueError                                Traceback (most recent call last)
In[2]: %debug 
ipdb> type(sampling_rate)
<class 'tuple'>
ipdb> np.size(sampling_rate)
2
ipdb> quit
```


