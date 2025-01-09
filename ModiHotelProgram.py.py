print('*'*32)
print('''     MENU MODI HOTEL
        ITEM     PRICE
    1.  COFFEE    20
    2.  TEA       10
    3.  BISCUIT   5
    4.  SAMOSA    10
    0.  Exit 
''')
print('*'*32)
import sys
total_amt=0
lst=[]

while (True):
    try:
    
        ch=int(input('enter your choice from above menu: '))
        print('-'*32)
        
        match ch:
                case 1:
                    while True:
                        try:
                            
                            qnt=int(input('enter how many cups of coffee you want: '))
                            print('-'*32)
                            total_amt=total_amt+qnt*20
                            lst.append([qnt,'       Coffee','      Amount----->',qnt*20])
                            break
                        except ValueError:
                            print("""Error: Don't Enter quantity of coffee in str,alnum.....
please enter number""")
                case 2:
                    while True:
                        try:
                            
                            qnt=int(input('enter how many cups of Tea you want: '))
                            print('-'*32)
                            
                            total_amt=total_amt+qnt*10
                            lst.append([qnt,'       Tea','         Amount----->',qnt*10])
                            break
                        except ValueError:
                            print("""Error: Don't Enter quantity of coffee in str,alnum.....
please enter number""")
                case 3:
                    while True:
                        try:
                            
                            qnt=int(input('enter how many Biscuits you want: '))
                            print('-'*32)
                            total_amt=total_amt+qnt*5
                            lst.append([qnt,'       Biscuit','     Amount----->',qnt*5])
                            break
                        except ValueError:
                            print("""Error: Don't Enter quantity of coffee in str,alnum.....
please enter number""")
                case 4:
                    while True:
                        try:
                           
                            qnt=int(input('enter how many Samosa you want: '))
                            print('-'*32)
                            
                            total_amt=total_amt+qnt*10
                            lst.append([qnt,'       Samosa','      Amount----->',qnt*10])
                            break
                        except ValueError:
                            print("""Error: Don't Enter quantity of coffee in str,alnum.....
please enter number""")
                case 0:
                    print(f'\n\n\n{'*'*32}')
                    for i in range(len(lst)):
                        for j in range(len(lst[i])):
                            print(f'{lst[i][j]}',end=" ")
                        print()
                    print('-'*32)
                    print(f'\n\t\t\tTotal Bill: {total_amt}\n')
                    print('\t\tVisit Again Sir')
                    print(f'{'*'*32}\n\n\n')
                    sys.exit()
    except ValueError:
            print(f"""Don't enter str,alnums and all....
Please Enter Your Choice as 1,2,3,4,0""")

print("Thanks a lot!!!!!!!")
        
            
