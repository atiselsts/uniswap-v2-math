#!/usr/bin/env python

#
# This script shows how to calculate the amount of tokens in a liquidity pool
# that belong to a specific LP address
#

import os
from abi import v2_pool_abi
from web3 import Web3

PROVIDER_URL = os.getenv("INFURA_URL_MAINNET")

web3 = Web3(Web3.HTTPProvider(PROVIDER_URL))
pair = '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc'
lp_address = '0x76E2E2D4d655b83545D4c50D9521F5bc63bC5329'
contract = web3.eth.contract(address=pair, abi=v2_pool_abi)

reserves = contract.functions.getReserves().call()
reserve_usdc = reserves[0]

total_supply = contract.functions.totalSupply().call()
lp_balance = contract.functions.balanceOf(lp_address).call()
lp_usdc = reserve_usdc * lp_balance / total_supply

usdc_decimals = 6
lp_usdc_adjusted = lp_usdc / 10 ** usdc_decimals

print(f"liquidity provider {lp_address} has {lp_usdc_adjusted} USDC in USDC/WETH pool")
