#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:55:13 2017

@author: zongyiwang
"""
import openpyxl
import os
import numpy as np
def main():
    print("Standard U_filter")
    filename = raw_input("Enter the source file name: ")
    columnletter = raw_input("What column are we looking at? ")
    #columnletter = column+'{}:'+column+'{}' ALREADY exists in class
    
    i = 1
    validEntry = False
    while i<3:
        while not validEntry:
            try:
                wb = IsoFilter(str(filename),str(columnletter))
                validEntry = True
                
            except IOError:
                filename = raw_input("No such file exits ! Enter the correct source file name: ")
        i += 1
    wb.getMean()
    wb.getStanddev()
    wb.getCounts()
    wb.theFilter()
    print(wb)
    
    
            

       