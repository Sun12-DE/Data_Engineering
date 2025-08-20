#[Customer_ID,Account_Balance,Credit_Score,Transaction_Count,Years_Active]
# [0,1,2,3,4]

import numpy as np
banking_data=np.array([
    [101,20000,775,25,10],
    [102,25000,300,30,15],
    [103,40000,400,15,20],
    [104,400000,800,100,40],
    [105,100000,900,50,21],
    [106,90000,750,100,2],
    [107,3000,301,100,5],
    [108,1000,550,20,2],
    [109,35000,600,30,10],
    [110,80000,825,25,1]])

customer_id=banking_data[:,0]
print(customer_id)