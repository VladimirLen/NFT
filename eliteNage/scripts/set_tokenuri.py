#!/usr/bin/python3
from brownie import EliteNagGang, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import OPENSEA_FORMAT, get_account
from scripts import db


def main():
    print("Working on " + network.show_active())
    elitenaggang_collectible = EliteNagGang[len(EliteNagGang) - 1]
    number_of_elitenaggang_collectible = elitenaggang_collectible.getCounterCollect()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_elitenaggang_collectible)
    )
    for token_id in range(number_of_elitenaggang_collectible):
        tokenURI = (db.getMetadata(token_id))['metadata_url']
        # if not elitenaggang_collectible.tokenURI(token_id):
        print("Setting tokenURI of {}".format(token_id))
        set_tokenURI(token_id, elitenaggang_collectible, tokenURI)
        # else:
        #     print("Skipping {}, we already set that tokenURI!".format(token_id))

def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = get_account()
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(nft_contract.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
