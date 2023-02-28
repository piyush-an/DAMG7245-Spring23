import streamlit as st
import requests
import os
import pandas as pd

BASE_URL = os.getenv("API_URL", "http://localhost:8000")

st.title('Data as a Service - Demo')

# @st.cache_data


def load_data():
    url = f"{BASE_URL}/get_station"
    response = requests.request("GET", url)
    df = pd.read_json(response.text, orient='records')
    return df


data_load_state = st.text('Loading data...')
df = load_data()
if df.empty:
    st.write('No data in db')
else:
    st.dataframe(data=df)
    st.map(df[['LAT', 'LON']])
data_load_state.text("Done!")
