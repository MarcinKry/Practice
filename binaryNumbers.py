'''
Objective
Task
Given a base-10 integer, , convert it to binary (base-2). Then find and print the base-2 integer denoting the maximum number of consecutive 1's in 1's binary representation. 

'''

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

def dec_to_bin(n):
    return int(bin(n)[2:])
    
binary = dec_to_bin(n)
string=str(binary)
score=[]
length=0
count = 0
for i in range(len(string)):
    if string[i]=='1':
        count+=1
        if count>length:
            length=count
    else:
        count=0

print(length)
