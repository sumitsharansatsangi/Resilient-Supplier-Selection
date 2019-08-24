#This program is creating four csv file for generating Dataset for 4 Supplier.
# Here OrderQuantity is same for all te 4 Supplier

import random
import pandas as pd

order_id=list(range(5000))

OrderQuantity=[]
for i in range(5000):
    OrderQuantity.append(random.randint(100,1001))

for t in range(1,5):
    ExpectedDays=[]
    for i in range(5000):
        if(100<=OrderQuantity[i]<=500):
            ExpectedDays.append(random.randint(3,5))
        else:
            ExpectedDays.append(random.randint(6,10))

    ActualDays=[]
    for i in range(5000):
        ActualDays.append(ExpectedDays[i]+random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5]))

    Status=[]
    for i  in range(5000):
        if(ExpectedDays[i]==ActualDays[i]):
            Status.append(1)
        else:
            Status.append(0)

    data = pd.DataFrame(
        {'OrderId':order_id,
         'OrderQuantity': OrderQuantity,
         'ExpectedDays': ExpectedDays,
         'ActualDays':ActualDays,
         'Status':Status
        })

    t=data.to_csv("data_new_"+str(t)+".csv",index=False)
