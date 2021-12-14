import pandas as pd
import plotly.express as px


official_df = pd.read_csv('official_dataset.csv')
lat = official_df['Latitude'].unique()
lon = official_df['Longitude'].unique()
official_df_imp = official_df.loc[official_df['FLOW'] == 'IMPORT']
# official_df['Value'] = official_df['Value'].str.strip()
official_df['Value'] = official_df['Value'].str.replace(' ','').replace(':','0')
# print(type(official_df['Value']))
print(official_df['Value'])
official_df['Value'] = official_df['Value'].astype(float)


fig = px.scatter_geo(official_df,
                    lat = 'Latitude',
                    lon = 'Longitude',
                    animation_frame = 'PERIOD',
                    size_max = 55,
                    hover_name = 'REPORTER',
                    size = 'Value',
                    color = 'PARTNER')

fig.update_geos(fitbounds="locations", showcountries = True)

# fig.update_layout(
#         updatemenus=[
#         dict(
#             type = "buttons",
#             direction = "left",
#             active = -1,
#             buttons=list([
#                 dict(
#                     args=[official_df['FLOW'], 'IMPORT'],
#                     label="Import",
#                     method="update"
#                 ),
#                 dict(
#                     args=[official_df['FLOW'], "EXPORT"],
#                     label="Export",
#                     method="update"
#                 )
#             ]),
#             pad={"r": 10, "t": 10},
#             showactive=True,
#             x=0.11,
#             xanchor="left",
#             y=1.1,
#             yanchor="top"
#         ),
#     ]
# )

fig.show()
