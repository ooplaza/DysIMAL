def BinarySearch(data, si, ei, target):
    if si > ei:
        return -1
    
    
    else:
        mid = (si + ei) // 2
        if data[mid] == target:
            return mid
        
        elif data[mid] > target:
            return BinarySearch(data, si, mid-1, target)
        
        else:
            return BinarySearch(data, mid+1, ei, target)
               
search = BinarySearch([1,2,4,5], 0, 4, 5)
print(search)