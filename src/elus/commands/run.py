import click 

area_list=['DE','BE']

@click.command()
@click.option('--estimate', type=float, help='estimated runtime of the program in hours') #timedelta
@click.option('--deadline', type=click.DateTime(formats=['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S']), help='latest date when the program should be finished')
@click.option('--area',type=click.Choice(area_list), default='DE', help="area code according to wherever we're putting the list")
@click.option('--commandline', type=str, help='the command line to be executed')

def run(estimate,deadline,area,commandline):
    '''adds a process to the queue'''
    print(f"Input: estimate {estimate}, deadline {deadline}, area {area}, commandline {commandline}")
    print("Joke's on you this doesn't do anything.")
