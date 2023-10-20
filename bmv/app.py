
import os
import click
import requests
from dotenv import load_dotenv
import pprint

load_dotenv()

API_TOKEN = os.getenv('BMV_API_TOKEN')
watchlist: list = [
    'FIBRAMQ12',
    'DANHOS13',
    'FMTY14',
    # 'FUNO11',
    # 'MAYAB',
    # 'ACTIGOBB',
]

endpoints: dict = {
    'prices': 'https://api.databursatil.com/v1/precios?token=' + API_TOKEN + '&bolsa=BMV&emisora_serie=',
    'dividend': 'https://api.databursatil.com/v1/dividendos?token=' + API_TOKEN + '&emisora_serie=',
    'credits': 'https://api.databursatil.com/v1/creditos?token=' + API_TOKEN,
}

@click.group(help='To request in the Mexican stock exchange')
def cli():
    pass