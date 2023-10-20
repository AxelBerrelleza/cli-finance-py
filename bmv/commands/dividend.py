import click
import requests
import pprint
from app import cli, endpoints

@cli.command(help='gets the most recent dividend')
@click.argument('symbol', type=click.STRING)
def dividend(symbol):
    url = endpoints['dividend'] + symbol

    response = requests.get(url)
    response.raise_for_status()
    pprint.pprint(response.json())