#division
import sys
while True:
    from Develop import ZeroError,NegError
    from Raise import division
    try:
        division()
    except NegError:
        print("Don't Enter Negative Numbers in b or a")
    except ZeroError:
        print("Don't Enter 0 in b----Try Again")
    except ValueError:
        print("Don't Enter str,alnum.....symbols")
    else:
        print("Thank YOU")
        sys.exit()
