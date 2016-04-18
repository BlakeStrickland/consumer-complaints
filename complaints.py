import numpy as np
import pandas as pd
from pandas import DataFrame, Series

'''Complaints per product'''
complaints = pd.read_csv('complaints_dec_2014.csv')
complaints_by_product = complaints[['Product','Complaint ID']].copy()
cbp = complaints_by_product.rename(columns={'Complaint ID': 'ID'}).copy()
c = cbp.groupby("Product").size()
c.sort_values(ascending=False)

'''Number of complaints by company (top 10 companies only)'''
complaints = pd.read_csv('complaints_dec_2014.csv')
complaints_by_product = complaints[['Company','Complaint ID']].copy()
cbp = complaints_by_product.rename(columns={'Complaint ID': 'ID'}).copy()
c = cbp.groupby("Company").size()
c.sort_values(ascending=False).head(10)

'''Number of complaints by company response'''
complaints = pd.read_csv('complaints_dec_2014.csv')
complaints_by_product = complaints[['Company response','Complaint ID']].copy()
cbp = complaints_by_product.rename(columns={'Complaint ID': 'ID'}).copy()
c = cbp.groupby("Company response").size()
c.sort_values(ascending=False)
