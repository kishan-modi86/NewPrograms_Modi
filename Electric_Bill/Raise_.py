from Exception_ import CnameError, CnumError, UnitError

def CustomerNumber():
    cnum = input('enter the number: ').split()
    for val in cnum:
        if not val.isdigit():
            raise CnumError

    return cnum
def CustomerName():
    cname=input('enter the name: ').split()
    for val in cname:
        if  not  val.isalpha():
            raise CnameError
    return cname
def units():
    sscharge=25
    scharge=15
    Unit=input('enter the total unit consumed: ')
    for val in Unit:
        if not Unit.isdigit():
            raise UnitError
    unit=float(Unit)
    if 0<=unit<51:
        rate=0
        sscharge=0
        scharge=0
    elif 50<unit<101:
        rate=4
        sscharge=25
        scharge=15
    elif 100<unit<151:
        rate=6
        sscharge=25
        scharge=15
    elif 150<unit:
        rate=8
        sscharge=25
        scharge=15

    return unit,rate,sscharge,scharge







