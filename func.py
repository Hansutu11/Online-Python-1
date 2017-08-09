# odd/ even
list = range(0,2001)
for i in list:
    if i%2 != 0:
        print "Number is", int(i), "This is an odd number"
    elif i%2 !=1:
        print "Number is", int(i), "This is an even number"

# Multiply
def multiply(arr, num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr

a = [2,4,10,16]
b = multiply(a,5)
print b

# Hacker
def layered_multiples(arr):
  for val in arr:
      if val *= layered_multiples(arr):
          return new_array
x = layered_multiples(multiply([2,4,5],3))
print val
# output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
