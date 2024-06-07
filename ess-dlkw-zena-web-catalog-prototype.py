# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")

# Get the current credentials
session = get_active_session()

df_options = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.SWEATSUITS").select(col('COLOR_OR_STYLE'))
#st.dataframe(data=my_dataframe, use_container_width=True)
#color_list = my_dataframe[0].values.to_list()
#print(color_list)
option = st.selectbox(label='Pick a sweatsuit color or style:', options=df_options)

sql_catalog_item = "select * from zenas_athleisure_db.products.catalog_for_website where color_or_style = '{}'".format(option)
df_catalog_item = session.sql(sql_catalog_item).to_pandas()

try:
    product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!' 
    #st.write(product_caption)
    
    #st.dataframe(data=df_catalog_item, use_container_width=True)
    
    #st.write(df_catalog_item.at[0,'COLOR_OR_STYLE'])
    
    st.image(df_catalog_item.at[0,'DIRECT_URL'], width=400, caption=product_caption)
    st.write('Price: ', df_catalog_item.at[0,'PRICE'])
    st.write('Sizes Available: ', df_catalog_item.at[0,'SIZE_LIST'])
    st.write(df_catalog_item.at[0,'UPSELL_PRODUCT_DESC'])
except:
    st.write("Sweatsuit color or style unavailable")