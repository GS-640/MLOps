import pandas as pd
import os

df = pd.DataFrame({'Name':['GS','SMR'],
                   'Age':['27','27'],
                   'Gender':['M','F']})


data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f'Data saved to {file_path}')