# MODULES
from os import system
import time
# - basic
import numpy as np 
import pandas as pd 
# - Binance 
import binance
from binance.client import Client
from binance.websockets import BinanceSocketManager

# grant access
def test_connection(k,s):
    try:
        client = Client(k,s)
        test = client.get_account()
    except:
        print('Can not connect with adresses you gave,\nCheck if you gave them in the right order, first key then secret. \nAlso, you may have missed a character.')
        grant_access = False
        return grant_access, client
    else:
        print(f'successfully connected!\n')
        grant_access = True
        return grant_access, client

# vars
user_api_key = ''
user_api_secret = ''
follower_api_key = ''
follower_api_secret = ''

grant_access = False
while grant_access == False:
    system('cls')
    print('Do not show anyone these adresses!')
    user_api_key = input('What is your api KEY? - ')
    user_api_secret = input('What is your api SECRET? - ')
    print('Testing connection...')
    grant_access, user_client = test_connection(user_api_key,user_api_secret)
    time.sleep(5)

grant_access = False
while grant_access == False:
    system('cls')
    print('Do not show anyone these adresses!')
    follower_api_key = input('What is your followers api KEY? - ')
    follower_api_secret = input('What is your followers api SECRET? - ')
    if follower_api_key or follower_api_secret == user_api_key or user_api_secret:
        print('You can not connect to the same address')
        time.sleep(5)
    else: 
        print('Testing connection...')
        grant_access, follower_client = test_connection(follower_api_key,follower_api_secret)
        time.sleep(5)

print('You are connected.')


