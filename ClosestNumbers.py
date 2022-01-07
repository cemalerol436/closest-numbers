#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr = sorted(arr)
    i = 0
    total = []
    dif = 0
    mindif = None
    finding = []

    while i<n-1:

        dif = arr[i+1]-arr[i]

        if mindif is None or dif<mindif:
            finding = []
            mindif = dif
            finding.append(arr[i])
            finding.append(arr[i+1])

        elif dif==mindif:
            finding.append(arr[i])
            finding.append(arr[i+1])
        i += 1
    return finding

n = int(input("n:").strip())

arr = list(map(int, input("Array:").rstrip().split()))

result = closestNumbers(arr)

print(result)
