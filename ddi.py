import json
import os
import requests
import requests_auth

from mydict import MyDict

TOKEN = None

DDI_DATA_PATH = os.environ.get("DDI_DATA_PATH")

DDI_DUMP_PATH = os.environ.get("DDI_DUMP_PATH")


# There are 3 different environments for DDI. Authentication is the same for all 3 using OKTA
URL_SANDBOX = "https://s5-infcoreddi-apim-01.azure-api.net/"
URL_NON_PROD = "https://n5-infcoreddi-apim-01.azure-api.net/"
URL_PROD = "https://p5-infcoreddi-apim-01.azure-api.net/"