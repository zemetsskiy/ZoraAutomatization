import asyncio
import re
import random
import string
import time

import web3.exceptions


from web3 import Web3
from logger import logger
from config import rpcs, nft_contract_abi, nft_ZoraCreator_contract_abi, ZoraNFTCreator_contract_abi, JSONExtensionRegistry_contract_abi


class Minter:
    def __init__(self, pk):
        self.pk = pk
        self.collectionAddress = ""

    async def mint(self, nft_address, nft_id: int):
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

            for i in range(5):
                await asyncio.sleep(5)
                try:
                    mint_tx_receipt = web3.eth.wait_for_transaction_receipt(raw_mint_tx_hash, timeout=300)

                    if mint_tx_receipt.status == 1:
                        logger.info(f"Transaction: https://explorer.zora.energy/tx/{mint_tx_hash}")

                    else:
                        logger.error("Something went wrong while minting")
                except web3.exceptions.TransactionNotFound as err:
                    logger.error(f"Something went wrong while minting: {err}")
                    continue
                except Exception as err:
                    logger.error(f"Something went wrong while minting: {err}")


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

    async def purchase(self, nft_contract_address, value_to_send): # ZoraCreator1155Impl

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

            for i in range(5):
                await asyncio.sleep(5)
                try:
                    mint_tx_receipt = web3.eth.wait_for_transaction_receipt(raw_mint_tx_hash, timeout=300)

                    if mint_tx_receipt.status == 1:
                        logger.info(f"Transaction: https://explorer.zora.energy/tx/{mint_tx_hash}")
                    else:
                        logger.error("Something went wrong while minting")
                except web3.exceptions.TransactionNotFound as err:
                    logger.error(f"Something went wrong while minting: {err}")
                    continue
                except Exception as err:
                    logger.error(f"Something went wrong while minting: {err}")



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

    async def createERC721(self, name, symbol, mintPrice, mintLimitPerAddress, editionSize, royaltyBPS, description, imageURI): # ZoraNFTCreator

        web3 = Web3(Web3.HTTPProvider(rpcs["zora"], request_kwargs={
            'proxies': {'https': 'http://' + "pnorwyha:snmfocltb81h@209.99.165.189:6094",
                        'http': 'http://' + "pnorwyha:snmfocltb81h@209.99.165.189:6094"}}))
        logger.info(f"Successfully connected to {rpcs['zora']}")

        wallet_address = web3.eth.account.from_key(self.pk).address
        wallet_balance = web3.eth.get_balance(wallet_address)

        logger.info(f"Wallet address: {wallet_address}")
        logger.info(f"Balance in ZORA network: {web3.from_wei(wallet_balance, 'ether')}")

        try:
            contract = web3.eth.contract(address=Web3.to_checksum_address("0xA2c2A96A232113Dd4993E8b048EEbc3371AE8d85"), abi=ZoraNFTCreator_contract_abi)

            create_tx = contract.functions.createEdition(
                name=name,
                symbol=symbol,
                editionSize=editionSize,
                royaltyBPS=int(royaltyBPS*100), # royalty = 3% => royaltyBPS = 3*100
                fundsRecipient=wallet_address,
                defaultAdmin=wallet_address,
                saleConfig=[web3.to_wei(mintPrice, 'ether'), mintLimitPerAddress, 1691759829, 18446744073709551615, 0, 0, b"0x000000000000000000000000000000"],
                description=description,
                animationURI="",
                imageURI=imageURI
            ).build_transaction({
                'from': web3.to_checksum_address(wallet_address),
                'nonce': web3.eth.get_transaction_count(wallet_address),
                'maxPriorityFeePerGas': web3.to_wei(0.005, 'gwei'),
                'maxFeePerGas': web3.to_wei(0.005, 'gwei')
            })

            signed_create_tx = web3.eth.account.sign_transaction(create_tx, self.pk)
            raw_create_tx_hash = web3.eth.send_raw_transaction(signed_create_tx.rawTransaction)
            create_tx_hash = web3.to_hex(raw_create_tx_hash)

            logger.info(f"Contract create tx hash: {create_tx_hash}")

            for i in range(5):
                await asyncio.sleep(5)
                try:
                    create_tx_receipt = web3.eth.wait_for_transaction_receipt(raw_create_tx_hash, timeout=300)

                    if create_tx_receipt.status == 1:
                        log = create_tx_receipt['logs'][-1]

                        if log:
                            self.collectionAddress = "0x" + log['topics'][2].hex()[-40:]

                        logger.info(f"Created collection address: {self.collectionAddress}")
                        logger.info(f"Transaction: https://explorer.zora.energy/tx/{create_tx_hash}")
                    else:
                        logger.error("Something went wrong while contract creating")

                except Exception as err:
                    logger.error(f"Something went wrong while contract creating: {err}")

        except Exception as err:
            if "insufficient funds" in str(err):
                logger.error(f"Insufficient funds for gas * price + value.")
            else:
                logger.error(f"Something went wrong: {err}")

    async def walletWarmUp1(self, nft_collection_address, uri): # Mint web page update emulating
        web3 = Web3(Web3.HTTPProvider(rpcs["zora"], request_kwargs={
            'proxies': {'https': 'http://' + "pnorwyha:snmfocltb81h@209.99.165.189:6094",
                        'http': 'http://' + "pnorwyha:snmfocltb81h@209.99.165.189:6094"}}))
        logger.info(f"Successfully connected to {rpcs['zora']}")

        wallet_address = web3.eth.account.from_key(self.pk).address
        wallet_balance = web3.eth.get_balance(wallet_address)

        logger.info(f"Wallet address: {wallet_address}")
        logger.info(f"Balance in ZORA network: {web3.from_wei(wallet_balance, 'ether')}")

        try:
            contract = web3.eth.contract(address=Web3.to_checksum_address("0xABCDEFEd93200601e1dFe26D6644758801D732E8"),
                                         abi=JSONExtensionRegistry_contract_abi)

            warm_tx = contract.functions.setJSONExtension(
                    target=Web3.to_checksum_address(nft_collection_address),
                    uri=uri
            ).build_transaction({
                'from': web3.to_checksum_address(wallet_address),
                'nonce': web3.eth.get_transaction_count(wallet_address),
                'maxPriorityFeePerGas': web3.to_wei(0.005, 'gwei'),
                'maxFeePerGas': web3.to_wei(0.005, 'gwei')
            })

            signed_warm_tx = web3.eth.account.sign_transaction(warm_tx, self.pk)
            raw_warm_tx_hash = web3.eth.send_raw_transaction(signed_warm_tx.rawTransaction)
            warm_tx_hash = web3.to_hex(raw_warm_tx_hash)

            logger.info(f"Warming up tx hash: {warm_tx_hash}")

            for i in range(5):
                await asyncio.sleep(5)
                try:
                    create_tx_receipt = web3.eth.wait_for_transaction_receipt(raw_warm_tx_hash, timeout=300)
                    if create_tx_receipt.status == 1:
                        logger.info(f"Transaction: https://explorer.zora.energy/tx/{warm_tx_hash}")
                    else:
                        logger.error("Something went wrong while  warming up")
                except web3.exceptions.TransactionNotFound as err:
                    logger.error(f"Something went wrong while  warming up: {err}")
                    continue
                except Exception as err:
                    logger.error(f"Something went wrong while warming up: {err}")

        except Exception as err:
            if "insufficient funds" in str(err):
                logger.error(f"Insufficient funds for gas * price + value.")
            else:
                logger.error(f"Something went wrong: {err}")

    async def walletWarmUp2(self, nft_collection_address, publicSalePrice):  # Mint price updating
        web3 = Web3(Web3.HTTPProvider(rpcs["zora"], request_kwargs={
            'proxies': {'https': 'http://' + "pnorwyha:snmfocltb81h@209.99.165.189:6094",
                        'http': 'http://' + "pnorwyha:snmfocltb81h@209.99.165.189:6094"}}))
        logger.info(f"Successfully connected to {rpcs['zora']}")

        wallet_address = web3.eth.account.from_key(self.pk).address
        wallet_balance = web3.eth.get_balance(wallet_address)

        logger.info(f"Wallet address: {wallet_address}")
        logger.info(f"Balance in ZORA network: {web3.from_wei(wallet_balance, 'ether')}")

        try:
            contract = web3.eth.contract(address=Web3.to_checksum_address(nft_collection_address),
                                         abi=nft_ZoraCreator_contract_abi)

            warm_tx = contract.functions.setSaleConfiguration(
                publicSalePrice=web3.to_wei(publicSalePrice, 'ether'),
                maxSalePurchasePerAddress=4294967295,
                publicSaleStart=int(time.time()),
                publicSaleEnd=18446744073709551615,
                presaleStart=0,
                presaleEnd=0,
                presaleMerkleRoot=b"0x000000000000000000000000000000"
            ).build_transaction({
                'from': web3.to_checksum_address(wallet_address),
                'nonce': web3.eth.get_transaction_count(wallet_address),
                'maxPriorityFeePerGas': web3.to_wei(0.005, 'gwei'),
                'maxFeePerGas': web3.to_wei(0.005, 'gwei')
            })

            signed_warm_tx = web3.eth.account.sign_transaction(warm_tx, self.pk)
            raw_warm_tx_hash = web3.eth.send_raw_transaction(signed_warm_tx.rawTransaction)
            warm_tx_hash = web3.to_hex(raw_warm_tx_hash)

            logger.info(f"Warming up tx hash: {warm_tx_hash}")

            for i in range(5):
                await asyncio.sleep(5)
                try:
                    create_tx_receipt = web3.eth.wait_for_transaction_receipt(raw_warm_tx_hash, timeout=300)
                    if create_tx_receipt.status == 1:
                        logger.info(f"Transaction: https://explorer.zora.energy/tx/{warm_tx_hash}")
                    else:
                        logger.error("Something went wrong while  warming up")
                except web3.exceptions.TransactionNotFound as err:
                    logger.error(f"Something went wrong while  warming up: {err}")
                    continue
                except Exception as err:
                    logger.error(f"Something went wrong while warming up: {err}")

        except Exception as err:
            if "insufficient funds" in str(err):
                logger.error(f"Insufficient funds for gas * price + value.")
            else:
                logger.error(f"Something went wrong: {err}")

    @staticmethod
    def generateUri(length=50, prefix="baf"):
        characters = string.ascii_lowercase + string.digits
        random_chars = ''.join(random.choice(characters) for _ in range(length - len(prefix)))
        return prefix + random_chars
