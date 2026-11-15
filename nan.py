import numpy as np
ecg_array=np.array([0.2,0.4,np.nan,0.8])
missing_values=np.isnan(ecg_array)
print("Missing values=",missing_values)