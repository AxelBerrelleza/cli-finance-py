
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

@cli.command(help='Request current prices of your watchlist')
def wl():
    url = endpoints["prices"] + watchlist[1]

    response = requests.get(url)
    response.raise_for_status()

    pprint.pprint(response.json())

@cli.command(help='gets the most recent dividend')
@click.argument('symbol', type=click.STRING)
def div(symbol):
    url = endpoints['dividend'] + symbol

    response = requests.get(url)
    response.raise_for_status()
    pprint.pprint(response.json())

@cli.command("api-credits")
def api_credits():
    url = endpoints['credits']
    response = requests.get(url)
    response.raise_for_status()
    pprint.pprint(response.json())

if __name__ == '__main__':
    cli()