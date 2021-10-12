import pandas as pd

list = ['dataset_india_export','dataset_india_import','dataset_brazil_export','dataset_brazil_import',
        'dataset_china_export','dataset_china_import','dataset_russia_export','dataset_russia_import',
        'dataset_us_export','dataset_us_import','dataset_southafr_export','dataset_southafr_import']

df_list = []
for i in list:
    print(i)
    # the next line of code don't work on IOS, substitute // with \
    PATH = 'dataset_project_DSA\\'+ i +'\\DS-1262527_1_Data.csv'
    data = pd.read_csv(PATH)
    df_list.append(data)

final_dataset = pd.concat(df_list)
final_dataset.to_csv('complete_dataset.csv')
