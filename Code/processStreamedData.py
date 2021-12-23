import os
from google.cloud import bigquery
import matplotlib.pyplot as plt
import requests
import json
import pandas as pd
import datetime


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="prefab-range-329220-17cd7466865e.json"

bqclient = bigquery.Client()
query_string = """
                SELECT * FROM `prefab-range-329220.crypto.wordcount`
                """
dataframe = (bqclient.query(query_string).result().to_dataframe(create_bqstorage_client=True,))
dataframe.to_csv('crypto_data.csv')

count = dataframe.groupby("word").sum()
dataframe["crypto_count"] = count
dataframe.plot(x="word", y="crypto_count")

endpoint = ''
page = requests.get(endpoint)
data = page.json()['Data']['Data'] 
df = pd.DataFrame(data)
df['time'] = pd.to_datetime(df['time'], unit='s')
df['bitcoin price per day'] = (df['close'])
plt.figure(figsize=(8,8))
plt.title('Daily Bitcoin Price Over 90 Days')
plt.plot(df['time'], df['bitcoin price per day'])
plt.legend()
plt.show()





