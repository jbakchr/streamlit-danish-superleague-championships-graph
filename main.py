import json

import streamlit as st
import pandas as pd
import plotly.express as px


# Load data
with open("./data.json") as f:
    data: dict = json.load(f)


# Create select box
years = tuple(f"{year - 1} - {year}" for year in range(2025, 1990, -1))
option = st.selectbox("Vælg sæson :", years)


# Turn data by selection into Dataframe and sort
df = pd.DataFrame(data[option])
df_sorted = df.sort_values(by='Mesterskaber')


# Create and show horizontal bar chart
fig = px.bar(df_sorted, x='Mesterskaber', y='Klub', orientation='h', title='Flest danske Superliga fodboldmesterskaber (1991 - 2025)', range_x=[0, 16])
fig.update_layout(xaxis=dict(tick0=0, dtick=1))
st.plotly_chart(fig)