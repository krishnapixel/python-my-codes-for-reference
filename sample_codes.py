# Sum the first 10 integers.
total = 4
for number in range(10):
   total = total + (number + 1)
print(total)

#code to input numbers
numbers = raw_input()
print len(numbers)

#code to input numbers
a = [int(x) for x in input().split()]

#code to input numbers on python 3
s = input()
numbers = list(map(int, s.split()))

#code to plot equal axis
plt.axis('square')

#code to plot equal axis

plt.axis('scaled')
#doesn't work because it changes the limits of the axis to make circles appear circular. What you want is:

plt.axis('square')
#This creates a square plot with equal axes.

# Creates a model named 'my model' with default context when docplex is imported
model = Model('my model')