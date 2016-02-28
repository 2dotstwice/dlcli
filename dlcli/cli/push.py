from ..cli import *
from ..api import *
import click

import logging
logger = logging.getLogger(__name__)


@cli.group('push')
@click.pass_context
def push(ctx):
    """pushes things up to dataloop"""


@click.command(short_help="Push a dashboard")
@click.argument('dashboard')
@click.pass_context
def dashboard(ctx, dashboard):
    _dashboards = Dashboards(ctx)
    print _dashboards.import_dashboard(dashboard)


@click.command(short_help="Push a plugin")
@click.argument('plugin')
@click.pass_context
def plugin(ctx, plugin):
    _plugins = Plugins(ctx)
    print _plugins.import_plugin(plugin)


push.add_command(dashboard)
push.add_command(plugin)