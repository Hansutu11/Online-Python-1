# find and replace
#print my string then find the word "day" and then replace it with "month"
# then print my new string with "month" replacing "day"
string = "It's Thanksgiving day. It's my birthday too!"
print string
print string.find("day")
string = string.replace("day", "month")
print string

#min/max

x = [2,54,-2,7,12,98]
print x
print min(x)
print max(x)

# first and last
# What I'm doing here is  looking at my value of x as an array type then I print x, then
# print (0) == "hello" then print (7)== "world"
x = ["hello", 2,54,-2,7,12,98,"world"]
print x
print x[0]
print x[7]

#new list
# On this I printed x[], then I sorted the x[] form lowest to highest. Then printed the sorted x
# Then I created 2 list "first_list" & "second_list" then I added x(0) and then the first_list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort ()
print x
first_list = x[:len(x)/2]
second_list = x[len(x)/2:]
print "fist list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list
