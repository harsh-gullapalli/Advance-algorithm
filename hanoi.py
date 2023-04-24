def Hanoi(n , start, end, mid):
	if n==1:
		print ("Move disk 1 from ",start,"to ",end)
		return
	Hanoi(n-1, start, mid, end)
	print ("Move disk",n,"from ",start,"to ",end)
	Hanoi(n-1, mid, end, start)

print("Starting Tower is A \nFinal Tower is C\n")

n = int(input("Enter no. of Disks : "))
Hanoi(n,'A','C','B')

