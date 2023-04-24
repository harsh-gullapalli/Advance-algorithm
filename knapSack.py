def knapSack(W, wt, val, n):
	if n == 0 or W == 0:
		return 0
	
	if (wt[n-1] > W):
		return knapSack(W, wt, val, n-1)
	else:
		return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                           knapSack(W, wt, val, n-1))


profit=[]
x=int(input("Enter no. of inputs: "))         
print("Enter profits : ")
for i in range(x):                                        
    profit.append(int(input()))           
                                                            
weight=[]       
print("Enter weights :")
for i in range (x):  
    weight.append(int(input()))           
  
W=int(input("Enter capacity of bag: "))
n = len(profit)
print ("\nMaximum Profit is :",knapSack(W, weight, profit, n))


