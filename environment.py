"""
The `environment` module provides a way to load environment variables for use in a Python application. It leverages the `dotenv` package to load environment variables from a `.env` file located in the current working directory.

The following environment variables are loaded by this module:
- `AD_USERNAME`: The username for the Active Directory service account.
- `AD_PASSWORD`: The password for the Active Directory service account.
- `DNA_CENTER_USERNAME`: The username for the Cisco DNA Center service account.
- `DNA_CENTER_PASSWORD`: The password for the Cisco DNA Center service account.
- `VERBOSE`: A boolean value indicating whether verbose logging is enabled. Defaults to False.
- `DEBUG`: A boolean value indicating whether debug logging is enabled. Defaults to False.

By using this module to load environment variables, developers can ensure that sensitive information such as passwords and API keys are not hard-coded in the application. This can improve the security of the application and simplify the management of credentials in a distributed environment.

Note that the `.env` file must be located in the same directory as the Python script that imports this module in order for the environment variables to be loaded.
"""


import os
import sys
import pathlib
from dotenv import load_dotenv


dotenv_current_path = os.path.join(pathlib.Path().resolve(), '.env')
load_dotenv(dotenv_current_path)

AD_USERNAME = os.environ.get("AD_USERNAME")
AD_PASSWORD = os.environ.get("AD_PASSWORD")

DNA_CENTER_USERNAME = os.environ.get("AD_USERNAME")
DNA_CENTER_PASSWORD = os.environ.get("AD_PASSWORD")
DNAC_URL = os.environ.get("DNAC_URL")


BOX_CLIENT_ID = os.environ.get("BOX_CLIENT_ID")
BOX_CLIENT_SECRET = os.environ.get("BOX_CLIENT_SECRET")
BOX_ENTERPRISE_ID = os.environ.get("BOX_ENTERPRISE_ID")
BOX_PUBLIC_KEY_ID = os.environ.get("BOX_PUBLIC_KEY_ID")
BOX_PRIVATE_KEY_DATA = os.environ.get("BOX_PRIVATE_KEY_DATA")
BOX_PRIVATE_KEY_PASSPHRASE = os.environ.get("BOX_PRIVATE_KEY_PASSPHRASE")

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION_NAME = os.environ.get("AWS_REGION_NAME")

PROXMOX_HOST = os.environ.get("PROXMOX_HOST")
PROXMOX_USER = os.environ.get("PROXMOX_USER")
PROXMOX_PASSWORD = os.environ.get("PROXMOX_PASSWORD")

HOME_MYSQL_HOST= os.environ.get("HOME_MYSQL_HOST")
HOME_MYSQL_USERNAME = os.environ.get("HOME_MYSQL_USERNAME")
HOME_MYSQL_PASSWORD = os.environ.get("HOME_MYSQL_PASSWORD")

VERBOSE = os.environ.get("VERBOSE")
DEBUG = os.environ.get("DEBUG")