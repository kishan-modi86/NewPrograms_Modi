from Exception_ import CnameError,CnumError,UnitError
from Raise_ import CustomerName,CustomerNumber,units
import sys
while True:
     try:
         a=CustomerName()
         b = CustomerNumber()
         unt, rt,Schrge,SSchrg = units()
     except CnameError:
         print("Don't enter digit,alnum,or symbols in name........")
     except CnumError:
         print("Don't enter alphabets,symbols in cnum......")
     except UnitError:
         print("Don't enter str,alnum,symbols in unit.........")
     else:
         print('*' * 30)
         print(f'''      Customer Details
Customer Name       {" ".join(a)}
Customer Number     {"".join(b)}
{'*'*30}
Units    consumed   {unt}
Rate                {rt}
Scharge             {Schrge}
Sscharge            {SSchrg}
{'*'*30}
Total Cost           {(rt*unt)+SSchrg+Schrge}
{'*'*30}
            ''')
         sys.exit()




