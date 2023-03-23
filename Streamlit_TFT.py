import requests
import streamlit as st
import pandas as pd
import datetime
import pytz

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

    utc_timezone = pytz.timezone('UTC')
    central_timezone = pytz.timezone('US/Central')
    epoch_time = data['timestamp']
    dt_utc = datetime.datetime.fromtimestamp(epoch_time / 1000, utc_timezone)
    dt_central = dt_utc.astimezone(central_timezone)
    date_str = dt_central.strftime("%Y-%m-%d %H:%M:%S %Z")

    st.write("Timestamp: %s" % date_str)
    st.dataframe(df)

else:
    print(f"Failed to retrieve {url}. Status code: {response.status_code}")