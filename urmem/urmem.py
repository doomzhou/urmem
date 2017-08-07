#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import os
try:
    import urllib.request as urlrequest
except:
    import urllib as urlrequest


logging.basicConfig(level=logging.WARNING)
BASEURL="https://raw.githubusercontent.com/doomzhou/dotdir/master/"

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

def main ():
    logging.info("start raw file")
    content = ''
    try:
        res = urlrequest.urlopen("%s%s" % (BASEURL, sys.argv[1]))
        content += res.read().decode()

    except AttributeError:
        content = res.read()

    wrapContent = "\n###### auto generate by urmem\n%s#####end of generate" % content
    writeToProfile(wrapContent) 
    print(wrapContent)
    logging.info("end exit")
    sys.exit(0)

if __name__ == "__main__":
    if  len(sys.argv) < 2:
        logging.warning("Usage: urmem identify")
    else:
        main()
