#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import yfinance
import json
import boto3
def lambda_handler(event, context):
    stock_list = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']
    kinesis = boto3.client("kinesis", "us-east-2")
    for stock in stock_list:
        df = yfinance.Ticker(stock).history(start='2020-12-01', end='2020-12-02', interval='5m')
        for index, row in df.iterrows():
            json_ob = json.dumps({"high": row['High'], "low": row['Low'], "ts": str(index), 'name': stock})+"\n"     
            kinesis.put_record(
                StreamName="stat9760_fifi",
                Data=json_ob,
                PartitionKey="partitionkey")      

