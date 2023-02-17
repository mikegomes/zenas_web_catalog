import streamlit as st
import snowflake.connector as sf
import pandas as pd

st.title('Zena\'s Athleisure Catalog')

my_cnx = sf.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute('select color_or_style from catalog_for_website')
my_catalog = my_cur.fetchall()

df = pd.DataFrame(my_catalog)

#st.write(df)

color_list = df[0].values.tolist()

option = st.selectbox('Pick a sweatsuit color or style:',list(color_list))
                      
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'
                      
my_cur.execute('select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = ' + option)
df2 = my_cur.fetchone()
                      
st.image(df2[0], width=400, caption=product_caption)
                      
st.write('Price: ', df2[1])
st.write('Sizes Available: ', df2[2])
st.write(df2[3])
