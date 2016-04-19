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

'''Mean number of complaints by day of week'''
complaints = pd.read_csv('complaints_dec_2014.csv')
complaints_by_product = complaints[['Date received','Complaint ID']].copy()
cbp = complaints_by_product.rename(columns={'Complaint ID': 'ID'}).copy()
cbp.index = pd.to_datetime(cbp["Date received"], format='%m/%d/%Y')

cbp['days_of_week'] = cbp.index.to_series().map(lambda d: d.weekday())

c = cbp.groupby('days_of_week').size()
c = c.sort_values(ascending=False)
deuce = c.copy()
c

abc = complaints[['Date received','Complaint ID']].copy()
xyz = abc.rename(columns={'Complaint ID': 'ID'})
mcbd = xyz.rename(columns={'Date received': 'Date'})

date_set = set(mcbd.Date)
date_set = sorted(list(date_set))
date_set = pd.to_datetime(date_set, format='%m/%d/%Y')
date_set = date_set.to_series().map(lambda d: d.weekday())
ace = date_set.value_counts()

deuce/ace
