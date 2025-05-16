from . import _class_primitives  # The actual C++ module

class Data:
    def __init__(self, name, value):
        """Create a Data object with a name and value.
        
        Args:
            name: The name of the data object
            value: The value for the data object
        """
        self._impl = _class_primitives.Data(name, value)
    
    @classmethod
    def from_name(cls, name):
        """Create a Data object with just a name.
        
        This uses the C++ constructor that only takes a name parameter.
        
        Args:
            name: The name of the data object
            
        Returns:
            A new Data instance
        """
        instance = cls.__new__(cls)
        instance._impl = _class_primitives.Data(name)  # Call single-parameter constructor
        return instance
    
    @classmethod
    def from_values(cls, name, value):
        """Create a Data object with a name and value.
        
        This is equivalent to using the standard constructor.
        
        Args:
            name: The name of the data object
            value: The value for the data object
            
        Returns:
            A new Data instance
        """
        return cls(name, value)
    
    @property
    def name(self):
        return self._impl.name
        
    @name.setter
    def name(self, value):
        self._impl.name = value
    
    @property
    def value(self):
        return self._impl.value

    @value.setter
    def value(self, value):
        self._impl.value = value

    def to_string(self):
        return self._impl.to_string()
    
    
        