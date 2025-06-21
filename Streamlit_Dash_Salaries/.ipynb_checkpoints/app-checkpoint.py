import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import urllib
import altair as alt

# 1. Engine (same as in etl.py)
odbc_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SWERVOPC;DATABASE=AnalyticsDB;"
    "Trusted_Connection=yes;"
)
conn_str = "mssql+pyodbc:///?odbc_connect=" + urllib.parse.quote_plus(odbc_str)
engine = create_engine(conn_str, fast_executemany=True)

# 2. Load tables
@st.cache_data(ttl=300)
def load_table(name):
    query = f"Select * FROM dbo.{name}"
    return pd.read_sql_query(query, engine)

raw  = load_table("careers_raw")
reg  = load_table("meaning_vs_salary")
cat  = load_table("category_summary")

# 3. UI
st.title("Career Analysis Dashboard")

st.header("Raw Data by Rank")
st.dataframe(raw.head(100))

st.header("Meaning vs Salary Regression")
chart = (
    alt.Chart(reg)
    .transform_regression('% High Meaning', 'Mid-Career Pay', method="linear", as_=['% High Meaning', 'Predicted Salary'])
    .mark_line(color='green')
    .encode(x='% High Meaning:Q', y='Predicted Salary:Q')
    +
    alt.Chart(reg)
    .mark_circle(size=60)
    .encode(
        x='% High Meaning:Q',
        y='Mid-Career Pay:Q',
        tooltip=['Major:N', '% High Meaning:Q', 'Mid-Career Pay:Q']
    )
)
st.altair_chart(chart.interactive(), use_container_width=True)


st.header("Category Summary")
st.bar_chart(cat.set_index("Category")["Mid-Career Pay"])