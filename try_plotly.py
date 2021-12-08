import pandas as pd
import plotly.express as px


official_df = pd.read_csv('official_dataset.csv')
lat = official_df['Latitude'].unique()
lon = official_df['Longitude'].unique()
official_df = official_df.loc[official_df['FLOW'] == 'IMPORT']
official_df['Value'] = official_df['Value'].str.repalce(' ','')
official_df['Value'] = pd.to_numeric(official_df['Value'], downcast="float")

fig = px.scatter_geo(official_df,
                    lat = 'Latitude',
                    lon = 'Longitude',
                    animation_frame = 'PERIOD',
                    size_max = 55,
                    hover_name = 'REPORTER',
                    size = 'Value')

fig.show()
