import random
import re

from web3 import Web3
from web3.types import Wei

from logger import logger
from config import rpcs, contracts


class Bridger:
    def __init__(self, pk):
        self.pk = pk

    def bridge(self, bridge_amount):
        web3 = Web3(Web3.HTTPProvider(rpcs["eth"]))
        logger.info(f"Successfully connected to {rpcs['eth']}")

        wallet_address = web3.eth.account.from_key(self.pk).address
        wallet_balance = web3.eth.get_balance(wallet_address)

        logger.info(f"Wallet address: {wallet_address}")
        logger.info(f"Balance in ETH network: {web3.from_wei(wallet_balance, 'ether')}")

        try:
            contract = web3.eth.contract(address=Web3.to_checksum_address(contracts["ZoraBridge"]["address"]),
                                         abi=contracts["ZoraBridge"]["abi"])

            bridge_tx = contract.functions.depositTransaction(
                wallet_address,
                bridge_amount,
                100000,
                False,
                b''
            ).build_transaction({
                'from': wallet_address,
                'value': bridge_amount,
                'gas': round(contract.functions.depositTransaction(wallet_address, bridge_amount, 100000, False,
                                                                   b'').estimate_gas(
                    {'from': wallet_address, 'value': bridge_amount,
                     'nonce': web3.eth.get_transaction_count(wallet_address)}) * 1.15),
                'nonce': web3.eth.get_transaction_count(wallet_address)
            }
            )

            signed_bridge_tx = web3.eth.account.sign_transaction(bridge_tx, self.pk)
            raw_bridge_tx_hash = web3.eth.send_raw_transaction(signed_bridge_tx.rawTransaction)
            bridge_tx_hash = web3.to_hex(raw_bridge_tx_hash)

            logger.info(f"Bridge tx hash: {bridge_tx_hash}")

            bridge_tx_receipt = web3.eth.wait_for_transaction_receipt(raw_bridge_tx_hash, timeout=300)

            if bridge_tx_receipt.status == 1:
                logger.info(f"Successfully bridged: {bridge_amount} wei to Zora")
                logger.info(f"Transaction: https://etherscan.io/tx/{bridge_tx_hash}")

            else:
                logger.error("Something went wrong while bridging")

        except Exception as err:
            if "insufficient funds" and "have" in str(err):
                have = int(re.search(r'have (\d+)', err.args[0]['message']).group(1))
                want = int(re.search(r'want (\d+)', err.args[0]['message']).group(1))
                gas = int(re.search(r'gas (\d+)', err.args[0]['message']).group(1))
                logger.error(f"Insufficient funds for gas * price + value. Want: {want} Have: {have} Gas: {gas}")

            elif "insufficient funds" in str(err):
                logger.error(f"Insufficient funds for gas * price + value.")

            else:
                logger.error(f"Something went wrong: {err}")

    @staticmethod
    def get_current_gwei():
        web3 = Web3(Web3.HTTPProvider(rpcs["eth"]))
        try:
            gas_price = web3.eth.gas_price
            current_base_fee = round(gas_price / 10 ** 9)
            logger.info(f"Current base fee: {current_base_fee} gwei")
            return current_base_fee
        except Exception as err:
            logger.error("Error while fetching gas price:", err)
            return None

    @staticmethod
    def choose_random_amount(min_amount_for_bridge, max_amount_for_bridge) -> Wei:
        min_places = len(str(min_amount_for_bridge).split('.')[1])
        max_places = len(str(max_amount_for_bridge).split('.')[1])
        places = max(min_places, max_places)

        random_number = random.uniform(float(min_amount_for_bridge), float(max_amount_for_bridge))
        formatted_string = "{:." + str(places) + "f}"
        formatted_number = float(formatted_string.format(random_number))
        logger.info(f"Random amount: {formatted_number}")


        bridge_amount = Web3.to_wei(float(formatted_number), 'ether')

        return bridge_amount