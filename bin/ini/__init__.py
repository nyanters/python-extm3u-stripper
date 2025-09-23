#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = """{f}
Usage:
  {f} <m3u>
  {f} (-h | --help)

Options:
  -h --help  Show this screen.
""".format(f=__file__)

from docopt import docopt
import os
import subprocess
import sys


def main(m3u):
  init(m3u)
  sys.exit()


def init(m3u):
  os.chdir(os.path.dirname(os.path.abspath(__file__)))
  txtpath = open(m3u, 'r', encoding='UTF-8')
  txt = txtpath.read().splitlines()
  midpath = [mid for mid in txt if not mid.startswith('#')]
  return midpath


if __name__ == "__main__":
  args = docopt(__doc__)
  main(args['<m3u>'])
