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
        return original * value, 0

    # If the value is above the threshold, times the special price * how many time its divisible
    devisible_times, remainder =  divmod(value, quantity)
    sub = devisible_times*special
        
    return sub, remainder

def buy_2E_get_B_free(value, original):

    # Work out how many times the value (how many there are)  can be divided by 2
    devisible_times, remainder =  divmod(value, 2)
    return devisible_times

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus_as_list = list(skus)
    counts = Counter(skus_as_list)
    print(counts)
    b_deductions = 0

    total = 0 

    for each in reversed(counts):

        units_specified = counts[each]


        if each not in ["A","B","C","D","E"]:
            return -1

        if each == "A":
            
            remainder = 0
            original_price = 50

            # If no offers have been met
            if units_specified < 3:
                total = total + (units_specified * original_price)
            
            # If the more valuable offer is available
            elif units_specified >= 5:
                special_price = 200
                special_threshold = 5
                sub, remainder = multi_offer(units_specified,special_threshold, original_price, special_price)
                total = total + sub

            # if use the other offer is available
            elif units_specified >=3 and units_specified < 5:
                special_price = 130
                special_threshold = 3
                sub, remainder = multi_offer(units_specified,special_threshold, original_price, special_price)
                total = total + sub


            # Check if the offer is availabe on the remainder    
            if remainder >= 3:
                special_price = 130
                special_threshold = 3
                sub, remainder = multi_offer(remainder,special_threshold, original_price, special_price)
                total = total + sub

            # Finally add any out of offer items            
            if remainder:
                total = total + (remainder * original_price)

        if each == "B":
            print(f"Calculating Bs")
            original_price = 30
            special_price = 45
            special_threshold = 2
            sub, remainder = multi_offer(units_specified-b_deductions, special_threshold, original_price, special_price)
            total = total + sub

            if remainder > 0:
                total = total + (remainder * original_price)

        if each == "C":
            original_price = 20
            total = total + (units_specified*20)

        if each == "D":
            original_price = 15

            total = total + (units_specified*15)

        if each == "E":
            print(f"Calculating Es")
            original_price = 40
            total = total + (units_specified*original_price)
            free_B = buy_2E_get_B_free(units_specified, original_price)
            print(f"{free_B} free Bs available")

            if "B" in counts.keys() and counts["B"] >= free_B:
                print(f"total B in basket = {counts['B']}")
                b_deductions = counts["B"] - free_B

        print(f"cost so far: {total}")


    print(total)

    return total


if __name__ == "__main__":
    checkout("BEBEEE")
