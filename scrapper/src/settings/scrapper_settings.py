import os
from os.path import join, dirname
from dotenv import load_dotenv

ENV_FILE_NAME='.env'

load_dotenv(join(dirname(__file__), ENV_FILE_NAME))

settings={}

settings['SCRAPPER_WEBPAGE_URL']=os.environ.get("SCRAPPER_WEBPAGE_URL")