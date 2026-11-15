import numpy as np
ecg_array=np.array([0.3,1.5,0.8,2.4,0.6])
threshold_value=1.0
threshold=ecg_array>threshold_value
print("values above threshold:",ecg_array[ecg_array>threshold_value])


