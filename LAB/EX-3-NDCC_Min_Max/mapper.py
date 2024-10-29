#!/usr/bin/env python3
import sys
for line in sys.stdin:
    fields = line.strip().split()
    
    if len(fields) >= 8:
        date = fields[1]  
        max_temp = fields[7]  
        min_temp = fields[6]  

        
        try:
            print(f"{date}\t{max_temp}\t{min_temp}")
        except ValueError:
            continue
