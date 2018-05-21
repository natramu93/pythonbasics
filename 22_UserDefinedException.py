class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg


try:
   raise Networkerror("Bad hostname")
except Networkerror as e:
   print(e.args)