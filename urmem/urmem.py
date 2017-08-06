#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
from urllib import request


logging.basicConfig(level=logging.WARNING)
BASEURL="https://raw.githubusercontent.com/doomzhou/dotdir/master/"

def main ():
    logging.info("start raw file")
    try:
        res = request.urlopen("%s%s" % (BASEURL, sys.argv[1]))
        with res as f:
            print(f.read().decode())
    except:
        logging.warning("url open exception")

    logging.info("end exit")
    sys.exit(0)

if __name__ == "__main__":
    if  len(sys.argv) < 2:
        logging.warning("Usage: urmem identify")
    else:
        main()
