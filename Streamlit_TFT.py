import requests
import streamlit as st
import pandas as pd

url = "https://raw.githubusercontent.com/The-Forbidden-Trove/tft-data-prices/master/lsc/bulk-beasts.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data['timestamp'])
    for item in data['data']:
        print(item)
    df = pd.DataFrame(data)
    st.dataframe(df)
    # Process the JSON data here
else:
    print(f"Failed to retrieve {url}. Status code: {response.status_code}")