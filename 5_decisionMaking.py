#if statement

'''
if expression:
   statement(s)
'''

var1 = 100
if var1:
   print ("1 - Got a true expression value")
   print (var1)

var2 = 0
if var2:
   print ("2 - Got a true expression value")
   print (var2)
print ("Good bye!")

#if else statement

'''
if expression:
   statement(s)

else:
   statement(s)
'''

amount = int(input("Enter amount: "))

if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
else:
    discount = amount * 0.10
    print("Discount", discount)

print("Net payable:", amount - discount)

#elif

'''
if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)
'''

amount = int(input("Enter amount: "))

if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
elif amount < 5000:
    discount = amount * 0.10
    print("Discount", discount)
else:
    discount = amount * 0.15
    print("Discount", discount)

print("Net payable:", amount - discount)

#nested if

'''
if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else
      statement(s)
elif expression4:
   statement(s)
else:
   statement(s)
'''

num = int(input("enter number"))
if num%2 == 0:
   if num%3 == 0:
      print ("Divisible by 3 and 2")
   else:
      print ("divisible by 2 not divisible by 3")
else:
   if num%3 == 0:
      print ("divisible by 3 not divisible by 2")
   else:
      print  ("not Divisible by 2 not divisible by 3")


#single line if clause

var = 100
if ( var  == 100 ) : print ("Value of expression is 100")
print ("Good bye!")

