
import os
import click
from dotenv import load_dotenv
from rich import print as rprint
from rich.table import Table, Column

load_dotenv()

API_TOKEN = os.getenv('BMV_API_TOKEN')
watchlist: list = [
    'FIBRAMQ12',
    'DANHOS13',
    'FMTY14',
    # 'FUNO11',
    # 'MAYAB',
    # 'ACTIGOBB',
]

endpoints: dict = {
    'prices': 'https://api.databursatil.com/v1/precios?token=' + API_TOKEN + '&bolsa=BMV&emisora_serie=',
    'dividend': 'https://api.databursatil.com/v1/dividendos?token=' + API_TOKEN + '&emisora_serie=',
    'credits': 'https://api.databursatil.com/v1/creditos?token=' + API_TOKEN,
}

@click.group(help='To request in the Mexican stock exchange')
@click.pass_context
def cli(context):
    context.obj = AppContext()

class CliTable:
    headers: list
    rows: list

class AppContext:
    def process(self, operation: CliTable | None = None):
        if operation is None:
            pass
        else:
            # rows: list = [
            #     {'cambio$': "0.02",
            #     'cambio%': "0.08",
            #     'ppp': "0.0",
            #     'tiempo': '2023-10-31 11:58:00',
            #     'ultimo': "26.6"},
            #     {'cambio$': "0.02",
            #     'cambio%': "0.08",
            #     'ppp': "0.0",
            #     'tiempo': '2023-10-31 11:58:00',
            #     'ultimo': "26.6"}
            # ]

            rows = operation.rows

            table = Table(*operation.headers)
            table.grid()
            for row in rows:
                # table.add_row(*list(row.values()))
                table.add_row(*row)
            
            rprint(table)
