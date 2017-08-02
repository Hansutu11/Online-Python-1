# this is counting between the range of 1 and 1001 and counting by 2.
# Only printing all odd numbers.
for count in range(1,1001,2):
    print count

# this counting by 5 and printing all multiples of 5 up to 1,000,000
for count in range(5,1000005,5):
    print count

#sum list

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum

# average list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum/len(a)
