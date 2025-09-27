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
from pathlib import Path
from time import sleep
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
  tmp_m3u = str(Path.home())+'/Downloads/tmp.m3u'
  txt = ini.init(m3u)
  os.chdir(os.path.dirname(m3u))
  for i in txt:
    if '.cue' in i:
      cmd_cue = ['open', '-a', 'Cog', i]
      subprocess.run(cmd_cue)
      sleep(3)
    else:
      with open(tmp_m3u, 'a', encoding='utf-8') as f:
        print(i, file=f)
  if os.path.exists(tmp_m3u):
    subprocess.run(['open', '-a', 'Cog', tmp_m3u])
    sleep(5)
  os.remove(tmp_m3u)
  return


if __name__ == "__main__":
  args = docopt(__doc__)
  main(args['-m'])
