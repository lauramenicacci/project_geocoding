import pandas as pd
import plotly.express as px


official_df = pd.read_csv('..\official_dataset.csv')
lat = official_df['Latitude'].unique()
lon = official_df['Longitude'].unique()

#subset dataset for import data
official_df_imp = official_df.loc[official_df['FLOW'] == 'IMPORT']
official_df_imp['Value'] = official_df_imp['Value'].str.replace(' ','').replace(':','0')
official_df_imp['Value'] = official_df_imp['Value'].astype(float)

#prepare dynamic map which shows evolution of imports over a two-year time
#the bubbles represent the size of imports of each EU countries from BRICS and USA
#it is possible to filter by partner and select the period to visualize

fig = px.scatter_geo(official_df_imp,
                    lat = 'Latitude',
                    lon = 'Longitude',
                    animation_frame = 'PERIOD',
                    size_max = 55,
                    hover_name = 'REPORTER',
                    size = 'Value',
                    color = 'PARTNER',
                    title="IMPORTS of EU countries from BRICS and USA")

fig.update_geos(fitbounds="locations", showcountries = True)
#plot map
fig.show()


#plot dynamic map which shows evolution of exports over a two-year time
#the bubbles represent the size of exports from each EU countries to BRICS and USA
#it is possible to filter by partner and select the period to visualize

official_df_exp = official_df.loc[official_df['FLOW'] == 'EXPORT']
official_df_exp['Value'] = official_df_exp['Value'].str.replace(' ','').replace(':','0')
official_df_exp['Value'] = official_df_exp['Value'].astype(float)


fig = px.scatter_geo(official_df_exp,
                    lat = 'Latitude',
                    lon = 'Longitude',
                    animation_frame = 'PERIOD',
                    size_max = 55,
                    hover_name = 'REPORTER',
                    size = 'Value',
                    color = 'PARTNER',
                    title="EXPORTS from EU countries to BRICS and USA")

fig.update_geos(fitbounds="locations", showcountries = True)
#plot map
fig.show()

