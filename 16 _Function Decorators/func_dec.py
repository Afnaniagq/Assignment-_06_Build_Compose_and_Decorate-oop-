# This is a decorator function that takes another function as input
def log_function_call(func):  

    # This is the inner function that adds extra behavior
    def wrapper():
        # This line runs before the actual function call
        print("Function is being called")
        
        # This calls the original function passed to the decorator
        func()

    # The decorator returns the inner wrapper function
    return wrapper


# This applies the decorator to the say_hello function
@log_function_call
def say_hello():
    # This is the actual function body
    print("Hello, World!")


# This calls the decorated function (which is now the wrapper)
say_hello()


    
 