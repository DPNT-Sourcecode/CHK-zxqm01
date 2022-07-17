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

def multi_offer(value, quantity, original, special):

    # if the value (how many there are) isnt above the threshold, just return the original price * value
    if value < quantity:
        return original * value

    # If the value is above the threshold, times the special price * how many time its divisible
    devisible_times, remainder =  divmod(value, quantity)
    sub = devisible_times*special

    # Must remember to also include any extras (they could buy more than quantity specified in the deal)
    if remainder > 0:
        sub = sub + remainder * original
        
    return sub

def bogof_offer(value, original):
    devisible_times, remainder =  divmod(value, 2)



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
            total = total + multi_offer(counts[each], 3, 50, 130)

        if each == "B":
            total = total + multi_offer(counts[each], 2, 30, 45)

        if each == "C":
            total = total + (counts["C"]*20)

        if each == "D":
            total = total + (counts["D"]*15)

        if each == "E":
            total = total + bogof_offer()

    return total


if __name__ == "__main__":
    checkout("AAABCDEEE")