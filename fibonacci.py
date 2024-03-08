# This is my take on the fibonacci sequence

# First, we initialize three variables
x = 0
y = 1
z = 0

# We print the first couple of numbers which are 0 and 1
print(x)
print(y)

# Now we loop! 'z' is going to equal the sum of 'x + y'
for i in range(1,31):
  z = x + y
  print(z)
  x = y
  y = z

# Its done!
