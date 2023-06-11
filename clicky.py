import click

@click.command()
@click.option('--name', prompt='Enter your name', help='The name to greet.')
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--caps', default=0, help='Capitalises result')
def greet(name, count, caps):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        if not caps:
            name_caps = "Hello " + name
            name_caps.upper()
            print(name_caps)
            click.echo(name_caps)
            
            # click.echo('Hello, %s!' % name)
        else:
            name_caps = "Hello caps " + name
            res = name_caps.upper()
            click.echo(res)

if __name__ == '__main__':
    greet()
