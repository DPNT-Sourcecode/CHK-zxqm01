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

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus not in ["A","B","C","D"]:
        return -1

