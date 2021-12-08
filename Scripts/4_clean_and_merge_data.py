import pandas as pd
import add_lat_lon
import os

def merge_database(compleate_df, already_merged = []):
    for dir in  os.listdir(str(os.getcwd()) + '/dataset_project_DSA'):
        l = []
        if dir[0:4] == 'data' and dir not in already_merged:
            PATH = str(os.getcwd() + '/dataset_project_DSA/'+ dir +'/DS-1262527_1_Data.csv')
            data = pd.read_csv(PATH)
            data = add_lat_lon.clean_df(data)
            data = add_lat_lon.add_lat_lon(data)
            l.append(data)
            already_merged.append(dir)
    datas = pd.concat(l)
    return pd.concat([compleate_df,datas], already_merged)
