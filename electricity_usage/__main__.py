#!usr/bin/env python3
# Module containing the data transformation
from datetime import date, datetime
import json
import click
from commands import areas, queue, run, start, stop

@click.group(help='AAAAAAAAAAAAAAAAA')
def cli():
   pass
cli.add_command(areas.areas)
cli.add_command(queue.queue)
cli.add_command(run.run)
cli.add_command(start.start)
cli.add_command(stop.stop)

   
if __name__ == '__main__':
    cli()


