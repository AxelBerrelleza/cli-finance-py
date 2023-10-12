
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
    'prices': 'https://api.databursatil.com/v1/precios?token=' + API_TOKEN + '&bolsa=BMV&emisora_serie='
}

@click.group()
def cli():
    pass

@click.command(help='Request current prices of your watchlist')
def wl():
    url = endpoints["prices"] + watchlist[1]

    response = requests.get(url)
    response.raise_for_status()

    pprint.pprint(response.json())

cli.add_command(wl)

if __name__ == '__main__':
    cli()