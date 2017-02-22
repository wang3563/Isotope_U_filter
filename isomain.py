#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 08:32:03 2017

@author: zongyiwang
"""
# Whatelse might I need to import?

import errno
from openpyxl import Workbook
import os
from os import path

def main():
    print("Standard U_filter")
    inputFile = raw_input("Enter the source file name: ")

    validEntry = False 
    #check and see if such a file exists in the directory
    while not validEntry:
        try:
            inputFile = open(inputFile, 'r')
            validEntry = True
        except IOError as e:
            print(os.strerror(e.errno)) 
            input('Enter the correct file name: ')
        
    outputFile = raw_input("Enter output File name : ")
    #First check and see to avoid overwritting existing files
    if path.isfile(outputFile):
        reponse =raw_input("File exists... overwrite? (y/n): ")
        if reponse.lower() == "y":
            outputFile = open(outputFile, 'w')
            for eachLine in inputFile:
                eachLine = eachLine.split('\t ')
                for eachNumber in eachLine:



                    
                    outputFile.write(' '.join(eachLine))
                    #do something
                    # if criteria...
                    # Some calculations
                    # maybe make a isotope ratio class?
                    #so that if the eachword 
        else:
            print("okay! Bye!")
            
               
    else:
        outputFile = open(outputFile, 'w')
        for eachLine in inputFile:
            eachLine = eachLine.split('\t ')
            for eachNumber in eachLine:
                #do something
                # if criteria...
                # Some calculations
                outputFile.write(' '.join(eachLine))
                    
    inputFile.close()
    outputFile.close()
    print('Done')
                
                
                
                
            
                
