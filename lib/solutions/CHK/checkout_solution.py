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
    skus_as_list = list(skus)
    counts = Counter(skus_as_list)
    print(counts)

    total = 0 

    for each in counts:
        if each not in ["A","B","C","D"]:
            return -1

        if each == "A":
            total = counts["A"]*50

        if each == "B":
            total = counts["B"]*50

        if each == "C":
            total = counts["C"]*50

        if each == "D":
            total = counts["D"]*50

    return total


if __name__ == "__main__":
    checkout("AAABC")

