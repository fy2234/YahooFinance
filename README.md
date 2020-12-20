# YahooFinance
Streaming Finance Data with AWS Lambda
# Streaming Finance Data with AWS Lambda

In this project, I provision a Lambda function to generate near real time finance data record for interactive querying. 

I collect one full day’s worth of stock HIGH and LOW prices for 10 companies on Tuesday, December 1st 2020, at a five minute interval. Here I choose to use the `history` function in the yfinance module and get a previous day’s data. I generate kinesis stream to hold the data. 

I configure AWS Glue and AWS Athena to interactively query the S3 file generated by the Lambda function. 

Finally I use Jupyter notebook to analyze the query result and generate four plots. 



