#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import configparser
from yaml import load
import sys
import getopt
from run import run

cur_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(cur_path, 'config.yaml')
with open(config_path, 'rb') as f:
    cont = f.read()

cf = load(cont)


def main():
    user_agent = cf.get('user_agent')
    download_dir = cf.get('download_dir')
    element = cf.get('element')
    search_range = cf.get('search_range')
    run(user_agent, download_dir, element, search_range)


if __name__ == "__main__":
    main()