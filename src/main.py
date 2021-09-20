# Plot multiple views

import webbrowser
from urllib import parse

import click


# Shared args
@click.group()
@click.option("--debug", "-d", is_flag=True, help="Use debug mode")
@click.option("--verbose", "-v", is_flag=True, help="Use verbose mode")
@click.pass_context
def cli(ctx, debug, verbose):
    """Pass general probram settings such as 'debug'

    Example, to call 'plot' with 'debug' use:
        'python ./src/main.py --debug plot'
    """
    ctx.ensure_object(dict)

    ctx.obj["DEBUG"] = debug
    ctx.obj["VERBOSE"] = verbose

    if verbose:
        click.echo(f"Verbose is on")
        click.echo(f"Debug is {'on' if ctx.obj['DEBUG'] else 'off'}")
    elif debug:
        click.echo(f"Debug is 'on'")
    else:
        pass


@click.option("--wolframalpha", "-w", is_flag=True, help="Wolfram Alpha browser views")
@click.option("--equation", "-e", is_flag=True, help="Equation to graph")
@cli.command()
@click.pass_context
def plot(ctx, wolframalpha, equation):
    debug = ctx.obj["DEBUG"]
    verbose = ctx.obj["VERBOSE"]

    equation = "(ln(t + 1), t/sqrt(9-t^2), 2^t)"
    if equation:
        equation = equation
    if wolframalpha:
        # open in wolframalpha with views
        # https://reference.wolfram.com/language/ref/ViewPoint.html
        base_query_url = "https://www.wolframalpha.com/input/?i=3d+parametric+plot+"
        equation = "(ln(t+1), t/sqrt(9-t^2), 2^t)"
        region = "t from -3 to 3"
        views = ["", "front", "back", "left", "right", "above", "below"]
        if debug:
            views = [""]
        for view in views:
            view_point = ""
            if view != "":
                view_point = "view from " + view
            query_parameters = parse.quote(
                ",".join([equation + "," + region + view_point])
            )
            url = base_query_url + query_parameters
            webbrowser.open_new_tab(url)


if __name__ == "__main__":
    cli(obj={})
