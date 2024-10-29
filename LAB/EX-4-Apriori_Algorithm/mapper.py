import sys
from itertools import combinations

def generate_combinations(items, k):
    return combinations(sorted(set(items)), k)

k = 3
for line in sys.stdin:
    items = line.strip().split()[1:]
    item_combinations = generate_combinations(items, k)
    for itemset in item_combinations:
        print(f"{','.join(itemset)}\t1")

