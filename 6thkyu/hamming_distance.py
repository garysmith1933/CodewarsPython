def hamming(a,b):
  count = 0
    
  for idx in range(len(a)):
    # compare current idx of both strings to see if they are NOT the same
    if a[idx] != b[idx]:
      # if they arent increment count
      count += 1
  
  return count

# Time: O(N) length of a or b cause they are both the same length
# Space: O(1)