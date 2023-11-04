import requests
from app import cli, endpoints
from rich import print as rprint

@cli.command("api-credits")
def api_credits():
    url = endpoints['credits']
    response = requests.get(url)
    response.raise_for_status()
    
    rprint('[bold]Remaining: %s' % (response.json()['Disponibles']))