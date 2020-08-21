def binarySearch(arr, l, r, x):
 
    while l <= r:
 
        mid = l + (r - l)/2;
         
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
 
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
     
    # If we reach here, then the element
    # was not present
    return mid, arr[mid]

l=[1,3,4,6,7,8,9]
a,b = binarySearch(l,0,len(l),5)
print a,b
 
	