sampling_rate=int(input("Enter the sampling rate (in Hz): "))
duration=int(input("Enter the duration :"))
total_measurement=sampling_rate*duration
#print("Total measurements for 1 lead:", total_measurement)
number_of_leads=int(input("enter the number of leads:"))
print(f"Total measurements for {number_of_leads}leads:", {total_measurement*number_of_leads})