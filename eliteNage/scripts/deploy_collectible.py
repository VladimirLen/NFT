import os
from brownie import EliteNagGang, accounts, network, config
from scripts.helpful_scripts import fund_collectible, get_account

def main():
    dev = get_account()
    publish_source = False
    elitenaggang_collectible = EliteNagGang.deploy(
        os.getenv('IPFS_URL'),
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["link_token"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": dev},
        publish_source=publish_source,
    )
    print(elitenaggang_collectible)
    fund_collectible(elitenaggang_collectible)  
    return elitenaggang_collectible