#!/usr/bin/python3
import os
import requests
import json
from brownie import EliteNagGang, network
from metadata import sample_metadata
from pathlib import Path
import db

def main():
    print("Working on " + network.show_active())
    elitenaggang_collectible = EliteNagGang[len(EliteNagGang) - 1]
    number_of_elitenaggang_collectible = elitenaggang_collectible.getCounterCollect()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_elitenaggang_collectible)
    )
    write_metadata(number_of_elitenaggang_collectible, advanced_collectible)


def write_metadata(token_ids, nft_contract):
    for token_id in range(token_ids):
        print('token_id', token_id)
        collectible_metadata = sample_metadata.metadata_template
        token_id_str = str(token_id)
        metadata_file_name = (
            "./metadata/{}/".format(network.show_active())
            + str(token_id)
            + "-"
            + token_id_str
            + ".json"
        )
        if Path(metadata_file_name).exists():
            print(
                "{} already found, delete it to overwrite!".format(
                    metadata_file_name)
            )
        else:
            print("Creating Metadata file: " + metadata_file_name)
            collectible_metadata["name"] = get_breed(
                nft_contract.tokenIdToBreed(token_id)
            )
            collectible_metadata["description"] = "An adorable {} pup!".format(
                collectible_metadata["name"]
            )
            image_to_upload = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_path = "./img/{}.png".format(
                    token_id_str)
                image_to_upload = upload_to_ipfs(image_path)
            collectible_metadata["image"] = image_to_upload
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            metadata_url = None
            if os.getenv("UPLOAD_IPFS") == "true":
                metadata_url = upload_to_ipfs(metadata_file_name)
            insertMetadataIfNotExist({'tokenId': token_id, 'metadata': collectible_metadata, 'imgUrl': image_to_upload, 'metadata_url': metadata_url})

def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = (
            os.getenv("IPFS_URL")
            if os.getenv("IPFS_URL")
            else "http://localhost:5001"
        )
        response = requests.post(ipfs_url + "/api/v0/add",
                                 files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = "https://ipfs.io/ipfs/{}?filename={}".format(
            ipfs_hash, filename)
        print(image_uri)
    return image_uri