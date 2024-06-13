def purify(numbers):
  new_list =[]
  for i in numbers:
    if i % 2 == 0:
      new_list.append(i)
  return new_list
  
print (purify([1,2,3,4]))
