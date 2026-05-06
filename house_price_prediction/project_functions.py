import os
import tarfile
import urllib
import requests
from dotenv import load_dotenv

load_dotenv()

HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = os.getenv("DOWNLOAD_ROOT")

def fetch_data(housing_url = HOUSING_URL, housing_path = HOUSING_PATH):
    response = requests.get(housing_url)
    if response.status_code == 200:
        housing_tgz = os.path.join(housing_path, "housing.tgz")
        with open(housing_tgz, "wb") as f:
            f.write(response.content)
        with tarfile.open(housing_tgz,"r:gz") as tar:
            tar.extractall(path = housing_path)
