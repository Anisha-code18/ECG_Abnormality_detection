import numpy as np
ecg_data=[-2,-1,0,1,2]
#min_value=np.min(ecg_data)
#print("Minimum value in the ECG data:", min_value)
#max_value=np.max(ecg_data)
#print("Maximum value in the ECG data:", max_value)

#x = int(input("Enter the value of x: "))
#print("Value of x:", x)
min_value = np.min(ecg_data)
max_value = np.max(ecg_data)
norm=(ecg_data-min_value)/(max_value-min_value)#to perform normalization of the data on the entire array at once using numpy
print("Normalilzed value is:",norm)