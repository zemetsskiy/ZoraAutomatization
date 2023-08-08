import time

from logger import logger
from Bridger import Bridger


if __name__ == "__main__":
    with open("private_keys.txt", "r") as file:
        logger.info("Getting private keys")
        private_keys = [private_key.strip() for private_key in file]

    for pk in private_keys:
        Bridger = Bridger(pk)

        duration = 5 * 60

        start_time = time.time()

        while time.time() - start_time < duration:
            current_base_fee = Bridger.get_current_gwei()
            if current_base_fee < 20:
                start_time = time.time()
                break
            else:
                Bridger.bridge(Bridger.choose_random_amount(0.0085, 0.009))
                time.sleep(1)

