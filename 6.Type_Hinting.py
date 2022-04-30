# We don't know type of data until runtime

def function(parameter: int) -> str:
    return f"{parameter + 10}"


print(function(10))
    