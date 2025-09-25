#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = """{f}
Usage:
  {f} (-m <m3u>)
  {f} (-h | --help)

Options:
  -h --help  Show this screen.
  -l <loop>   Loop count (optional) [default: 1]
  -m <m3u>   M3U Path (required)
""".format(f=__file__)

from docopt import docopt
import ini
import os
import subprocess
import sys


def main(m3u):
  play_mid(m3u)
  sys.exit()


def play_mid(m3u):
  mod = 3
  txt = ini.init(m3u)
  os.chdir(os.path.dirname(m3u))
  for i in txt:
    subprocess.run(['timidity', '--module='+str(mod), '-Od', i])
  return


if __name__ == "__main__":
  args = docopt(__doc__)
  main(int(args['-l']), args['-m'])
