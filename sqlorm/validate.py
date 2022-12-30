types = {
   str: {
      "equals": str,
      "len": int,
      "min": int,
      "max": int,
      'startsWith': str,
      'endsWith': str,
      'contains': str,
   }
}

class Validate():
   def __init__(self):
      self.name = self.__class__.__name__
      self.types = types
      self.constraints = {}
      
      for k in dir(self):
         v = getattr(self, k)
         if isinstance(v, tuple):
            self.constraints[k] = v

   def __getitem__(self, key):
      return super().__getattribute__(key)
   
   def __validate(self, t):
      constraintsAllowed = self.types[t]
      
      for c, (constraintValue, constraintMessage) in self.constraints.items():
         if c not in constraintsAllowed:
            raise TypeError(f"Validation '{self.name}' has invalid constraint '{c}' for {t}")
         
         constraintsType = constraintsAllowed[c]
         if not isinstance(constraintValue, constraintsType):
            raise TypeError(f"Validation '{self.name}' has invalid constraint '{c}' expected {constraintsType} got {type(constraintValue)} as value")
   
   def contraintValidation(self, constraint: str, constraintFunc):
      if self.constraints.get(constraint):
         (constraintValue, constraintMessage) = self.constraints[constraint]
         if not constraintFunc(constraintValue):
            raise Exception(constraintMessage)
   
   def str(self):
      self.__validate(str)
      
      def validation(value: str):
         self.contraintValidation("equals", lambda equals: value == equals)
         self.contraintValidation("len", lambda length: len(value) != length)
         self.contraintValidation("min", lambda min: len(value) < min)
         self.contraintValidation("max", lambda max: len(value) > max)
         self.contraintValidation("startsWith", lambda startsWith: value.startswith(startsWith))
         self.contraintValidation("endsWith", lambda endsWith: value.endswith(endsWith))
         self.contraintValidation("contains", lambda contains: contains in value)
         
      return validation