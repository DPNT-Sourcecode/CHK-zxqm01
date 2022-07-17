"""
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+
"""

from collections import Counter
from itertools import count
from math import remainder

def multi_offer(value, quantity, original, special):

    # if the value (how many there are) isnt above the threshold, just return the original price * value
    if value < quantity:
        return original * value

    # If the value is above the threshold, times the special price * how many time its divisible
    devisible_times, remainder =  divmod(value, quantity)
    sub = devisible_times*special

    print(sub, remainder)
        
    return sub, remainder

def bogof_offer(value, original):

    # Work out how many times the value (how many there are)  can be divided by 2
    devisible_times, remainder =  divmod(value, 2)

    sub = devisible_times * original

    # Must remember to also include any extras (they could buy more than quantity specified in the deal)
    if remainder > 0:
        sub = sub + remainder * original

    print(f"{value} items @ {original} price = {sub}")


    return sub

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus_as_list = list(skus)
    counts = Counter(skus_as_list)

    total = 0 

    for each in counts:

        if each not in ["A","B","C","D", "E"]:
            return -1

        if each == "A":
            remainder = 0
            original_price = 30
            
            # If the more valuable offer is available
            if counts[each] > 5:
                special_price = 200
                special_threshold = 5
                sub, remainder = multi_offer(counts[each],special_threshold, original_price, special_price)
                total = total + sub

            # Use the other offer if the more valuable one has been used or there is still enough in the remainder to trigger this one
            if counts[each] > 3 or remainder > 3:
                # Figure out which one it is
                this = counts[each] if counts[each] > 3 else remainder
                special_price = 130
                special_threshold = 3
                sub, remainder = multi_offer(counts[each],special_threshold, original_price, special_price)
                total = total + sub
            
            if remainder > 0:
                total = total + (remainder * original_price)

        if each == "B":
            original_price = 30
            special_price = 45
            special_threshold = 2
            sub, remainder = multi_offer(counts[each], special_threshold, original_price, special_price)
            total = total + sub

            if remainder > 0:
                total = total + (remainder * original_price)


        if each == "C":
            total = total + (counts[each]*20)

        if each == "D":
            total = total + (counts[each]*15)

        if each == "E":
            total = total + bogof_offer(counts[each], 40)

    return total


if __name__ == "__main__":
    checkout("AAABCDEEE")




