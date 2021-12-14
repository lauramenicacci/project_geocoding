import requests
import pandas as pd

<<<<<<< HEAD
# Download the csv with every country and the position (latitude and longitude)
=======
#Download the csv with countries and positions (latitude and longitude)
>>>>>>> 6e40c3fe69dbfdb78f68303afc83ebfd51df0415
url = 'https://developers.google.com/public-data/docs/canonical/countries_csv'
html = requests.get(url).content
df_list = pd.read_html(html)
df_position = df_list[-1]
<<<<<<< HEAD

#read the c
=======
#import the complete dataset
>>>>>>> 6e40c3fe69dbfdb78f68303afc83ebfd51df0415
complete_dataset = pd.read_csv('official_dataset.csv')

#create list "l" of countries : from position dataset (df_position), select and append only the countries that are also present
# in the official_dataset (Only EU countries)
l = []
for i in list(df_position['name']):
    l.append(i in list(set(complete_dataset['REPORTER'])))
print(l)

# update position dataframe (filtered in the step before)
df_position = df_position[l]
#export dataset
df_position.to_csv('position_countries.csv')
