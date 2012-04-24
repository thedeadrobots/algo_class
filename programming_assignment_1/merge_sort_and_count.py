import sys

inversions = 0 

def mergesort(list):
    if len(list) == 1:
        return list
    
    m = len(list) / 2
    l = mergesort(list[:m])
    r = mergesort(list[m:])

    if not len(l) or not len(r):
        return l or r
        
    result = []
    i = 0
    j = 0
    global inversions
    
    while (len(result) < len(r)+len(l)):        
      if l[i] < r[j]:
	result.append(l[i])
	i += 1
      else:
	result.append(r[j])
	j += 1
	inversions += (len(l) - i)   #total left list minus pointer curr_loc        
      if i == len(l) or j == len(r):            
        result.extend(l[i:] or r[j:])
        break
    return result 
    
f = open('IntegerArray.txt')
r = open('results.txt', 'w')
numbers = []
while True:
  line = f.readline()
  if line == '':
    break
  else:
    numbers.append(int(line.strip()))

print "Initial List Size: ", len(numbers)
result = mergesort(numbers)
print "Total Inversions: ", inversions

#write sorted output to a file for fun
for value in result:
  print >> r, value
