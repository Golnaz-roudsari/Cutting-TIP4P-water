#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 10:04:56 2022

@author: roudsari
modifying pdb file. z axis is multiplied with -1 inorder to give a mirror image of AgI slab.
"""

inds = []    
LoL_new = []
Path="/Users/roudsari/Documents/agi_mirror_drop/"   
a_file = open(Path+"agi.pdb", "r")       #reading the pdb file    
LoL = a_file.readlines()                 #list of pdb lines 
LoL_sliced = LoL[4:-2]                   #removing the first 4 lines and the last 2 lines of pdb file

for j in range(len(LoL_sliced)):            #going through the line in pdb file
    line=LoL_sliced[j]                       
    line_ls= line.split()                   #splitting lines columnwise 
    z = line_ls[7]                          #reading z column
    index = line.find(z)                    #specifing the index of column z
    line_new = line[:index-1] + "-"+z + line[index-1+len(z)+1:] #adding the indexes before and after column z and adding negative sign to the z column 
    LoL_new.append(line_new)                #appending the rows in list of new lines

LoL_new= LoL[0:4] + LoL_new + LoL[-2:]      #concatenating the fisrt 4lines and the last 2 lines with the cutting part of droplet

b_file = open(Path+"agi_mir.pdb", "w")          #writing a new pdb file
b_file.writelines(LoL_new)
b_file.close()
