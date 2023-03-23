import requests
import streamlit as st
import pandas as pd

select_tft_json = st.sidebar.selectbox(
    "Select JSON",
    ("bulk-beasts", "bulk-breach", "bulk-compasses", "bulk-expedition", "bulk-heist", "bulk-invitation", "bulk-legion-jewels",
     "bulk-lifeforce", "bulk-maps", "bulk-sets", "bulk-simulacrum", "bulk-stacked-deck", "bulk-vessel", "bulk-watcher's-eye",
     "hideout", "service")
)

url = f"https://raw.githubusercontent.com/The-Forbidden-Trove/tft-data-prices/master/lsc/{select_tft_json}.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data['data'])
    st.write(data['timestamp'])
    st.dataframe(df)
    # Process the JSON data here
else:
    print(f"Failed to retrieve {url}. Status code: {response.status_code}")