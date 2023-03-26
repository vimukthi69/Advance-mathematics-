import numpy as np
import scipy.fftpack as sfft
import matplotlib.pyplot as plt

x = np.arange(-np.pi,np.pi, 0.01)
x1 = np.arange(-np.pi,np.pi, 0.1)

y = np.cos(x) + 0.5*np.cos(50*x)
y1 = np.cos(x1) + 0.5*np.cos(50*x1)

#dft
yf = sfft.fft(y)
yf1 = sfft.fft(y1)

#idft
yf_ = sfft.ifft(yf)
yf1_ = sfft.ifft(yf1)

plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x,np.real(yf_))
plt.plot(x1,np.real(yf1_))
plt.legend(["100Hz","10Hz","100Hz ifft", "10Hz ifft"])
plt.show()

# In here we are applying higher frequency and a lower frequency for the same function. In the lower frequency the
# function is aliasing. Which means this frequency is less than 2fs (<2fs) or less than 2/t(<2/t). To solve this issue
# we can increase the frequency or we can filter out the terms in the function which affects to this.
