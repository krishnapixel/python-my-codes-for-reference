s = 'hello'
print (s)

s = 15
print (s)

s= 'invest'
s[0]
print (s[0])                                           #the command prints zeroeth index

s[:3]
print(s[:3])                                             # colon indicates to print everything before 3rd index

s[0:]
print(s[0:])                                          #colon indicates to print everything from zeroeth index

s[0:4]
print(s[0:4])

print(s[2:5])

a = 'welcome wednesday'
print (a)

b = '''Don't come'''                                 #when you put this in single quotes, it would not work
print(b)

c = "Don't come"
print (c)

num = 12
name = 'Sam'

print('My name is {} and my number is {}.'.format(name, num))

my_list = ['s', 'q', 'u', 'a', 'r', 'e']
print(my_list)
my_list.append('brackets')                                      #the append command takes only one argument

print(my_list)

print(my_list[0])
print(my_list[0:2])
print(my_list[6])

my_list[0] = 'new item'           #replaces the indicated index with the variable            
print(my_list)

nest_with_quotes = ['1', '2',['3','4']]
print(nest_with_quotes)

nest = [1, 2,[3,4]]                     #nest within a list, the inner list is denoted by 2
print(nest)

print(nest[2])
print(nest[2][0])


print(nest[2][1])                 #this command prints 4, the 1st index in 


nest = [1, 2, 3, [4, 5, ['target']]]
print (nest[3][2][0])

#crash course 2
d = {'key1' : 'value1', 'key2' : 123 }
print (d['key1'])

print(d['key2'])

d = {'key1' :{'innerkey':[1, 2, 3]}}
print(d['key1']['innerkey'][1])
if 1 == 2:
    print("if for first condition")
elif 1 == 1:
    print("elif for middle conditions")   
else:
    print("else for last condition") 

#for loop to perform a block of code section 3
seq = [1, 2, 3, 4, 5]
for item in seq:
    print (item)

seq = [1, 2, 3, 4, 5]
for cat in seq:
    print (cat)    

seq = [1, 2, 3, 4, 5]
for jelly in seq:
    print ('jelly')   

i = 1

while i < 5:
    print( 'i is: {}' .format(i))
    i = i + 1

for x in seq:
    print (x)

for x in range (0, 5):
    print(x)

print (list (range(10)))

x = [1, 2 ,3, 4]
out = []
for num in x:
    out.append(num**2)
print (out)

print([num**2 for num in x])

out = [num**2 for num in x]     #list comprehension
print(out)

#writing a function
def square(num):
    return (num **2)
output = square(2)
print(output)


def times2(var):
    return (var**2)
output = times2(5**2)
print(output) 

def times2(var): return var*2

#map
seq = [1, 2, 3, 4, 5]
new_seq = list(map(lambda num: num*3, seq))
print(new_seq)

output = list(filter(lambda num: num%2 == 0, seq))   
print(output)

s = 'HELLO, my name is SAM'
lower_case = s.lower()
print(lower_case)

s = 'HELLO, my name is SAM'
upper_case = s.upper()
print(upper_case)

s = 'HELLO, MY NAME IS SAM'
splitted = s.split()
print(splitted)

tweet = 'Go Sports! #sports'
s = tweet.split()
print(s)

tweet = 'Go Sports! #sports'
s = tweet.split('#')
print(s)

tweet = 'Go Sports! #sports'
s = tweet.split('#')[1]
print(s)

d = {'k1' : 1, 'k2' : 2, }
s = d.keys()
print(s)

d = {'k1' : 1, 'k2' : 2, }
s = d.values()
print(s)

lst = [1, 2, 3]
s = lst.pop()
print (s)
print(lst)


lst = [1, 2, 3, 4, 5]
s = lst.pop()
print (lst)
print(s)
lst.pop(0)
print(lst)
lst.append('new')
print(lst)
x in [1, 2, 3]

x in ['x', 'y', 'z']
print(x)
x = [(1, 2), (3, 4), (5, 6)]
for (a, b) in x:
    print(a)
    print(b)
    print('ab')


print(10 > 9)
print(12 == 4)
print(bool("Hello"))
print(bool(10 > 9))
print(bool(10 > 19))

#Exercises
#What is 7 to the power of 4?
print(7**4)
a = 7**4
print(a)

#split the string " Hi there, Sam!"
a = 'Hi there, Sam!'
a.split()
print(a.split())

#Given variables
planet = 'earth'
diameter = 12742

print('The diameter of the {} is {} kilometers'.format(planet, diameter))

#given the nested list, use indexingto grab the word "hello"
lst = [1, 2, [3, 4],[5,[100, 200, ['hello']], 23, 11], 1, 7]
print(lst[3][1][2])

#given the nest dictionary grab 'hello'. This is annoyingly tricky

d = {'k1':[1, 2, 3,{'tricky':['oh', 'man', 'inception',{'target':[1, 2, 3, 'hello']}]}]}
print(d['k1'][2])
print(d['k1'][3])
print(d['k1'][3]['tricky'][2])
print(d['k1'][3]['tricky'][3]['target'][3])      #you should always write the key in the command line

#What's the main difference between tuple and a list?

#create a function that grabs the email website domain from a string in the form user@domain.com
def domainGet(email):
    return (email.split('@'))
print(domainGet('user@domain.com'))    #this is where you call the function using an argument or example input

#create a basic function taht returns True if the input string has 'dog', also try accounting for capitalization

def findDog(s):
    return('dog' in s.lower().split())
print(findDog('is there a Dog here?'))

def findDog(s):
    return('dog' in s.split())
print(findDog('is there a Dog here?'))

def countDog(s):
    count = 0
    for word in s.lower().split():
        if word == 'dog':
            count == count+1
print(countDog('is there a Dog here?'))

def countDog(s):
    count = 0
    for word in s.lower().split():
        if word == 'dog':
            count += 1
    return count          
print(countDog('is there a dog dog here?'))

#use lambda expressions and the filter() function to filter out words FROM A LIst thta does not start with letter s.
s = ['soup', 'dog', 'salad', 'cat', 'great']
list(filter (lambda word: word[0] =='s', s))
print(list(filter (lambda word: word[0] =='s', s)))

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed

    if speeding > 80:
        return 'big ticket or fine'
    elif speeding > 60:
        return 'small ticket or fine'  
print(caught_speeding(40, True))          
        
'''caught_speeding(96, True)
return 'small ticket'''

#python for data analytics with numPy
#numPy arrays
#create an object my_list

my_list = [1, 2, 3]
print(my_list)
import numpy as np
arr = np.array(my_list)
print(arr)

my_mat =[[1, 2, 3], [4, 5, 6],[7, 8, 9]]
arr = np.array(my_mat)
print (arr)

a = np.arange(0, 10)
print (a)

a = np.arange(0, 13, 2)
print (a)

a = np.zeros((2,3))
print(a)

a = np.ones((3))
print(a)

a = np.ones((3,4))
print(a)

a = np.linspace(3,44,10)
print(a)

a = np.linspace(3,44,20)  #this is a one dimensional array
print(a)

a = np.eye(4)             #identity matrix two dimensional
print(a)

a = np.random.rand(5)
print (a)

a = np.random.randn(5)     #single dimension when one number in brackets is specified
print (a)

a = np.random.randn(5)
print (a)

a = np.random.randint(5, 29, 6)        #type (low, high, size)
print (a)

arr = np.arange(25)
print(arr)

ranarr = np.random.randint(0, 50, 10)
print(ranarr)
print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax())
print(ranarr.argmin())
print(arr.shape)

arr = arr.reshape(5, 5)
print (arr.shape)
print(arr.dtype)

from numpy.random import randint
print(randint(5,40))


a = arr.reshape(5,5)
print(a)

#Numpy indexing and selection

import numpy as np
arr = np.arange(0,11)
print (arr)
arr[8]
print (arr[8])
print(arr[0:5])
print(arr[1:5])
print(arr[:5])
print(arr[1:])
print(arr[5:])
arr[0:5] = 100
print (arr)
slice_of_arr = arr[0:6]
print (slice_of_arr)
slice_of_arr [:] =  99

