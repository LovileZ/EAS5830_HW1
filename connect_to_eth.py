import json
from web3 import Web3
from web3.middleware import ExtraDataToPOAMiddleware
from web3.providers.rpc import HTTPProvider

'''
If you use one of the suggested infrastructure providers, the url will be of the form
now_url  = f"https://eth.nownodes.io/{now_token}"
alchemy_url = f"https://eth-mainnet.alchemyapi.io/v2/{alchemy_token}"
infura_url = f"https://mainnet.infura.io/v3/{infura_token}"
'''

def connect_to_eth():
	url = "https://mainnet.infura.io/v3/fd63f35277f44785b28203d0aad096ed"  # FILL THIS IN
	w3 = Web3(HTTPProvider(url))
	assert w3.is_connected(), f"Failed to connect to provider at {url}"
	return w3


def connect_with_middleware(contract_json):
    with open(contract_json, "r") as f:
        d = json.load(f)
        d = d['bsc']
        address = d['address']
        abi = d['abi']

    # The first section will be the same as "connect_to_eth()" but with a BNB url
    url = "https://bsc-testnet.drpc.org"
    w3 = Web3(HTTPProvider(url))
    assert w3.is_connected(), f"Failed to connect to provider at {url}"

    # Inject middleware into the w3 object
    w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

    # Create a contract object
    contract = w3.eth.contract(address=address, abi=abi)

    return w3, contract


if __name__ == "__main__":
	connect_to_eth()
