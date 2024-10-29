import sys

current_itemset = None
current_count = 0
min_support = 2

for line in sys.stdin:
    itemset, count = line.strip().split("\t")
    count = int(count)

    if current_itemset == itemset:
        current_count += count
    else:
        if current_itemset and current_count >= min_support:
            print(f"{current_itemset}\t{current_count}")
        current_itemset = itemset
        current_count = count

if current_itemset and current_count >= min_support:
    print(f"{current_itemset}\t{current_count}")
