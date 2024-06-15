import builtins

def case_insensitive_input(func):
    def wrapper(*args, **kwargs):
        def convert_input(s):
            return s.lower()

        old_input_func = builtins.input  # Save the original input function
        builtins.input = lambda prompt="": convert_input(old_input_func(prompt))
        result = func(*args, **kwargs)
        builtins.input = old_input_func  # Restore the original input function
        return result

    return wrapper
