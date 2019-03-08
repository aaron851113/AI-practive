#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:21:13 2018

@author: aaron
"""

import requests
import os.path
from bs4 import BeautifulSoup 


thepage = requests.get('https://tw.finance.appledaily.com/realtime')
soup = BeautifulSoup(thepage.text,'html.parser')

#print(soup.prettify())



save_path = '/Users/aaron/Desktop/pytry'

name_of_file = input("input file name>>")

completeName = os.path.join(save_path, name_of_file+".txt")         

file1 = open(completeName, "w")

print (soup.title)
tofile = soup.find('title').string
file1.write(tofile+'\n')

num = soup.find_all('a')
for n in num:
        
    if n.find('time') != None :
        print(n.find('time').string)
        file1.write('[')
        file1.write(n.find('time').text)
        file1.write(']-')
        if n.find('h1') != None :
            print(n.find('h1').string)
            file1.write(n.find('h1').text+'\n')
    
    

file1.close()
