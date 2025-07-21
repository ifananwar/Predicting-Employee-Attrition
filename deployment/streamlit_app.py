import streamlit as st
import prediction
import eda

st.set_page_config(
    page_title='HR Analytics Prediction Attrition',
    layout='wide',
    initial_sidebar_state='expanded'
)



page = st.sidebar.selectbox('Pilih halaman', ('EDA',"Prediction"))

if page == 'EDA':
    eda.run()

else:
    prediction.run()