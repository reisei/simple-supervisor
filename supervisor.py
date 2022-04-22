#!/usr/bin/env python

import argparse
import subprocess
import shlex
import time
import logging
import sys


def getLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    fmt = '%(asctime)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


def runProcess(processName):
    logger.info(f'Starting process {processName}')
    processArgs = shlex.split(processName)
    process = subprocess.run(processArgs)
    if process.returncode != 0:
        logger.error(f'Process {processName} ends abnormally')
    else:
        logger.info(f'Process {processName} ends normally')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--seconds',
                        help='Seconds to wait between attempts to restart service',
                        type=int, default=0)
    parser.add_argument('-c', '--count', help='Number of attempts before giving up', type=int, default=0)
    parser.add_argument('-p', '--process', help='Process to supervise')

    args = parser.parse_args()
    logger = getLogger()

    runProcess(args.process)

    if args.count == 0:
        exit(0)

    for i in range(1, args.count + 1):
        logger.info(f'Restarting in {args.seconds} seconds...')
        time.sleep(args.seconds)
        runProcess(args.process)
