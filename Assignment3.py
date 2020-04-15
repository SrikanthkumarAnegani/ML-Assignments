1.1 Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()
# Reduce 
def myreduce(anyfunc, sequence):


  result = sequence[0]

  for item in sequence[1:]:
   result = anyfunc(result, item)

  return result

1.2 Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()

#  filter function 
def myfilter(anyfunc, sequence):


 result = []

 for item in sequence:
  if anyfunc(item):
   result.append(item)

 # return funal output
 return result




2. Write List comprehensions to produce the following Lists
#########
word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print ("ACADGILD => " + str(alphabet_list))

#########
# Compress above for loop into a single list 
input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))

#########
# Compress above for loop into a single list
input_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_list  ]
print("['x','y','z'] => " +   str(result))

#########
input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))

#########
input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))

#########
input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))

#########