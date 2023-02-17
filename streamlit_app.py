import streamlit as st
import snowflake.connector as sf
import pandas as pd

st.title('Zena\'s Athleisure Catalog')

my_cnx = sf.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute('select color_or_style from catalog_for_website')
my_catalog = my_cur.fetchall()

df = pd.DataFrame(my_catalog)

streamlit.write(df)

color_list = df[0].values.tolist()
