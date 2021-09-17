
from functools import wraps


def add_wrapping_style(style):
    def add_wrapping(item):
        @wraps(item)  #original function name
        def wrapped_item():
            return f"A {style} wrapped up box of {item()}"
        return wrapped_item
    return add_wrapping



@add_wrapping_style("beautifully")
def new_gpu():
    return "A new RTX 3090 TI gpu!!!"

print(new_gpu())
print(new_gpu.__name__)