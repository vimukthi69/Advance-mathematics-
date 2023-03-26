import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.fftpack as sfft
import scipy.signal as signal

img = mpimg.imread(r"./Fruit.jpg")

# --------------- Part a ---------------

#fft
imgf = sfft.fft2(img)
plt.imshow(np.abs(imgf))
# plt.show()

#image with fft shift
imgf = sfft.fftshift(imgf)
plt.imshow(np.abs(imgf))
# plt.show()  this takes lower frequencies to the middle

#remove low frequencies
imgf1 = np.zeros((360,360),dtype=complex)
c = 180
r = 90
for m in range(0,360):
    for n in range(0,360):
        if (np.sqrt(((m-c)**2 + (n-c)**2))>r):
            imgf1[m,n] = imgf[m,n]

img1 = sfft.ifft2(imgf1)
plt.imshow(np.abs(img1))
plt.show()

# --------------- Part b ---------------

#Gaussian filter
kernel = np.outer(signal.gaussian(360, 5), signal.gaussian(360, 5))
kf = sfft.fft2(sfft.ifftshift(kernel))  #freq domain kernel
plt.imshow(np.abs(kf))
#plt.show()
imgf = sfft.fft2(img)
plt.imshow(np.abs(kf))
#plt.show()
img_b = imgf*kf
plt.imshow(np.abs(img_b))
#plt.show()
img1 = sfft.ifft2(img_b)
plt.imshow(np.abs(img1))
plt.show()

# --------------- Part c ---------------

#DCT
imgc = sfft.dct((sfft.dct(img,norm='ortho')).T,norm='ortho')
plt.imshow(imgc)
#plt.show()

#IDCT
img1 = sfft.idct((sfft.idct(imgc,norm='ortho')).T,norm='ortho')
plt.imshow(img1)
plt.show()

#Scaling
imgc2 = imgc[0:240,0:240]
img1 = sfft.idct((sfft.idct(imgc2,norm='ortho')).T,norm='ortho')
plt.imshow(img1)
plt.show()

# --------------- Part d ---------------

#Removing high frequency components
imgc1 = np.zeros((480,480))
imgc1[:120,:120] = imgc[:120,:120]
img1 = sfft.idct((sfft.idct(imgc1,norm='ortho')).T,norm='ortho')
plt.imshow(img1)
plt.show()