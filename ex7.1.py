"""
Mubinjon Satymov
Exercise 7.1: Fourier transforms of simple functions
"""
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 1000, endpoint=False)
plt.plot(t, signal.square(2 *np.pi * 2 * t))
plt.title('Graph of Part A')
plt.show()
r=np.fft.rfft(signal.square(2 *np.pi * 2 * t))
plt.plot(r*np.conjugate(r))
plt.title('FFT of Part A')
plt.show()

z = np.linspace(0, 1, 500)
d=signal.sawtooth(2 * np.pi * 2 * z)
plt.plot(z, d)
plt.title('Graph of Part B')
plt.show()
e=np.fft.rfft(d)
plt.plot((e*np.conjugate(e)))
plt.title('FFT of Part B')
plt.show()



n=np.arange(0,1000, step=1)
y=np.sin(np.pi*n/1000)*np.sin(20*np.pi*n/1000)
plt.plot(n,y)
plt.title('Graph of Part C')
plt.show()

fftc=np.fft.rfft(y)
plt.plot(fftc*np.conjugate(fftc))
plt.title('FFT of Part C')
plt.show()