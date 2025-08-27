import consts
import worker

def start(id_num,password):
    while not id_num.isdigit() or len(id_num)!=9:
        print('Invalid id')
        id_num=input("Enter id number: ")
    if id_num in consts.DONOR_DICT.keys():
        if password!=consts.DONOR_DICT['ID']['[password']:
            print('Wrong password')
        else:
            print('signed in successfully')
    elif id in consts.NEED_HELP_DICT.values():
        if password!=consts.NEED_HELP_DICT['ID']['[password']:
            print('Wrong password')
        else:
            print('signed in successfully')
    else:
        signup(id_num,password)

def signup(id_num,password):
    count=0
    name=input("Enter your name:")
    while not name.isalpha():
        print('Invalid name')
        name=input("Enter your name:")
        continue
    phone_num=input("Enter phone number:")
    while not phone_num.isdigit() or len(phone_num)!=10 or phone_num[0]!=0 or phone_num[1]!=5:
        print('Invalid phone number')
        phone_num=input("Enter phone number:")
        continue
    for i in consts.USERS_TYPE:
        count+=1
        print(count, i)
    user_type=input("what are you?:")
    while user_type.upper() not in consts.USERS_TYPE:
        print('Invalid user type')
        user_type=input("what are you?:")
        continue
    for j in consts.HELP_OPTIONS:
        print(count,j)
    help_type=input("Enter What type of help you need/able to give: ")
    while help_type.upper() not in consts.HELP_OPTIONS:
        print('Invalid help type')
        help_type=input("Enter What type of help you need/able to give: ")
        continue
    if user_type==consts.DONOR:
        if worker.legit():
            consts.DONOR_DICT[id_num]= {'password':password,
                                          'user type':user_type.upper(),
                                          'help type':help_type.upper(),
                                          'name':name,
                                          'phone number':phone_num}
        else: exit()
    else:
        consts.NEED_HELP_DICT.update(id_num, {'password': password,
                                      'user type': user_type.upper(),
                                      'help type': help_type.upper(), 'name': name,
                                      'phone number': phone_num})
