class Validator:
    def __init__(self, column, constraints, value):
        self.column = column
        self.constraints = constraints
        self.value = self.parse_value(value)

    def check_value_type(self, value):
        if isinstance(value, self.constraints['type']):
            return value

        raise TypeError(f"{self.column} must be a {self.constraints['type']} instead found {type(value)}")

    def parse_value(self, value):
        # if required is specified
        if self.constraints.get("required"):
            #if required check to see if value exists
            if not value:
                raise ValueError(f"{self.column} is a required field")
            
        if self.constraints.get("type"):
            if not self.constraints.get("required") and not value:
                return value
            
            return self.check_value_type(value)

        return value
    