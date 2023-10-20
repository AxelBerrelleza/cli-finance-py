import click
import requests
import pprint
from app import cli, endpoints

@cli.command("api-credits")
def api_credits():
    url = endpoints['credits']
    response = requests.get(url)
    response.raise_for_status()
    pprint.pprint(response.json())