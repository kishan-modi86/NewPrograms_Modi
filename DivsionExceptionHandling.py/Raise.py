from Develop import ZeroError, NegError

__a=50
def division():
    a=int(input('enter the value of a'))
    b = int(input('enter the value of b'))
    if b==0:
        raise ZeroError
    elif a<0 or b<0:
        raise NegError
    else:
        div=a/b
    print(f'div({a},{b})={div}')
