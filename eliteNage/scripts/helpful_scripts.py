import os
from brownie import (
    network,
    accounts,
    config,
    interface
)

OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"

def fund_collectible(nft_contracts):
    dev = get_account()
    link_token = interface.LinkTokenInterface(config['networks'][network.show_active()]['link_token'])
    link_token.transfer(nft_contracts, 100000000000000000, {'from': dev})

def get_account():
    return accounts.add(config["wallets"]["from_key"])