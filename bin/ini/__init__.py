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
from pathlib import Path
import os
import re
import subprocess
import sys


def main(m3u):
  init(m3u)
  sys.exit()


def init(m3u):
  midpath = []
  os.chdir(os.path.dirname(os.path.abspath(m3u)))
  txtpath = open(m3u, 'r', encoding='UTF-8')
  txt = txtpath.read().splitlines()
  midpath_raw = [mid for mid in txt if not mid.startswith('#')]
  for i in midpath_raw:
    i_home = re.sub(r'^~', str(Path.home()), i)
    i_abs = os.path.abspath(i_home)
    midpath.append(i_abs)
  return midpath


if __name__ == "__main__":
  args = docopt(__doc__)
  main(args['<m3u>'])
