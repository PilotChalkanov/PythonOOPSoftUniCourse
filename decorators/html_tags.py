import functools

def tags(tag:str):
    def decorator_tag(func):
        @functools.wraps(func)
        def wrapper_tag(*args):
            result = f"<{tag}>{func(*args)}</{tag}>"
            return result
        return wrapper_tag
    return decorator_tag

@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))