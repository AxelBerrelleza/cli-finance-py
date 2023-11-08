import click
import requests
from app import cli, endpoints
from outputs import OutputConsoleTable

@cli.command(help='Gets info about the last dividends of a symbol')
@click.argument('symbol', type=click.STRING)
@click.pass_context
def dividend(context, symbol):
    url = endpoints['dividend'] + symbol
    response = requests.get(url)
    response.raise_for_status()

    table = OutputConsoleTable()
    table.headers = [
        'Date',
        'Amount',
        'Type',
    ]
    auxRows: list = []

    data: dict = response.json()
    for key, value in data['historico'].items():
        auxRows.append([
            key,
            str(value['pago']),
            value['tipo'],
        ])

    table.rows = auxRows
    context.obj.process(table)
