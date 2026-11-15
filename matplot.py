import numpy as np
import matplotlib.pyplot as plt
ecg_values=np.array([0.2,0.4,0.3,0.8,0.5])
time_values=np.array([0,0.002,0.004,0.006,0.008])
plt.plot(time_values,ecg_values)
plt.scatter(time_values,ecg_values,color='red',s=70)
plt.title("ECG signal")
plt.xlabel("Time(seconds)")
plt.ylabel("Amplitude(mV)")
plt.grid()
plt.show()