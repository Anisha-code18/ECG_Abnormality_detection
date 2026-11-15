import numpy as np
ecg_data=np.array([-2,-1,0,1,2])
mean_value=np.mean(ecg_data)
print("Mean value=",mean_value)
std_value=np.std(ecg_data)
print("Standard deviation=",std_value)
standardized_data=(ecg_data-mean_value)/(std_value)
print("Standardized value=",standardized_data)