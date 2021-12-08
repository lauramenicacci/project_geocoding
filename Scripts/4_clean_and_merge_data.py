import pandas as pd
import add_lat_lon_3
import os

def merge_database(complete_df, already_merged = []):
    l = []
    for dir in  os.listdir(str(os.getcwd()) + '/dataset_project_DSA'):
        if dir[0:4] == 'data' and dir not in already_merged:
            PATH = str(os.getcwd() + '/dataset_project_DSA/'+ dir +'/DS-1262527_1_Data.csv')
            data = pd.read_csv(PATH)
            data = add_lat_lon_3.clean_df(data)
            pos_countries = pd.read_csv(str(os.getcwd() + '/dataset_project_DSA/position_countries.csv'))
            data = add_lat_lon_3.add_lat_lon(data, pos_countries)
            l.append(data)
            already_merged.append(dir)
    datas = pd.concat(l)
    return datas, already_merged

if __name__ == '__main__':
    tup = merge_database([])
    tup[0].to_csv('./official_dataset.csv')
