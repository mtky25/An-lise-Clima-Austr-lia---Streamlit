import pandas as pd
import plotly.graph_objects as go

def tratar_temp(df,selected_dates):
   start_date = pd.to_datetime(selected_dates[0])
   end_date = pd.to_datetime(selected_dates[1])

   df_temp = df.copy()
   df_temp = df_temp[(df_temp['Date'] >= start_date) & (df_temp['Date'] <= end_date)]


   df_temp.drop(['Rainfall', 'Evaporation',
       'Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
       'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
       'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
       'Temp3pm', 'RainToday', 'RainTomorrow'],axis = 1, inplace=True)
   df_temp['temp_media'] = (df_temp['MinTemp'] + df_temp['MaxTemp']) / 2

   return df_temp 
   
def plot_temp(df,selected_dates):
   color_scale = [
   [0.0, "blue"],    # cold
   [0.5, "yellow"], # neutral
   [1.0, "red"]   # good
   ]

   df_temp = tratar_temp(df,selected_dates)

   df_temp = df_temp.groupby('Location').mean()
   df_temp = df_temp.reset_index()
   df_temp = df_temp.sort_values('temp_media', ascending=False)

   bar_data = go.Bar(
    x=df_temp['Location'], 
    y=df_temp['temp_media'],
    marker=dict(
        color=df_temp['temp_media'],  # Define a cor baseada nos valores de 'temp_media'
        cmin=df_temp['temp_media'].min(),  # Define o mínimo da escala de cores
        cmax=df_temp['temp_media'].max(),  # Define o máximo da escala de cores
        colorscale=color_scale  # Aplica a escala de cores
    )
      )

      # Criando a figura e adicionando o gráfico de barras
   fig = go.Figure(data=bar_data)
   fig.update_layout(
         title='Gráfico de Barras Ordenado por Temperatura Média',
         xaxis_title="Localização",
         yaxis_title="Temperatura Média"
      )
   return fig


def generate_df(df,selected_dates,location):
   
    df_temp = tratar_temp(df,selected_dates)
    df_temp = df_temp[(df_temp['Location'] == location)]
    return df_temp


def download_df(df,selected_dates,location):
   df.to_excel(f'temperatura_{location}_{selected_dates[0]}_{selected_dates[1]}.xlsx')