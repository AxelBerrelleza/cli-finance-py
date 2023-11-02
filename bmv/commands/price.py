import click
import requests
from app import cli, endpoints, CliTable

@cli.command(help='Request current prices')
@click.argument('symbols', nargs=-1)
@click.pass_context
def price(context, symbols):
    if len(symbols) == 0:
        raise click.BadArgumentUsage('Please provide at least one symbol') 

    table = CliTable()
    table.headers = [
        'Precio',
        'Porcentaje',
        'Variacion ($)',
        'Fecha y Hora',
    ]
    respuestas: list = []
    for symbol in symbols:
        url = endpoints["prices"] + symbol
        response = requests.get(url)
        response.raise_for_status()
        aux = response.json()['BMV']
        respuestas.append([
            str(aux['ultimo']),
            str(aux['cambio%']),
            str(aux['cambio$']),
            str(aux['tiempo']),
        ])

    table.rows = respuestas

    context.obj.process(table)