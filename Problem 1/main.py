def knapSack(maxWieght, weight, value, n):
    dp = [0 for i in range(maxWieght+1)]  # Over here I'm making the dynamic array.
 
    for i in range(1, n+1):  # Here I'm traversing from 1 to n using for-in loop.

        for w in range(maxWieght, 0, -1):  # To start from back we are keeping record of previous items.
                                
            if weight[i-1] <= w:

                dp[w] = max(dp[w], dp[w-weight[i-1]]+value[i-1]) # Here we are looking for max values and storing in dynamic array.

    return dp[maxWieght]



if __name__ == "__main__":

    # test case: 1
	value = [150, 35, 200, 160, 60, 45, 60, 40]
	weight = [9, 13, 153, 50, 15, 68, 27, 39]
	maxWieght = 100
	n = len(value)
	print(knapSack(maxWieght, weight, value, n))
    
    # test case: 2
	maxWieght = 200
	n = len(value)
	print(knapSack(maxWieght, weight, value, n))



