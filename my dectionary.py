fruit_dectionary={}
option=True
while True:
    print('[A] Add\n [B] View\n [C] Delete\n [D] Clear all\n [E] Updaten\n [F] Exit Program ')

    option=input('enter your choice:'.lower())
    if option.lower()=='a':
        item=input('enter fruit to be added: ')
        if item in fruit_dectionay:
            print('item already exist!')

        else:
            ammount=int(input('enter ammount to be added: '))
            fruit_dectionary[item]=ammount
        elif option.lower()=='b':
                for item in fruit_dectionary:
                    print(item,': ammount:', fruit_dectionary[item])
            elif option.lower()=='c':
                item=input('enter item to be deleted: ')
                del(fruit_dectionary[item])
                print('item deleted sucessfully!')
            elif option.lower()=='d':
                fruit_dectionary.clear()
                print('all item cleared!')
            elif option.lower()=='e':
                item=input('enter item to be updated: ')
                if item in fruit_dectionary:
                    ammount=int(input('enter ammount of updated item: '))
                    fruit_dectionary[item]=fruit_dectionary[item]=ammount
                    print('item sucessfully updated: ')
                else:
                    print('item not found! press [A] to add item in dectionary')
            elif option.lower()=='f':
                print('bye!!\n thankyou')
                break
            else:
                print('error')
                
