import click
import requests
import pprint
from app import cli, endpoints

@cli.command(help='Request current prices')
@click.argument('symbols', nargs=-1)
def price(symbols):
    
    if len(symbols) == 0:
        raise click.BadArgumentUsage('Please provide at least one symbol') 

    url = endpoints["prices"] + symbols[0]

    response = requests.get(url)
    response.raise_for_status()

    pprint.pprint(response.json())