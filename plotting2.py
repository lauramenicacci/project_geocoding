import webbrowser
import pandas as pd
import plotly.express as px

complete_dataset = pd.read_csv('complete_dataset.csv')
position_countries = pd.read_csv('position_countries.csv')
lat = position_countries['latitude'].mean()
print(lat)
lon = position_countries['longitude'].mean()

indiaEx_try = complete_dataset.loc[(complete_dataset['PERIOD'] == 'Jan. 2020') & \
                            (complete_dataset['PARTNER'] == 'India') &\
                            (complete_dataset['FLOW'] == 'EXPORT')]
# print(indiaEx_try)
export = []
for i in range(indiaEx_try.shape[0]-1):
    export.append(float(indiaEx_try['Value'][i*20].replace(' ',''))/10**7)
#problem with dimension, need ot be fixed!

position_countries['export'] = export

fig = px.scatter_geo(position_countries, # work on the dataframe position_countries
                     lon = "longitude",  # so modify it as you need!
                     lat = "latitude",
                     projection="natural earth",
                     hover_name = "name",
                     size = 'export')

fig.update_traces(marker = dict(color = "green"))

fig.update_geos(fitbounds="locations", showcountries = True)

fig.show()
