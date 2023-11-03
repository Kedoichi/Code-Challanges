##Explanation and Complexity:
1. Initialization: Three variables are initialized to keep track of the number of positive, negative, and zero elements.
2. Iteration: A single forEach loop goes through each element of the array to update our counters. This is an O(n) operation, where n is the number of elements in the array.
3. Ratio Calculation: After the loop, we calculate the ratio of each type of number to the total number of elements.
4. Output: I use toFixed(6) to format the output to 6 decimal places, as specified in the problem.

#Performance

##O(n)

Cause using one loop thought the array.