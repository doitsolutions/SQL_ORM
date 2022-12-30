types = {
   str: {
      "min": int,
      "max": int,
   }
}

class Validate():
   def __init__(self):
      self.types = types
      self.constraints = {}
      
      for k in dir(self):
         v = getattr(self, k)
         if isinstance(v, tuple):
            self.constraints[k] = v

   def __getitem__(self, key):
      return super().__getattribute__(key)
   
   def __validate(self, type):
      if type not in self.types:
         raise TypeError(f"validation {type} not implemented")
      
      constraintsType = self.types[type]
      
      for c, v in self.constraints.items():
         if c not in constraintsType:
            raise TypeError(f"validation {type} has invalid constraint '{c}'")
   
   def str(self):
      self.__validate(str)