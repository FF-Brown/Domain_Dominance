# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:10:10 2020

@author: Nathan
"""

import logging
# import time

def configLogger(outFile):
    logging.basicConfig(filename=outFile, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt =  "%Y-%m-%d %H:%M")
    
if __name__ == '__main__':
    configLogger()
    logging.info("Log message") 
    # logging.warning("Date test") 
    
#