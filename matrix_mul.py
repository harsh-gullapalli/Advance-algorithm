A=[]
n=int(input("Enter N for N x N matrix: "))         
print("Enter the elements of 1st matrix: ")
for i in range(n):  
   row=[]                                     
   for j in range(n): 
      row.append(int(input()))           
   A.append(row)                      
                                       
B=[]       
print("Enter the element of 2nd matrix: ")
for i in range (n): 
   row=[]                                     
   for j in range(n): 
      row.append(int(input()))           
   B.append(row)                       

print("Matrix A: ")
for i in range(n):
   for j in range(n):
      print(A[i][j], end=" ")
   print()  

print("Matrix B: ")
for i in range(n):
   for j in range(n):
      print(B[i][j], end=" ")
   print()  

resultant=[]
for i in range(n):
    row = []
    for j in range(n):
        row.append(0) 
    resultant.append(row)

for i in range(len(A)): 
   for j in range(len(B[0])): 
      for k in range(len(B)): 
         resultant[i][j] += A[i][k] * B[k][j] 

print("\nThe Resultant Matrix Is")
for r in resultant: 
   print(r) 