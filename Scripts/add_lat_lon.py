import pandas as pd

def clean_df(df):
    drop_df = df.loc[df['REPORTER'] == 'Czechia']
    df = df.drop(drop_df.index)
    df['REPORTER'] = df['REPORTER'].replace({'Belgium (incl. Luxembourg \'LU\' -> 1998)':'Belgium'})
    df['REPORTER'] = df['REPORTER'].replace({'Germany (incl. German Democratic Republic \'DD\' from 1991)':'Germany'})
    df['REPORTER'] = df['REPORTER'].replace({'Ireland (Eire)':'Ireland'})
    df['REPORTER'] = df['REPORTER'].replace({'Spain (incl. Canary Islands \'XB\' from 1997)':'Spain'})
    df['REPORTER'] = df['REPORTER'].replace({'France (incl. Saint Barth�lemy \'BL\' -> 2012; incl. French Guiana \'GF\', Guadeloupe \'GP\', Martinique \'MQ\', R�union \'RE\' from 1997; incl. Mayotte \'YT\' from 2014)':'France'})
    df['REPORTER'] = df['REPORTER'].replace({'Italy (incl. San Marino \'SM\' -> 1993)':'Italy'})
    return df

def add_lat_lon(df, pos_countries):
    d_lat = dict(zip(pos_countries['name'], pos_countries['latitude']))
    d_long = dict(zip(pos_countries['name'], pos_countries['longitude']))
    lat = []
    long = []
    for index, row in df.iterrows(): #there are only 500, that's way I iterate over the rows
        lat.append(d_lat[row['REPORTER']])
        long.append(d_long[row['REPORTER']])
    df['Latitude'] = lat
    df['Longitude'] = long
    return df


if __name__ == '__main__':
    df = pd.read_csv('dataset_project_DSA/dataset_india_export/DS-1262527_1_Data.csv')
    pos_countries = pd.read_csv('position_countries.csv')

    print(add_lat_lon(clean_df(df), pos_countries))
