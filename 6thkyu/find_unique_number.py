def find_uniq(arr):
    from collections import Counter
    
    count = Counter(arr)
   
    for key,value in count.items():
        if value == 1:
            return key

# Time: O(N)
# Space: O(N)