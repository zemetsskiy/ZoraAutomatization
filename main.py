import asyncio
import time

from logger import logger
from Bridger import Bridger
from Minter import Minter
from IPFS import IPFS


async def run():
    with open("private_keys.txt", "r") as file:
        logger.info("Getting private keys")
        private_keys = [private_key.strip() for private_key in file]

    for pk in private_keys:
        #bridger = Bridger(pk)
        #Bridger.get_current_gwei()
        #time.sleep(10)
        #bridger.eth_zora_bridge(Bridger.choose_random_amount(0.008123, 0.008909))
        #time.sleep(60) Wait some time
        minter = Minter(pk)

        #minter.purchase("0x3f1201a68b513049f0f6e182f742a0dce970d8cd", value_to_send=0.000777)
        #time.sleep(33)
        #minter.mint("0x5ca17551b686baf0c6bd7727e153b95be9b1ae0d", 1)
        #time.sleep(60)
        #minter.mint("0x4c0c2dd31d2661e8bcec60a42e803dcc6f81baad", 7)


        #minter.purchase("0x34573d139A15e5d3D129AD6AE20c3C8B221fD921", value_to_send=0.001007)
        #minter.purchase("0xbc8ae1adbfb0052babae00d3211f0be30f1fbd5c", value_to_send=0.000777)
        #time.sleep(60)
        #minter.purchase("0xcba60a105b5c2fdaf9dd27e733132cc4f7ac9a66", value_to_send=0.000777)
        #minter.purchase("0xd4889d519b1ab9b2fa8634e0271118de480f6d32", value_to_send=0.000777)
        #minter.purchase("0xcdc9c8060c7c357ee25cd80455cbe05b226d291f", value_to_send=0.000778)
        #minter.purchase("0xf6087d1e9be8b71b339a4a80f31e8826af9d0fbb", value_to_send=0.000777)

        try:
            hash = await IPFS.upload("1.png")
        except RuntimeError:
            hash = "bafkreid65aasswl5lzt6sa6eqzcft3fbuwvtqew57hb53y6x3au2q7tq3m"

        await minter.createERC721(name="Something", symbol="STH", description="Hey",  mintPrice=1, mintLimitPerAddress=5, editionSize=3, royaltyBPS=2.3, imageURI=f"ipfs://{hash}")


if __name__ == "__main__":
    asyncio.run(run())
