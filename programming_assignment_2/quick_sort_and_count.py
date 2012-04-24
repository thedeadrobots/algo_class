import sys

def quicksort_first_pivot(numbers, left, right):
    if right - left <= 1:
      return 0 
    else:
      pivotIndex = partition(numbers, left, right)
      comparisons = (right - left) - 1
      left_cnt = quicksort_first_pivot(numbers, left, pivotIndex)
      right_cnt = quicksort_first_pivot(numbers, pivotIndex + 1, right)
      comparisons += left_cnt + right_cnt 
      return comparisons

def quicksort_last_pivot(numbers, left, right):
    if right - left <= 1:
      return 0 
    else:
      numbers[left], numbers[right - 1] = numbers[right - 1], numbers[left]
      pivotIndex = partition(numbers, left, right)
      comparisons = (right - left) - 1
      left_cnt = quicksort_last_pivot(numbers, left, pivotIndex)
      right_cnt = quicksort_last_pivot(numbers, pivotIndex + 1, right)
      comparisons += left_cnt + right_cnt 
      return comparisons 

def quicksort_median_pivot(numbers, left, right):
  if right - left <= 1:
    return 0
  else:
    find_middle = (right - left + 1) / 2 - 1
    median_index = left + find_middle
    first = numbers[left]
    last = numbers[right - 1]
    middle = numbers[median_index]
    three_pivots = [first, last, middle]
    is_middle = []
    is_middle.append(min(three_pivots))
    is_middle.append(max(three_pivots))
    median = set(three_pivots) - set(is_middle)
    
    if last in median:  #swap first and last
      numbers[left], numbers[right - 1] = numbers[right - 1], numbers[left]
    elif middle in median: #swap middle and last
      numbers[left], numbers[median_index] = numbers[median_index], numbers[left]
    
    pivotIndex = partition(numbers, left, right)
    comparisons = (right - left) - 1
    left_cnt = quicksort_median_pivot(numbers, left, pivotIndex)
    right_cnt = quicksort_median_pivot(numbers, pivotIndex + 1, right)
    comparisons += left_cnt + right_cnt
    return comparisons

def partition(numbers, left, right):
  pivot = numbers[left]
  i = left + 1
  for j in range (left + 1,  right):
    if numbers[j] < pivot:
      numbers[i], numbers[j] =  numbers[j], numbers[i]
      i += 1
  #swap
  numbers[left], numbers[i - 1] = numbers[i - 1],  numbers[left]
  return i - 1

def main():
  f = open('Quicksort.txt')
  numbers = []
  numbers_last = []
  numbers_median = []
  while True:
    line = f.readline()
    if line == '':
      break
    else:
      numbers.append(int(line.strip()))
      numbers_last.append(int(line.strip()))
      numbers_median.append(int(line.strip()))

  print "Initial List Size: ", len(numbers)
  result = quicksort_first_pivot(numbers, 0, len(numbers)) 
  print "First Element Pivot: ", result 
  last_element = quicksort_last_pivot(numbers_last, 0, len(numbers_last))
  print "Last Element Pivot: ", last_element
  median_element = quicksort_median_pivot(numbers_median, 0, len(numbers_median))
  print "Median Element Pivot: ", median_element

if __name__ == '__main__':
    main()

