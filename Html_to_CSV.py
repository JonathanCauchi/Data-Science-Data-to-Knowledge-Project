#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:15:41 2019

@author: joncauchi
"""

from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
import csv

def main(): 
    mypath = "/home/joncauchi/Desktop/Part3/data/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyfiles.sort()
    #for loop hawnhekk
    for i in range(len(onlyfiles)):
        add_name = str(i)
        soup = BeautifulSoup(open("data/"+onlyfiles[i]), "html.parser")
        properties = soup.find_all("p",{"class":None})      
        filename = "property"+add_name+".csv"
        path_to_file = join("/home/joncauchi/Desktop/Part3/CSVfiles/", filename)
        f = open(path_to_file,"w")
        f = open("property"+add_name+".csv", "w") 
        writer = csv.writer(f)
        writer.writerow(["Date","Property Description"]) # Write column headers as the first line
        for i in range(len(properties)): 
            dates = soup.find_all("h2",{"class":"classified_date default_top_margin"})
            dates_csv = dates[0].text 
            properties = soup.find_all("p",{"class":None})
            properties_csv = properties[i].text
            
            writer.writerow([dates_csv, properties_csv])
        f.close()
        
if __name__ == '__main__':
    main()
            