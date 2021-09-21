import requests
import os
from pathlib import Path

PINATA_BASE_URL = 'https://api.pinata.cloud/'
endpoint = 'pinning/pinFileToIPFS'
# Change this to upload a different file
filepath = './vaporwave-autogen/files/images'
headers = {'pinata_api_key': os.getenv('PINATA_API_KEY'),
           'pinata_secret_api_key': os.getenv('PINATA_API_SECRET')}


for root, ds, fs in os.walk(filepath):
    for f in fs:
        fullname = os.path.join(root, f)
        with Path(fullname).open("rb") as fp:
            filename = fullname.split('/')[-1:][0]
            image_binary = fp.read()
            response = requests.post(PINATA_BASE_URL + endpoint,
                                    files={"file": (filename, image_binary)},
                                    headers=headers)
            print(response.json())
