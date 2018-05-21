#While loop

'''
while expression:
   statement(s)
'''

count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")

#else with loop

count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")


#single statement suite

flag = 1

while (flag): print ('Given flag is really true!')

print ("Good bye!")

#for loop
'''
for iterating_var in sequence:
   statements(s)
'''

'''
>>> list(range(5))
[0, 1, 2, 3, 4]
'''

for var in list(range(5)):
   print (var)

for letter in 'Python':     # traversal of a string sequence
   print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # traversal of List sequence
   print ('Current fruit :', fruit)

print ("Good bye!")

#iterating by index
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

print ("Good bye!")

#else in loop

numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
   if num%2 == 0:
      print ('the list contains an even number')
      break
else:
   print ('the list doesnot contain even number')