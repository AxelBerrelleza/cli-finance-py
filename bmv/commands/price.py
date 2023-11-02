import click
import requests
from app import cli, endpoints, CliTable

@cli.command(help='Request current prices')
@click.argument('symbols', nargs=-1)
@click.pass_context
def price(context, symbols):
    if len(symbols) == 0:
        raise click.BadArgumentUsage('Please provide at least one symbol') 

    url = endpoints["prices"] + symbols[0]

    response = requests.get(url)
    response.raise_for_status()

    table = CliTable()
    table.headers = [
        'Precio',
        'Porcentaje',
        'Variacion ($)',
        'DT',
    ]
    aux = response.json()['BMV']
    fila: list = [[
        str(aux['ultimo']),
        str(aux['cambio%']),
        str(aux['cambio$']),
        str(aux['tiempo']),
    ]]
    
    table.rows = fila

    context.obj.process(table)