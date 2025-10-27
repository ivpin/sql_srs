import io
import streamlit as st
import pandas as pd
import duckdb

solution = duckdb.sql(answer).df()

with st.sidebar:
    option = st.selectbox(
        "What would you like to review ?",
        ["Joins", "GroupBy", "Window Functions"],
        index=None,
        placeholder="Select a theme..."
    )
    st.write("You selected:", option)

