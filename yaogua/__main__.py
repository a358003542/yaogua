#!/usr/bin/env python
# -*-coding:utf-8-*-


import logging
import click
from yaogua import __version__
from .zhouyi import explain_all, zhouyi_yaogua

logger = logging.getLogger(__name__)


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('yaogua version {}'.format(__version__))
    ctx.exit()


def enable_debug(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    logging.basicConfig(level=logging.DEBUG)


@click.command()
@click.option('-v', '--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True, help='本软件版本')
@click.option('-V', '--verbose', is_flag=True, is_eager=True,
              callback=enable_debug, expose_value=False, help='打印输出冗余信息')
def main():
    string = explain_all(zhouyi_yaogua())
    click.echo(string)


if __name__ == '__main__':
    main()
