class Networkerror(Exception):
   def __init__(self, arg):
      self.args = arg


try:
   raise Networkerror("Bad network")
except Networkerror as e:
   print(e.args)