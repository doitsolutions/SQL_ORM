class Validator:
    """
    Class to handle data validation of passed in arguments\n
    Example: Validator(key={'value': 'foo', 'required': True, 'type': str})\n
    'key' - column name *(required if the column has value)\n
    'required' - bool to decide whether or not the value is required *(this is not a required field)\n
    'type' - type of the value being supplied *(not a required field)\n
    'value' - content of the key *(not a required field)
    """
    def __init__(self, **kwargs):
        # loop through attributes passed in
        for key in kwargs:
            # initialize empty value
            value = None
            # if key has value
            if kwargs.get(key):
                element = kwargs.get(key)
                # check to make sure that element is a object
                self.check_kwarg_type(key, element)
                # parse components of element and compute on them
                value = self.parse_element(key, element)

            setattr(self, key, value)


    def check_kwarg_type(self, key, element):
        """
        Function to check if the element coming into the kwargs is an object that has required validation fields\n
        key - key of the passed in object element\n
        element - object containing the value
        """
        if isinstance(element, dict):
            return True
        raise TypeError(f"{key} must be a {dict} instead found {type(element)}")

    def parse_element(self, key, element):
        """
        Function to parse an element, check its components and run validation on them\n
        key - key of the passed in object element\n
        element - object containing the value
        """
        # if required is specified
        if element.get("required"):
            #if required check to see if value exists
            if element.get("value"):

                # if var type is specified
                if element.get("type"):
                    if not isinstance(element.get("value"), element.get("type")):
                        raise TypeError(f"value: {element.get('value')} is not of type: {element.get('type')} but is instead of type: {type(element.get('value'))}")
                # assign value to output var
                return element["value"]
            # otherwise raise value error
            raise ValueError(f"{key} is a required field")
        # otherwise assign value to output var
        return element.get("value")