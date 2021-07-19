'''
Objective
Task
Given a base-10 integer, , convert it to binary (base-2). Then find and print the base-2 integer denoting the maximum number of consecutive 1's in 1's binary representation. When working with different bases, it is common to show the base as a subscript.

Example n=125

The binary representation of 125  is 1111101 . In base 10, there are 5 and 1 consecutive ones in two groups. Print the maximum, 5.

Input Format

A single integer, n .

Constraints 1<n<10^6

Output Format

Print a single base-10 integer that denotes the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2

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