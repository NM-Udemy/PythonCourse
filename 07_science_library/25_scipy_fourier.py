# 25_scipy_fourier.py
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as plt


N = 800 # サンプルのポイント数
T = 1.0 # 秒数


x = np.linspace(0.0, T, N)
y = np.sin(50.0 * 2.0 * np.pi * x)\
     + 0.5 * np.sin(80.0 * 2.0 * np.pi * x) + 5 * np.random.rand(N)
plt.subplot(3,1,1)
plt.plot(x,y)

yf = fft(y) # 0..NのArray。0...N//2-1: 正の周波数、N//2・・・N-1: 負の周波数

print(yf[:5])

xf = np.linspace(0.0, N * T/2, N//2) # 各周波数
plt.subplot(3,1,2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.ylim([0, 1.5])

z = ifft(yf)
plt.subplot(3,1,3)
plt.plot(x, z)

plt.show()