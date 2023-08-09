from logger import logger
from Bridger import Bridger
from Minter import Minter


if __name__ == "__main__":
    with open("private_keys.txt", "r") as file:
        logger.info("Getting private keys")
        private_keys = [private_key.strip() for private_key in file]

    for pk in private_keys:
        #Bridger = Bridger(pk)
        #Bridger.get_current_gwei()
        #time.sleep(10)
        #Bridger.bridge(Bridger.choose_random_amount(0.0081, 0.0085))

        Minter = Minter(pk)

        #Minter.mint("0x4c0c2dd31d2661e8bcec60a42e803dcc6f81baad", 7)
        #Minter.mint("0x5ca17551b686baf0c6bd7727e153b95be9b1ae0d", 1)

        #Minter.collect_ZoraCreator("0x34573d139A15e5d3D129AD6AE20c3C8B221fD921", 0.001007)
        #Minter.collect_ZoraCreator("0xbc8ae1adbfb0052babae00d3211f0be30f1fbd5c", value_to_send=0.000777)


