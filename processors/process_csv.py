import pandas as pd
import os

dirname = os.path.dirname(__file__)
try:
    indata = pd.read_csv(os.path.join(dirname,'../data/processed_data.csv'),header=0,encoding='utf-8')
    indata['buy'] = pd.to_numeric(indata['buy'], errors='coerce')
    indata['sell'] = pd.to_numeric(indata['sell'], errors='coerce')
    indata['difference'] = indata['buy'] - indata['sell']
    indata['bid_percentage'] = (indata['difference'] / indata['sell']) *100
    indata = indata.sort_values(by = ['bid_percentage'])
    indata.to_csv(os.path.join(dirname,'../data/stats.csv'), index=False)
    print('Your output is ready!!')
except FileNotFoundError:
    print('Input File not found !')