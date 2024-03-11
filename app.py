import time
import schedule
import json
import pandas as pd
from os import environ, remove
from pathlib import Path
from ftplib import FTP_TLS

def get_ftp() -> FTP_TLS:
    FTPHOST = environ['FTPHOST']
    FTPUSER = environ['FTPUSER']
    FTPPASS = environ['FTPPASS']

    ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)
    ftp.prot_p()

    return ftp

def read_csv(config: dict) -> pd.DataFrame:            
    url = config["URL"]                                  
    params = config["PARAMS"]                     
    return pd.read_csv(url, **params)

if __name__ == "__main__":

    with open("config.json", "rb") as fp:
        config = json.load(fp)

    # print(config)

    print(read_csv(config["OFAC_SDN"]).head())