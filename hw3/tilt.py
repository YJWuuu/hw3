import matplotlib.pyplot as plt
import numpy as np
import serial
import time

Fs = 100.0;  # sampling rate
Ts = 10.0/Fs; # sampling interval
t0 = np.arange(0,10,Ts) # time vector; create Fs samples between 0 and 1.0 sec.
x = np.arange(0,10,Ts) # signal vector; create Fs samples
y = np.arange(0,10,Ts)
z = np.arange(0,10,Ts)

t1 = np.arange(0,10,Ts)
tilt = np.arange(0,10,Ts)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 115200)
s.readline()
s.readline()
s.readline()
for i in range(0, int(Fs)):
    line = s.readline() # Read an echo string from K66F terminated with '\n'
    x[i] = float(line)
    line = s.readline()
    y[i] = float(line)
    line = s.readline()
    z[i] = float(line)
    if (abs(x[i]) >= 0.2 or abs(y[i]) >= 0.2):
        tilt[i] = 1
    else:
        tilt[i] = 0

fig, ax = plt.subplots(2, 1)
ax[0].plot(t0,x, color="blue", label="x")
ax[0].plot(t0,y, color="red", label="y")
ax[0].plot(t0,z, color="green", label="z")
ax[0].legend(loc='upper left', frameon=False)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[1].stem(t1,tilt)
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
plt.show()
s.close()