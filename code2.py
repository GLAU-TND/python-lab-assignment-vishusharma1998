class MyException(Exception):
    pass
   


def xyz(a,b):
    c = a+b
    if c<150:
        raise MyException("Custom Exception Occurred")
    else:
        return c
   

print(xyz(30,40))
