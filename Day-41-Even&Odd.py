import math
import os
import random
import re
import sys


n=int(input())
if(n%2!=0) or (n>=6 and n<=20):
    print('Weird')
else:
    print('Not Weird') 
