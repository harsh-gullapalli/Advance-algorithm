def partition(arr,left,right):
  i=left+1
  pivot=arr[left]
  for j in range(left+1,right+1):
    if arr[j]<pivot:
      arr[i],arr[j]=arr[j],arr[i]
      i+=1
  pos=i-1
  arr[left],arr[pos]=arr[pos],arr[left]
  return pos
  
def quicksort(arr,left,right):
  if left<right:
    pivot=partition(arr,left,right)
    quicksort(arr,left,pivot-1)
    quicksort(arr,pivot+1,right)
    
arr = input('Enter the list of numbers: ').split()
arr = [int(x) for x in arr]
quicksort(arr, 0, len(arr)-1)
print('Sorted list: ', end='')
print(arr)