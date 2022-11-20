from decorators import count_calls

@count_calls
def say_whee():

    print("whee!")

say_whee()
say_whee()