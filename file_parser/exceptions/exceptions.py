class NotImplementedException(Exception):
    message:str = "Not implemented yet"
    
    def __init__(self):
        super().__init__(self.message)

class NotSupportedFileException(Exception):
    message:str = "Not supported file format"
    
    def __init__(self):
        super().__init__(self.message)

class GenericException(Exception):
    message:str = "Something wrong here"
    
    def __init__(self):
        super().__init__(self.message)

'''
-----------------------------------------
Input files exceptions
'''
class InputFileNotFoundException(Exception):
    message:str = "Input file not found"

    def __init__(self):
        super().__init__(self.message)

class InputFileNotPermissionToReadException(Exception):
    message:str = "No permission to read input file"

    def __init__(self):
        super().__init__(self.message)

'''
-----------------------------------------
Parsing exceptions
'''

class InvalidStringException(Exception):
    message:str = "Input content is not a string"
    
    def __init__(self):
        super().__init__(self.message)

class InvalidDictException(Exception):
    message:str = "Input content is not a dict"
    
    def __init__(self):
        super().__init__(self.message)

class EmptyContentException(Exception):
    message:str = "Input content is empty"

    def __init__(self):
        super().__init__(self.message)

'''
-----------------------------------------
Headers exception
'''

class EmptyHeadersException(Exception):
    message:str = "Empty headers"

    def __init__(self):
        super().__init__(self.message)