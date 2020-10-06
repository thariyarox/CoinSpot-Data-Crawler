import pandas as pd
try:
    indata = pd.read_csv('../data/processed_data.csv', encoding='utf-8', header=0)
    indata['difference'] = indata['buy'] - indata['sell']
    indata['bid_percentage'] = (indata['difference'] / indata['sell']) *100
    indata = indata.sort_values(by = ['bid_percentage'])
    indata.to_csv('../data/stats.csv', index=False)
    print('Your output is ready!!')
except FileNotFoundError:
    print('Input File not found !')