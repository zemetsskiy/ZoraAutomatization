import httpx
import json
from logger import logger


class IPFS:
    URL = "https://ipfs-uploader.zora.co/api/v0/add?stream-channels=true&cid-version=1&progress=false"

    @staticmethod
    async def upload(filepath):

        file = {'file': ('filename.txt', open(filepath, 'rb'))}

        async with httpx.AsyncClient() as client:
            response = await client.post(IPFS.URL, files=file)

        if response.status_code == 200:
            data = json.loads(response.text)
            hash = data["Hash"]

            logger.info(f"{filepath} successfully uploaded to IPFS")
            logger.info(f"Hash: {hash}")

            return hash

        else:
            logger.error("Something went wrong while uploading to IPFS")
            raise RuntimeError("Something went wrong while uploading to IPFS")