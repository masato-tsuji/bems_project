import streamlit as st
import pandas as pd
import requests
import plotly.express as px

from utils.api_client import get_hello


st.title("Energy Visualization Dashboard")

if st.button("Fetch greeting from backend"):
    result = get_hello()
    st.write(result)


# backendのFastAPI からデータ取得
response = requests.get("http://127.0.0.1:8000/api/sample")
data = response.json()

df = pd.DataFrame(data)

st.title("Sample Data Plot")
fig = px.line(df, x="date", y="value", title="Sample Time Series")
st.plotly_chart(fig)