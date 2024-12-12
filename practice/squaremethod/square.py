def power(param, param1):
    multiple = 1
    for number in range(1, param + 1):
        multiple *= param1
    return multiple

def square(param):
    if isinstance(param, str):
        raise TypeError("Argument must be an integer")
    return param ** 2

def square_root(param):
    if isinstance(param, str):
        raise TypeError("Argument must be an integer")
    return param ** 0.5

def get_maximum(value1, value2, value3):
    maximum = value1
    if(maximum < value2):
        maximum = value2
    if(maximum < value3):
        maximum = value3
    return maximum
