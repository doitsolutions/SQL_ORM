import re

types = {
   str: {
      "equals": str,
      "length": int,
      "min": int,
      "max": int,
      'startsWith': str,
      'endsWith': str,
      'contains': str,
      'regex': str
   },
   int: {
      "equals": int,
      "min": int,
      "max": int,
   }
}

class BaseValidate():
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
            raise TypeError(f"Validate '{self.name}' invalid constraint '{c}' for .{t.__name__}()")
         
         constraintsType = constraintsAllowed[c]
         if not isinstance(constraintValue, constraintsType):
            raise TypeError(f"Validate '{self.name}' constraint '{c}' value must be {constraintsType} instead got {type(constraintValue)}")
   
   def constraintValidate(self, constraint: str, constraintFunc):
      if self.constraints.get(constraint):
         (constraintValue, constraintMessage) = self.constraints[constraint]
         if not constraintFunc(constraintValue):
            raise TypeError(constraintMessage)
   
   def str(self):
      self.__validate(str)
      
      def validation(value: str):
         self.constraintValidate("equals", lambda equals: value == equals)
         self.constraintValidate("len", lambda length: len(value) == length)
         self.constraintValidate("min", lambda min: len(value) >= min)
         self.constraintValidate("max", lambda max: len(value) <= max)
         self.constraintValidate("startsWith", lambda startsWith: value.startswith(startsWith))
         self.constraintValidate("endsWith", lambda endsWith: value.endswith(endsWith))
         self.constraintValidate("contains", lambda contains: contains in value)
         self.constraintValidate("regex", lambda regex: re.match(regex, value))
         
      return validation
   
   def int(self):
      self.__validate(int)
      
      def validation(value: int):
         self.constraintValidate("equals", lambda equals: value == equals)
         self.constraintValidate("min", lambda min: value >= min)
         self.constraintValidate("max", lambda max: value <= max)
         
      return validation