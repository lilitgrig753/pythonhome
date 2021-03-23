import random

ch = random.choice('pu')
point_pc = 0
point_user = 0
point = 0
while (point_user != 4 and point_pc != 4 ):
    if ch == 'u':
        print('User Start')
        point=0
        while True:

            while True:
                user = input('(1-3): ')
                end = 4

                if point > 18:
                    end = 22 - point
                if user.isdigit():
                    user = int(user)
                    if 0 < user < end:

                        print("User-", point, '+', user, '=', point + user)
                        point += user
                        break
                    else:
                        print('\n\tplease input betwen :1', '-', end - 1)
                else:
                    print('\n\tplease input only Number:')

            if point == 21:
                point_pc += 1
                print('\n\tWin PC', "Pc points =", point_pc)
                break

            pc = 4 - point % 4
            print("Pc-", point, '+', pc, '=', point + pc)
            point += pc

            if point == 21:
                point_user += 1
                print('\n\tWin USER', "User points =", point_user)
                break

    if point_user == 1:
        while True:
            while True:
                user = input('(1-3): ')
                end = 4

                if point > 18:
                    end = 22 - point
                if user.isdigit():
                    user = int(user)
                    if 0 < user < end:

                        print("User-", point, '+', user, '=', point + user)
                        point += user
                        break
                    else:
                        print('\n\tplease input betwen :1', '-', end - 1)
                else:
                    print('\n\tplease input only Number:')

            if point == 21:
                point_pc += 1
                print('\n\tWin PC', "Pc points =", point_pc)
                break

            pc = 4 - point % 4
            print("Pc-", point, '+', pc, '=', point + pc)
            point += pc
            point=0

            if point == 21:
                point_user += 1
                point=0
                print('\n\tWin USER', "User points =", point_user)
                break




    else:
        print('Start pc')
        point =0
        while True:
            if point % 4 == 0:
                pc = random.randint(1, 3)
            else:

                pc = 4 - point % 4
            print("Pc-", point, '+', pc, '=', point + pc)
            point += pc

            if point == 21:
                point_user += 1
                print('\n\tWin USER', "User points =", point_user)
                break

            while True:
                user = input('(1-3): ')
                end = 4

                if point > 18:
                    end = 22 - point
                if user.isdigit():
                    user = int(user)
                    if 0 < user < end:

                        print("User-", point, '+', user, '=', point + user)
                        point += user
                        break
                    else:
                        print('\n\tplease input betwen :1', '-', end - 1)
                else:
                    print('\n\tplease input only Number:')

            if point == 21:
                point_pc += 1
                print('\n\tWin PC', "Pc points =", point_pc)
                break
else:
    if(point_user == 4):
        print("Yow winn!!!!!!!!")
    else:
        print("""Yow lose!
        Try Again!""")
