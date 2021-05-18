#!/usr/bin/env python

import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-s', '--stop',help="Stop VM")
parse.add_argument('-ss', '--start',help="Start VM")
args=parse.parse_args()

if args.s:
    print("Hola")