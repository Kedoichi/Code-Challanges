import unittest


def countPurchases(cost, budget):
    # Filter out items that are more expensive than the budget and calculate their sum
    affordable_items = [c for c in cost if c <= budget]
    if not affordable_items:
        return 0  # Return early if no items can be afforded

    total_affordable_sum = sum(affordable_items)
    min_cost = min(affordable_items) if affordable_items else float('inf')

    # Calculate how many full rounds can be made with the total sum of affordable items
    full_rounds = budget // total_affordable_sum
    purchases = full_rounds * len(affordable_items)

    # Calculate the remaining budget after full rounds
    remaining_budget = budget % total_affordable_sum

    # Use the remaining budget to buy additional items
    for item_cost in affordable_items:
        if item_cost <= remaining_budget:
            remaining_budget -= item_cost
            purchases += 1
            # Break early if the next purchase cannot be made
            if remaining_budget < min_cost:
                break

    return purchases



if __name__ == '__main__':
    unittest.main()
