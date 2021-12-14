import requests
import pandas as pd

# Download the csv with every country and the position (latitude and longitude)
url = 'https://developers.google.com/public-data/docs/canonical/countries_csv'
html = requests.get(url).content
df_list = pd.read_html(html)
df_position = df_list[-1]

#read the c
complete_dataset = pd.read_csv('official_dataset.csv')


print(list(set(complete_dataset['REPORTER'])))
l = []
print(list(df_position['name']))
for i in list(df_position['name']):
    l.append(i in list(set(complete_dataset['REPORTER'])))
print(l)

print(df_position[l])
df_position = df_position[l]
# df_position[df_position['country'].index.item() in list(set(complete_dataset['REPORTER']))]
# df_position.filter(df_position['country'] in list(set(complete_dataset['REPORTER'])), axis = 0)
df_position.to_csv('position_countries.csv')
