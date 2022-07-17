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

def multi_getter(value, quantity, original, special):
    sub = 0 
    
    value, remainder =  divmod(value, quantity)
    print(value)
    print(remainder)



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
            if counts[each] >= 3:
                total = multi_getter(counts[each], 3, 50, 130)
            else:
                total = total + (counts[each] * 50)

        if each == "B":
            if counts[each] >= 2:
                total = multi_getter(counts[each], 2, 30, 45)
            else:
                total = total + (counts[each] * 30)

        if each == "C":
            total = total + (counts["C"]*20)

        if each == "D":
            total = total + (counts["D"]*15)

    print(total)
    return total


if __name__ == "__main__":
    checkout("AAABCD")

