import matplotlib.pyplot as plt
import numpy as np
import serial
import time


Fs = 10.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,10,Ts) # time vector; create Fs samples between 0 and 1.0 sec.
xd = np.arange(0,10,Ts) # signal vector; create Fs samples
yd = np.arange(0,10,Ts)
zd = np.arange(0,10,Ts)
td = np.arange(0,10,Ts)
#n = len(y) # length of the signal
#k = np.arange(n)
#T = n/Fs
#frq = k/T # a vector of frequencies; two sides frequency range
#frq = frq[range(int(n/2))] # one side frequency range
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev,115200)
for x in range(0, 100):
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    xd[x] = float(line)
    line=s.readline()
    yd[x] = float(line)
    line=s.readline()
    zd[x] = float(line)
    line=s.readline()
    td[x] = float(line)

#Y = np.fft.fft(y)/n*2 # fft computing and normalization
#Y = Y[range(int(n/2))] # remove the conjugate frequency parts
fig, ax = plt.subplots(2, 1)
ax[0].plot(t,xd, label='x')
ax[0].plot(t,yd, label='y')
ax[0].plot(t,zd, label='z')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[0].legend(loc='upper right')

ax[1].plot(t,td,) # plotting the spectrum
ax[1].set_xlabel('Time')
ax[1].set_ylabel('horizontal')
plt.show()
s.close()