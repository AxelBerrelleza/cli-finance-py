import requests
import click
from bmv.app import cli, endpoints
from bmv.outputs import OutputConsoleTable

@cli.command(help='Get currency values, updates every hour')
@click.pass_context
def currencies(context):
    url = endpoints['currencies']
    response = requests.get(url)
    response.raise_for_status()
    
    table = OutputConsoleTable()
    table.headers = [
        '',
        'Value',
        'Rate',
        'Change',
    ]
    table.rows = []

    data: dict = response.json()
    for currency, values in data.items():
        if type(values) == str:
            click.echo(values)
            continue

        color = 'green' if values['cambio$'] >= 0 else 'red'
        withFormat = '[' + color + ']%s'
        table.rows.append([
            currency,
            withFormat % (str(values['precio']) + '$'),
            withFormat % (str(values['cambio%']) + '%'),
            withFormat % (str(values['cambio$']) + '$'),
        ])

    context.obj.process(table)