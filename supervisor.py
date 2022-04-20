#!/usr/bin/env python

import argparse
import psutil
import threading
import logging
import sys


def getLogger():
    logger = logging.getLogger("test_task")
    logger.setLevel(logging.DEBUG)
 
    handler = logging.StreamHandler(sys.stdout)
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
 
    logger.addHandler(handler)
    return logger

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return proc.as_dict(attrs=['pid', 'name', 'cmdline'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--seconds', help='Seconds to wait between attempts to restart service')
    parser.add_argument('-c', '--count', help='Number of attempts before giving up')
    parser.add_argument('-n', '--name', help='Name of process to supervise')
    parser.add_argument('-i', '--interval', help='Check interval in seconds')

    args = parser.parse_args()
    #thread = threading.Thread(name='supervisor', target=checkIfProcessRunning('bash'))
    #thread.start()
