invalid_recordings=[]

with open("labels.csv") as file:
    file.readline()  # Skip the header
    valid_count=0
    labels={}
    for line in file:
        data=line.split(",")
        if data[0].strip()=="":
            continue

        if len(data)<2 or data[1].strip() == "":
            invalid_recordings.append(data[0])
            continue

        recording_id=data[0]
        label=data[1].strip() 
        valid_count+=1
        labels[recording_id]=label 
        

    print(f"Total valid recordings: len({valid_count})") 
    print(f"Invalid recordings: len({invalid_recordings})")     
