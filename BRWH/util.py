import json
from BRWH.usr import *
import requests
from requests.auth import HTTPBasicAuth
import pickle as pkl
import pandas as pd
#from clickhouse_driver import Client

#credentials = json.loads(open('../credentials.json').read())
#authentication = HTTPBasicAuth(credentials['username'], credentials['password'])

base_url = 'https://api.github.com'


def call_api(postfix):
    data = requests.get(base_url + postfix, auth=authentication)
    return data.json()


def pkl_save(data, path='data/usr.pkl'):
    with open(path, 'wb') as f:
        pkl.dump(data, f)


def pkl_load(path='data/usr.pkl'):
    with open(path, 'rb') as f:
        data = pkl.load(f)
    return data


def csv_save(dataFrame, path='data/usr.csv'):
    dataFrame.to_csv(path, index=False)


def csv_load(path='data/usr.csv'):
    return pd.read_csv(path)


#def clickhouse_client():
#    return Client(host='172.16.199.184', port='9000', database='BRWH')
