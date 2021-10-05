import pandas as pd
import requests

#creates a df from json api pages. define number pages and target 
def create_payload_df(url, max_pages, target):
    page_list = []
    
    for i in range(1, max_pages + 1):
        response = requests.get(url + "?page=" + str(i))
        data = response.json()
        page_items = data['payload'][target]
        page_list += page_items
        
    return pd.DataFrame(page_list)

#saves a csv to a specified file
def save_csv(location):
    to_csv(location)

#concats dfs
def put_together(dfs):
    pd.concat(df, gnore_index=True)

#read csv from specified location
def opencsv(location):
    pd.read_csv(location)
    