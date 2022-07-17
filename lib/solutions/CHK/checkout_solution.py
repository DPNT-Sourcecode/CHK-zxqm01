"""
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
"""

from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus_as_list = skus.split()
    counts = Counter(skus_as_list)
    print(counts)
    
    for each in counts:
        if each not in ["A","B","C","D"]:
            return -1

        if each == "A":
            

