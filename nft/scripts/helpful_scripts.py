from brownie import (
    network,
    accounts,
    config,
    interface
)

def fund_advanced_collectible(nft_contracts):
    dev = accounts.add(config['wallets']['from_key'])
    link_token = interface.LinkTokenInterface(config['network'][network.show_active()]['link_token'])
    link_token.transfer(nft_contracts, 100000000000000000, {'from': dev})
