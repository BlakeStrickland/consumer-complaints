import numpy as np
import pandas as pd
from pandas import DataFrame, Series

'''Complaints per product'''
complaints = pd.read_csv('complaints_dec_2014.csv')
complaints_by_product = complaints[['Product','Complaint ID']].copy()
print(complaints_by_product)
cbp = complaints_by_product.rename(columns={'Complaint ID': 'ID'}).copy()
c = cbp.groupby("Product").size()
c.sort_values(ascending=False)
