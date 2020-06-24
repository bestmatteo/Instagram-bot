#!/usr/bin/env python3
# coding: utf-8
from subprocess import Popen

filename = 'artrudesScript.py'
while True:
    print("Starting " + filename)
    p = Popen("python3 " + filename, shell=True)
    p.wait()