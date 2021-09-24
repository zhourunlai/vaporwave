# from web3 import Web3
# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
from web3.auto.infura import w3

# https://web3py.readthedocs.io/en/stable/examples.html#working-with-contracts
address = '0xb50ac03C228162Af67E7265313524a2872DCe54a'
abi = '''
[
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "tokenURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "mint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
'''
contract_instance = w3.eth.contract(address=address, abi=abi)

contract_instance.functions.tokenURI(330).call()
# contract_instance.functions.mint().call()
