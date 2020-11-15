# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 22:49:05 2019

@author: Welcome
"""

import re
pattern1 = '^h...s$'
input_text = 'hello did you get pattern'
out = re.match(pattern1, input_text)
if out:
  print("Got Pattern matching string")
else:
  print("match string is not present")	
  
  
input_sentence = 'roll no 7 is doing better than rollno 12 but rollno 10 is exceedingly good'
pattern2 = '\d+'
outcome = re.findall(pattern2, input_sentence) 
print(outcome)


data = 'Twelve:12 Eighty nine:89.'
pattern3 = '\d+'
splitdata = re.split(pattern3, data) 
print(splitdata)