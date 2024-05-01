import streamlit as st
import pandas as pd

import temperatura
import auxiliar


st.set_page_config(
    page_title="Análise de Clima da Austrália",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="Back.jpg"
)

st.markdown(
    f'<h1 style="text-align: center; font-family: Helvetica; font-size: 36px;">Análise de Clima da Austrália</h1>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    div[class*="stTextInput"] label {
    font-size: 35px;
    color: red;
}

# div[class*="stSelectbox"] label {
#     font-size: 35px;
#     color: red;
# }
#     </style>
#     """,
    unsafe_allow_html=True,
)

############################ IMPORTAR BASE #################################
df = pd.read_csv('weatherAUS.csv')


##########################  TRATAR BASE ####################################

df = auxiliar.df_tratar(df)

min_date = df['Date'].min().date()
max_date = df['Date'].max().date()


########################### INTERFACE ######################################

selected_dates = st.slider("Selecione o intervalo de datas:",
                           min_value=min_date,
                           max_value=max_date,
                           value=(min_date, max_date),
                           format="MM-DD-YYYY")

fig = temperatura.plot_temp(df,selected_dates)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

selected_location = st.selectbox("Selecione uma localização:",df['Location'].unique())

df_export = temperatura.generate_df(df,selected_dates,selected_location)

st.table(df_export.head(15))

if st.button('Pressione para Download!'):
        temperatura.download_df(df_export,selected_dates,selected_location)





