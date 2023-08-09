import re

from web3 import Web3
from logger import logger
from config import rpcs, nft_contract_abi, nft_ZoraCreator_contract_abi


class Minter:
    def __init__(self, pk):
        self.pk = pk

    def mint(self, nft_address, nft_id: int):
        web3 = Web3(Web3.HTTPProvider(rpcs["zora"], request_kwargs={'proxies':{'https': 'http://' + "pnorwyha:snmfocltb81h@209.99.165.189:6094", 'http': 'http://' + "pnorwyha:snmfocltb81h@209.99.165.189:6094"}}))
        logger.info(f"Successfully connected to {rpcs['zora']}")

        wallet_address = web3.eth.account.from_key(self.pk).address
        wallet_balance = web3.eth.get_balance(wallet_address)

        logger.info(f"Wallet address: {wallet_address}")
        logger.info(f"Balance in ZORA network: {web3.from_wei(wallet_balance, 'ether')}")

        try:
            contract = web3.eth.contract(address=Web3.to_checksum_address(nft_address), abi=nft_contract_abi)

            mint_tx = contract.functions.mint(
                "0x169d9147dFc9409AfA4E558dF2C9ABeebc020182",
                nft_id,
                1,
                Web3.to_hex(b'\x00' * 12 + Web3.to_bytes(hexstr=wallet_address)),
            ).build_transaction({
                'from': web3.to_checksum_address(wallet_address),
                'value': web3.to_wei(0.000777, 'ether'),
                'gas': 150000,
                #'gasPrice': web3.to_wei(0.005, 'gwei'),
                'nonce': web3.eth.get_transaction_count(wallet_address),
                'maxPriorityFeePerGas': web3.to_wei(0.005, 'gwei'),
                'maxFeePerGas': web3.to_wei(0.005, 'gwei')
            })

            signed_mint_tx = web3.eth.account.sign_transaction(mint_tx, self.pk)
            raw_mint_tx_hash = web3.eth.send_raw_transaction(signed_mint_tx.rawTransaction)
            mint_tx_hash = web3.to_hex(raw_mint_tx_hash)

            logger.info(f"Mint tx hash: {mint_tx_hash}")

            mint_tx_receipt = web3.eth.wait_for_transaction_receipt(raw_mint_tx_hash, timeout=300)

            if mint_tx_receipt.status == 1:
                logger.info(f"Transaction: https://explorer.zora.energy/tx/{mint_tx_hash}")

            else:
                logger.error("Something went wrong while minting")

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

    def collect_ZoraCreator(self, nft_contract_address, value_to_send): # ZoraCreator1155Impl

        web3 = Web3(Web3.HTTPProvider(rpcs["zora"], request_kwargs={
            'proxies': {'https': 'http://' + "pnorwyha:snmfocltb81h@209.99.165.189:6094",
                        'http': 'http://' + "pnorwyha:snmfocltb81h@209.99.165.189:6094"}}))
        logger.info(f"Successfully connected to {rpcs['zora']}")

        wallet_address = web3.eth.account.from_key(self.pk).address
        wallet_balance = web3.eth.get_balance(wallet_address)

        logger.info(f"Wallet address: {wallet_address}")
        logger.info(f"Balance in ZORA network: {web3.from_wei(wallet_balance, 'ether')}")

        try:
            contract = web3.eth.contract(address=Web3.to_checksum_address(nft_contract_address), abi=nft_ZoraCreator_contract_abi)

            mint_tx = contract.functions.purchase(
                1
            ).build_transaction({
                'from': web3.to_checksum_address(wallet_address),
                'value': web3.to_wei(value_to_send, 'ether'),
                'gas': 150000,
                # 'gasPrice': web3.to_wei(0.005, 'gwei'),
                'nonce': web3.eth.get_transaction_count(wallet_address),
                'maxPriorityFeePerGas': web3.to_wei(0.005, 'gwei'),
                'maxFeePerGas': web3.to_wei(0.005, 'gwei')
            })

            signed_mint_tx = web3.eth.account.sign_transaction(mint_tx, self.pk)
            raw_mint_tx_hash = web3.eth.send_raw_transaction(signed_mint_tx.rawTransaction)
            mint_tx_hash = web3.to_hex(raw_mint_tx_hash)

            logger.info(f"Mint tx hash: {mint_tx_hash}")

            mint_tx_receipt = web3.eth.wait_for_transaction_receipt(raw_mint_tx_hash, timeout=300)

            if mint_tx_receipt.status == 1:
                logger.info(f"Transaction: https://explorer.zora.energy/tx/{mint_tx_hash}")

            else:
                logger.error("Something went wrong while minting")

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