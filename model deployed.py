# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import pickle  
loaded_model=pickle.load(open ('C:/Users/Benjamin/Desktop/new phone prediction/phone_sales_data.pkl', 'rb'))
new_phone= pd.DataFrame([{
    'Screen Size (inches)':6.2,
    'RAM (GB)':4,
    'Storage (GB)':64,
    'Battery Capacity (mAh)':4000,
    'Camera Quality (MP)':48, 
}])
predicted_price =loaded_model.predict(new_phone)
print("Predicted Price for new phone:", predicted_price[0])
