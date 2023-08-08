import math

from web3 import Web3
from config.logger import logger
from config.rpcs import rpcs


class Bridger:
    def __init__(self):
        pass

    def bridge(self):
       pass

    def get_current_gwei(self):
        web3 = Web3(Web3.HTTPProvider(rpcs["eth"]))
        try:
            gas_price = web3.eth.gas_price
            print("GasPrice: ", round(gas_price / 10**9))
            return gas_price
        except Exception as err:
            print("Ошибка при получении цены газа:", err)
            return None

if __name__ == "__main__":
    Bridger = Bridger()
    print(Bridger.get_current_gwei())