Markdown
# Spend it All

There is a budget and an array of n costs. Repeat the following process until budget is less than
the minimum element in cost.

## Process

Start at element and work tan-1.

At each element cost[i]:

                If cost[i]<= budget, reduce budget by cost(i) and move to the next index. This is a purchase.

                If cost[i]> budget, move to the next index.

The array is circular, so the next index after n-1 is index 0.
Continue until there is not enough budget to make a purchase.

Determine how many purchases are made.

## Example

cost = [5, 8, 3]

budget = 12

Process:

                Buy item 0 for 5 budget 12-5-7

                Item 1 is too expensive, budget = 7.

• Buy item 2 for 3, budget 7-3-4

                Items 0 and 1 are too expensive, budget = 4.

• Buy item 2 for 3, budget-4-3-1

                Now budget = 1, and there are no more items that can be purchased.

                Return 3, the number of items purchased,

## Function Description

Complete the function countPurchases in the editor below.

count Purchases has the following parameters:

                int cost[n]: the costs of all the items
                long budget: the starting amount of the budget to be spent

Returns

                long: the number of purchases

Constraints

                1<n<2*105

                1≤ cost[i] < 109

                1≤ budget ≤1015