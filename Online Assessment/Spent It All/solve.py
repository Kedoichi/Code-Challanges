import unittest


def countPurchases(cost, budget):
    
    cost = [c for c in cost if c <= budget]
    purchases = 0

    # Loop until no more purchases can be made
    while cost:
        # Track if any purchase was made in this iteration to decide whether to continue
        made_purchase = False

        # Iterate over a copy of the list since we'll be modifying the original list
        for c in cost[:]:
            if c <= budget:
                budget -= c
                purchases += 1
                made_purchase = True
            else:
                # Remove items that are no longer affordable
                cost.remove(c)

        # If no purchases were made in this iteration, break out of the loop
        if not made_purchase:
            break

    return purchases



if __name__ == '__main__':
    unittest.main()
