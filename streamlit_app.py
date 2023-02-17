import streamlit as st
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute('select current_user(), current_account(), current_region()')
my_data_row = my_cur.fetchone()

st.text('Hello from Snowflake')
st.text(my_data_row)
