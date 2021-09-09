#!/usr/bin/python3
from brownie import EliteNagGang, accounts, config
from scripts.helpful_scripts import fund_collectible, get_account
import time
import os
countCollectible = int(os.getenv('COUNT_COLLECTIBLE')) if os.getenv('COUNT_COLLECTIBLE') else 1

def main():
    for i in range(countCollectible):
        dev = get_account()
        print('EliteNagGang', EliteNagGang)
        EliteNagGang_collectible = EliteNagGang[len(EliteNagGang) - 1]
        print('count', EliteNagGang_collectible.getCounterCollect())
        fund_collectible(EliteNagGang_collectible.address)
        token_id = EliteNagGang_collectible.createCollectible({"from": dev})
        print("Created collectible tokenId: {}".format(token_id))
