#!/usr/bin/python3
from brownie import SimpleCollectible, AdvancedCollectible, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import get_breed, OPENSEA_FORMAT


# dog_metadata_dic = {
#     "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
#     "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
#     "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
# }
token_uri_dict = {
    0: "https://gateway.pinata.cloud/ipfs/QmcThHHfXBwRW2e7nM1mgkyyTJCqobZYhfmLJ94qP2Vj4M/vaporwave%230.json",
    1: "https://gateway.pinata.cloud/ipfs/QmcThHHfXBwRW2e7nM1mgkyyTJCqobZYhfmLJ94qP2Vj4M/vaporwave%231.json",
    2: "https://gateway.pinata.cloud/ipfs/QmcThHHfXBwRW2e7nM1mgkyyTJCqobZYhfmLJ94qP2Vj4M/vaporwave%232.json",
    3: "https://gateway.pinata.cloud/ipfs/QmcThHHfXBwRW2e7nM1mgkyyTJCqobZYhfmLJ94qP2Vj4M/vaporwave%233.json",
    4: "https://gateway.pinata.cloud/ipfs/QmcThHHfXBwRW2e7nM1mgkyyTJCqobZYhfmLJ94qP2Vj4M/vaporwave%234.json",
    5: "https://gateway.pinata.cloud/ipfs/QmcThHHfXBwRW2e7nM1mgkyyTJCqobZYhfmLJ94qP2Vj4M/vaporwave%235.json",
    6: "https://gateway.pinata.cloud/ipfs/QmcThHHfXBwRW2e7nM1mgkyyTJCqobZYhfmLJ94qP2Vj4M/vaporwave%236.json",
    7: "https://gateway.pinata.cloud/ipfs/QmcThHHfXBwRW2e7nM1mgkyyTJCqobZYhfmLJ94qP2Vj4M/vaporwave%237.json",
    8: "https://gateway.pinata.cloud/ipfs/QmcThHHfXBwRW2e7nM1mgkyyTJCqobZYhfmLJ94qP2Vj4M/vaporwave%238.json",
    9: "https://gateway.pinata.cloud/ipfs/QmcThHHfXBwRW2e7nM1mgkyyTJCqobZYhfmLJ94qP2Vj4M/vaporwave%239.json",
    10: "https://gateway.pinata.cloud/ipfs/QmcThHHfXBwRW2e7nM1mgkyyTJCqobZYhfmLJ94qP2Vj4M/vaporwave%2310.json",
}

def main():
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_advanced_collectibles)
    )
    for token_id in range(number_of_advanced_collectibles):
        print(token_id)
        # breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id, advanced_collectible,
                         token_uri_dict[int(token_id)])
        else:
            print("Skipping {}, we already set that tokenURI!".format(token_id))

    # token_id = 1
    # set_tokenURI(token_id, advanced_collectible, token_uri_dict[int(token_id)])


def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(nft_contract.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
