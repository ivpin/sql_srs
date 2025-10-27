import io
import streamlit as st
import pandas as pd
import duckdb

csv = '''
beverage, price
orange juice,2.5
Expresso,2
Tea,3
'''
beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item, food_price
cookie juice,2.5
chocolatine,2
muffin,3
'''
food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with st.sidebar:
    option = st.selectbox(
        "What would you like to review ?",
        ["Joins", "GroupBy", "Window Functions"],
        index=None,
        placeholder="Select a theme..."
    )
    st.write("You selected:", option)

st.header("enter your code")
query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = duckdb.sql(query).df()
    st.write(f"Vous avez entré la query suivante : {query}")
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.write(answer)
