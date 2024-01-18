import click
import requests
from bmv.app import cli, endpoints
from bmv.outputs import OutputConsoleTable

@cli.command(help='Request current prices')
@click.argument('symbols', nargs=-1)
@click.option('--watchlist', type=click.Path(exists=True), help='json array of symbols')
@click.pass_context
def price(context, watchlist, symbols):
    if len(symbols) == 0 and watchlist is None:
        raise click.BadArgumentUsage('Please provide at least one symbol') 

    if watchlist is not None:
        auxFile = click.open_file(watchlist, 'r')
        symbols = auxFile.readlines()

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
        if symbol is None or symbol.strip() == '':
            continue
        
        url = endpoints["prices"] + symbol.strip()
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