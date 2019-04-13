# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:04:47 2018

@author: GnacikM
"""

import requests
import json
import pandas as pd
import numpy as np


def filling_dicto(key1, key2, dicto, new_dict, input_str):
    if key2 in dicto.keys():
        new_dict[key1].append(dicto[key2][input_str])
    else:
        new_dict[key1].append(np.nan)


def convert_data_to_df(data):
    data_dict = {}
    #columns in a data frama,strike_price, call, put
    columns = ['strike','call']
    

    for item in columns:
        data_dict[item]=[]

    for item in data:
        filling_dicto('strike', 'call', item, data_dict, 'strike')
        filling_dicto('call','call', item, data_dict, 'lastPrice')
    df = pd.DataFrame.from_dict(data_dict)
    df = df[columns]
    return  df

def yahoo_fin_opts(ticker, date):
    yahoo_fin = "https://query2.finance.yahoo.com/v7/finance/options/%s?straddle=true&date=%s" % (ticker, date)
    html = requests.get(yahoo_fin)
    steam_json = json.loads(html.text)
    options_data = steam_json['optionChain']['result'][0]['options'][0]['straddles']
    df = convert_data_to_df(options_data)
    return df

def main():
    AAPL_options = yahoo_fin_opts('AAPL', '1592524800')
    GOOG_options = yahoo_fin_opts('GOOG', '1592524800')
    FB_options= yahoo_fin_opts('FB', '1592524800')

if __name__ == '__main__':    
    main()
   
        
        


