from functools import wraps

# Custom decorator with advanced capabilities
def custom_decorator(condition):
    # Decorator function that takes the original method as input
    def decorator(func):
        @wraps(func)
        # Wrapper function that intercepts method calls
        def wrapper(*args, **kwargs):
            if condition:
                # Modify arguments before calling the original method
                modified_args = [arg + 1 if isinstance(arg, int) else arg for arg in args]
                print("Modified arguments:", modified_args)

                # Call the original method with modified arguments
                result = func(*modified_args, **kwargs)

                # Alter the return value of the original method
                modified_result = result * 2
                print("Modified return value:", modified_result)

                # Change method execution flow based on the result
                if result > 10:
                    print("Result is greater than 10!")
                else:
                    print("Result is less than or equal to 10!")

                return modified_result
            else:
                # If condition is False, call the original method as it is
                return func(*args, **kwargs)

        return wrapper
    return decorator

# Example class using the custom decorator
class MyClass:
    @custom_decorator(condition=True)
    # Method to be decorated
    def my_method(self, x, y):
        return x + y

# Test the decorated method
obj = MyClass()
result = obj.my_method(3, 4)
print("Final result:", result)
