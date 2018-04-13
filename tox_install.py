#!/usr/bin/env python

if __name__ == '__main__':
    import sys
    import os
    import subprocess

    for package in sys.argv[1:]:
        cmd = "pip install " + package
        print(cmd)
        subprocess.call(cmd, shell=True)
