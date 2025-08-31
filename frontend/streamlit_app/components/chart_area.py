import streamlit as st
import plotly.express as px
import pandas as pd

def render_chart():
    df = pd.DataFrame({
        "time": pd.date_range("2023-01-01", periods=10),
        "value": [i**2 for i in range(10)]
    })
    fig = px.line(df, x="time", y="value", title="Sample Data Trend")
    st.plotly_chart(fig)
