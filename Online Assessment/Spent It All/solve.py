import unittest


def countPurchases(cost, budget):
    purchases = 0 

    for c in cost: 
        if c <= budget: 
            budget -= c 
            purchases += 1

    return purchases


if __name__ == '__main__':
    unittest.main()
