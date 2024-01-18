
import os
import click
from dotenv import load_dotenv
from rich import print as rprint
from rich.table import Table, Column
from bmv.outputs import OutputConsoleTable

load_dotenv()
API_TOKEN = os.getenv('BMV_API_TOKEN')

endpoints: dict = {
    'prices': 'https://api.databursatil.com/v1/precios?token=' + API_TOKEN + '&bolsa=BMV&emisora_serie=',
    'dividend': 'https://api.databursatil.com/v1/dividendos?token=' + API_TOKEN + '&emisora_serie=',
    'credits': 'https://api.databursatil.com/v1/creditos?token=' + API_TOKEN,
    'filter': 'https://api.databursatil.com/v1/emisoras?token=' + API_TOKEN + '&mercado=%s&letra=%s',
    'currencies': 'https://api.databursatil.com/v1/divisas?token=' + API_TOKEN,
}

@click.group(help='To request in the Mexican stock exchange')
@click.pass_context
def cli(context):
    context.obj = AppContext()

class AppContext:
    def process(self, operation: OutputConsoleTable | None = None):
        if operation is None:
            pass
        else:
            table = Table(*operation.headers)
            table.grid()
            for row in operation.rows:
                table.add_row(*row)
            
            rprint(table)
