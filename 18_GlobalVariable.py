Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1
   print(locals().keys())
   print(globals().keys())
print(Money)
AddMoney()
print(Money)
print(locals().keys())
print(globals().keys())
