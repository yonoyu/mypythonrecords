# class MyCustomError(Exception):
class MyCustomError(TypeError):
    """
    Exception raised when a specifc error code is needed.
    """
    #call the super class constructor with the message as an argument
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code #property of MyCustomError object
       
err = MyCustomError('An error occurred.', 500)
print(err.__doc__) #output:  Exception raised when a specifc error code is needed.
# raise MyCustomError("OUCH! An error happened.", 500)



print("""
    Hello
How are you""")