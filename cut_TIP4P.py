#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 1 18:03:56 2022
Cutting the TIP4P water droplet. Here I cut the droplet in the dirction of z axis.
@author: roudsari
"""

z= 50
inds = []    
LoL_new = []
Path="/Users/roudsari/Documents/TIP_droplet/"   
a_file = open(Path+"hem1.pdb", "r")      #reading the pdb file    
LoL = a_file.readlines()                 #list of pdb lines 
LoL_sliced = LoL[4:-2]                   #removing the first 4 lines and the last 2 lines of pdb file

for j in range(len(LoL_sliced)):            #going through the line in pdb file
    line=LoL_sliced[j]                       
    line= line.split()                      #split the pdb file column wise                 
    if line[2] =="OW" and float(line[7])>z: #the 3rd column is OW and 8th column is z coordinate.  
        L = LoL_sliced[j:j+4:1]             #considering the whole water molecules HW1, HW2 and MW (three rows after OW).
        LoL_new +=  L                       #appending the rows in list of new lines

LoL_new= LoL[0:3] + LoL_new + LoL[-2:]      #concatenating the fisrt 4lines and the last 2 lines with the cutting part of droplet

b_file = open(Path+"hem.pdb", "w")          #writing a new pdb file
b_file.writelines(LoL_new)
b_file.close()
