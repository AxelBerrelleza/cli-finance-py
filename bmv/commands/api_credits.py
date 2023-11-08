import requests
from rich import print as rprint
from app import cli, endpoints

@cli.command("api-credits", help='Ask for the remaining API credits')
def api_credits():
    url = endpoints['credits']
    response = requests.get(url)
    response.raise_for_status()
    
    rprint('[bold]Remaining: %s' % (response.json()['Disponibles']))