import click
import requests
from bmv.app import cli, endpoints
from bmv.outputs import OutputConsoleTable

@cli.command(help='Symbols look up, exclude the serie')
@click.argument('text', type=click.STRING)
@click.option(
    '-m', '--market', 
    type=click.Choice(['local', 'global'], case_sensitive=False), 
    default='local', show_default=True
)
@click.pass_context
def search(context, text, market):
    url = endpoints['filter'] % (market, text)
    response = requests.get(url)
    response.raise_for_status()

    table = OutputConsoleTable()
    table.headers = [
        'Symbol',
        'Status',
        '',
        'Stock Exchange',
        'Type',
        'Current shares',
        'ISIN',
    ]

    data: dict = response.json()
    auxRows: list = []
    for key, coincidences in data.items():
        for symbol, values in coincidences.items():
            for key, data in values.items():
                auxRows.append([
                    symbol + data['Serie'],
                    data['Estatus'],
                    data['Razon Social'],
                    data['Bolsa'],
                    data['Tipo Valor Descripcion'],
                    str(data['Acciones en Circulacion']),
                    str(data['ISIN']),
                ])

    table.rows = auxRows
    context.obj.process(table)