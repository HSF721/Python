#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os

def detect_walk(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for filename in files:        
            print "file:%s\n" % filename
        for dirname in dirs:
            print "dir:%s\n" % dirname

if __name__ == "__main__":
    detect_walk(".")