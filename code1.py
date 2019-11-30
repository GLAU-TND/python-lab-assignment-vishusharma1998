try:
    a=str()
    print(a.append())
    x=int(input('Enter a first number'))
    y=input('Enter a second number')
    print('result',x//y)
    print('result',x+y)
except AttributeError:
           print('Error')

except TypeError:
           print('Not possible')

except ValueError:
           print('Error Occured')
    
