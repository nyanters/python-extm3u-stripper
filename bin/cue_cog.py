#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = """{f}
Usage:
  {f} (-m <m3u>)
  {f} (-h | --help)

Options:
  -h --help  Show this screen.
  -m <m3u>   M3U Path (required)
""".format(f=__file__)

from docopt import docopt
import ini
import os
import platform
import subprocess
import sys


def main(m3u):
  check_os()
  play_mid(m3u)
  sys.exit()


def check_os():
  if not platform.system() == 'Darwin':
    sys.exit('This script is for only macOS!')
  return


def play_mid(m3u):
  txt = ini.init(m3u)
  os.chdir(os.path.dirname(m3u))
  for i in txt:
    apath = os.path.abspath(i)
    cmd = ['open', '-a', 'Cog', apath]
    subprocess.run(cmd)
  return


if __name__ == "__main__":
  args = docopt(__doc__)
  main(args['-m'])
