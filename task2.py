Temp=[]
for i in range(5):
    temp=float(input(f"Enter the Temp of Day {i+1} :"))
    Temp.append(temp)
avg=sum(Temp)/5

print("Average temperature of 5 days are: ",+avg)