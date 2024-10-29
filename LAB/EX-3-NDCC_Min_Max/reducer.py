#!/usr/bin/env python3
import sys

current_date = None
current_max_temp = float('-inf')
current_min_temp = float('inf')

for line in sys.stdin:
    line = line.strip()
    date, max_temp, min_temp = line.split("\t")
    
    try:
        max_temp = float(max_temp)
        min_temp = float(min_temp)
    except ValueError:
        continue
    
    if current_date == date:
        current_max_temp = max(current_max_temp, max_temp)
        current_min_temp = min(current_min_temp, min_temp)
    else:
        if current_date:
            print(f"{current_date}\t{current_max_temp}\t{current_min_temp}")
        
        current_date = date
        current_max_temp = max_temp
        current_min_temp = min_temp

if current_date:
    print(f"{current_date}\t{current_max_temp}\t{current_min_temp}")
