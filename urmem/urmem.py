#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import os
import argparse
try:
    import urllib.request as urlrequest
except:
    import urllib as urlrequest


logging.basicConfig(level=logging.WARNING)
BASEURL="https://raw.githubusercontent.com/{}/{}/{}/{}"


parser = argparse.ArgumentParser(description='shell profile online')
parser.add_argument('name', action="store", metavar='NAME', help='UR github username')
parser.add_argument('-r', action='store', dest='repo', help='UR repo name', default='urmem')
parser.add_argument('-b', action='store', dest='branch', help='UR branch name', default='master')
parser.add_argument('-f', action='store', dest='filename', help='UR file name', default='default')

args = parser.parse_args()

def writeToProfile(wrapContent):
    if os.getenv("SHELL").endswith("zsh"):
        proFilename = ".zshrc"
    elif os.getenv("SHELL").endswith("bash"):
        proFilename = ".bash_profile"
    else:
        logging.warning("save profile only support bash/zsh")
        sys.exit(3)

    try:
        logging.info("append to proFilename %s/%s" % (os.getenv("HOME"),
            proFilename))
        with open("%s/%s" % (os.getenv("HOME"), proFilename), "a") as f:
            f.write(wrapContent)
    except Exception as e:
        logging.warning("exception: %s" % e)


def main():
    logging.info("start raw file")
    content = ''
    url = BASEURL.format(args.name, args.repo, args.branch, args.filename)
    res = urlrequest.urlopen(url)
    if res.getcode() == 200:
        try:
            content += res.read().decode()
        except Exception as e:
            logging.warning(e)
            content += res.read()
    else:
        logging.warning('network error')
        sys.exit(2)
    wrapContent = "\n###### auto generate by urmem\n{}#####end of generate".format(content)
    writeToProfile(wrapContent) 
    logging.info("download with {} end exit".format(content))
    sys.exit(0)


if __name__ == "__main__":
    main()
