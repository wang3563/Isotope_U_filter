#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 12:42:10 2017

@author: zongyiwang
"""

import openpyxl
import os
import numpy as np

class IsoFilter:
    def __init__(self, filename, columnletter): # input filename and columnletter as strings
        self.column = str(columnletter)+'{}:'+str(columnletter)+'{}'
        self.filename = str(filename)+'.xlsm'
        self.wb = openpyxl.load_workbook(self.filename)
        self.ws = self.wb.active
    
    def mean(self):
        outlist = []
        for row in self.ws.iter_rows(self.column.format(2, self.ws.max_row - 8)):
        #I'd like the G to be able to be inputed as a function object, but can't figure it out
            for cell in row:
                if cell.value:
                    outlist.append(cell.value)
                else:
                    outlist.append(np.nan)
        outarray = np.array(outlist, dtype = np.float) 
        outmean = np.nanmean(a = outarray)
        return outmean


    def standdev(self):
        outlist = []
      # column = column_letter+'{}:'+column_letter+'{}'
        for row in self.ws.iter_rows(self.column.format(2, self.ws.max_row - 8)):
            for cell in row:
                value = cell.value
                if value:
                    outlist.append(value)
                else:
                    outlist.append(np.nan)
        outarray = np.array(outlist, dtype = np.float) 
        outstanddev = np.nanstd(a = outarray)
        return outstanddev
        #meancol = np.mean(a = outarray)
        #print meancol   
    
    def counts(self):
        total_counts = 0
        #column = column_letter+'{}:'+column_letter+'{}'
        for row in self.ws.iter_rows(self.column.format(2, self.ws.max_row -8)):
            for cell in row:
                value = cell.value
                if value:
                    total_counts += 1

        return total_counts
        