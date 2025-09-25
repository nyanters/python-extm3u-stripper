#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = """{f}
Usage:
  {f} (-m <m3u>) [-s <sf2>]
  {f} (-h | --help)

Options:
  -h --help   Show this screen.
  -m <m3u>    M3U Path (required)
  -s <sf2>    SF2 Path (optional) [default: ]
""".format(f=__file__)

from docopt import docopt
import ini
import os
import subprocess
import sys


def main(m3u, sf2):
  play_mid(m3u, sf2)
  sys.exit()


def play_mid(m3u, sf2):
  txt = ini.init(m3u)
  os.chdir(os.path.dirname(m3u))
  for i in txt:
    subprocess.run(['fluidsynth', '-i', sf2, i])
  return


if __name__ == "__main__":
  args = docopt(__doc__)
  main(args['-m'], args['-s'])
