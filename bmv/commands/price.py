import click
import requests
from app import cli, endpoints
from outputs import OutputConsoleTable

@cli.command(help='Request current prices')
@click.argument('symbols', nargs=-1)
@click.pass_context
def price(context, symbols):
    if len(symbols) == 0:
        raise click.BadArgumentUsage('Please provide at least one symbol') 

    table = OutputConsoleTable()
    table.headers = [
        'Symbol',
        'Price',
        'Rate',
        'Change',
        'Datetime',
    ]
    respuestas: list = []
    for symbol in symbols:
        url = endpoints["prices"] + symbol
        response = requests.get(url)
        response.raise_for_status()
        
        aux = response.json()['BMV']
        color = 'green' if aux['cambio%'] >= 0 else 'red'
        percentageWithFormat = '[%s]%s' % (color, str(aux['cambio%']) + '%')
        changeWithFormat = '[%s]%s$' % (color, aux['cambio$'])
        respuestas.append([
            symbol,
            str(aux['ultimo']) + '$',
            percentageWithFormat,
            changeWithFormat,
            aux['tiempo'],
        ])

    table.rows = respuestas
    context.obj.process(table)