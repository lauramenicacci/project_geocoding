#import webbrowser
import pandas as pd
import plotly.express as px
import time

complete_dataset = pd.read_csv('complete_dataset.csv')
position_countries = pd.read_csv('position_countries.csv')
lat = position_countries['latitude'].mean()
print(lat)
lon = position_countries['longitude'].mean()

d = complete_dataset.loc[(complete_dataset['PERIOD'] == 'Mar. 2020') & \
                        (complete_dataset['PARTNER'] == 'Brazil') &\
                        (complete_dataset['FLOW'] == 'IMPORT')]


def map_function(partner_country, time_period, Import = True):
    if Import:
        df = complete_dataset.loc[(complete_dataset['PERIOD'] == time_period) & \
                                (complete_dataset['PARTNER'] == partner_country) &\
                                (complete_dataset['FLOW'] == 'IMPORT')]
        Import = []
        index = df.index.tolist()
        for i in index[:-1]:
            if df['Value'][i] == ':':
                df['Value'][i] = '0'
            Import.append(float(df['Value'][i].replace(' ',''))/10**7)
        position_countries['Import'] = Import

        fig = px.scatter_geo(position_countries, # work on the dataframe position_countries
                             lon = "longitude",  # so modify it as you need!
                             lat = "latitude",
                             projection="natural earth",
                             hover_name = "name",
                             size = 'Export')
        fig.update_geos(fitbounds="locations", showcountries = True)
    else:
        df = pd.DataFrame(complete_dataset.loc[(complete_dataset['PERIOD'] == time_period) & \
                            (complete_dataset['PARTNER'] == partner_country) &\
                            (complete_dataset['FLOW'] == 'EXPORT')])
        Export = []
        index = df.index.tolist()
        for i in index[:-1]:
            if df['Value'][i] == ':':
                df['Value'][i] = '0'
            Export.append(float(df['Value'][i].replace(' ',''))/10**7)

        position_countries['Export'] = Export

        fig = px.scatter_geo(position_countries, # work on the dataframe position_countries
                             lon = "longitude",  # so modify it as you need!
                             lat = "latitude",
                             projection="natural earth",
                             hover_name = "name",
                             size = 'Export')

        fig.update_geos(fitbounds="locations", showcountries = True)

    if Import:
        fig.update_traces(marker = dict(color = "pink"))
    else:
        fig.update_traces(marker = dict(color = "blue"))
    return fig


map_function('Brazil','Mar. 2020', Import = False).show()
time.sleep(3)
map_function('Brazil','Mar. 2020').show()

# #
# indiaEx_try = complete_dataset.loc[(complete_dataset['PERIOD'] == 'Jan. 2020') & \
#                              (complete_dataset['PARTNER'] == 'India') &\
#                              (complete_dataset['FLOW'] == 'EXPORT')]
# # # print(indiaEx_try)
# export = []
# for i in range(indiaEx_try.shape[0]-1):
#     export.append(float(indiaEx_try['Value'][i*20].replace(' ',''))/10**7)
# # #problem with dimension, need ot be fixed!
# #
# position_countries['export'] = export
# #
# fig = px.scatter_geo(position_countries, # work on the dataframe position_countries
#                      lon = "longitude",  # so modify it as you need!
#                      lat = "latitude",
#                      projection="natural earth",
#                      hover_name = "name",
#                      size = 'export')
# #
# fig.update_traces(marker = dict(color = "green"))
# #
# fig.update_geos(fitbounds="locations", showcountries = True)
# #
# fig.show()
