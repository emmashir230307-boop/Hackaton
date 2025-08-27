
import consts
def find_user_type(id_num):
    for helper in consts.VOLUNTEER_DICT.keys():
        if id_num == helper:
            return consts.VOLUNTEER_DICT[helper]['user type']
    for needy in consts.NEED_HELP_DICT.keys():
        if id_num == needy:
            return consts.NEED_HELP_DICT[needy]['user type']
    print()

def match_donor_to_needy(id_num,user_type):
    match=False
    if user_type==consts.VOLUNTEER:
        for needy in consts.NEED_HELP_DICT.keys():
            if consts.NEED_HELP_DICT[needy]['help type']==consts.VOLUNTEER_DICT[id_num]['help type']:
                match=needy
    else:
        for helper in consts.VOLUNTEER_DICT.keys():
            if consts.VOLUNTEER_DICT[helper]['help type']==consts.NEED_HELP_DICT[id_num]['help type']:
                match=helper
    return match

def contacting(id_num):
    user_type=find_user_type(id_num)
    match=match_donor_to_needy(id_num,user_type)
    if not match:
        print('no match right now, we wrote you in our data base.')
    elif user_type==consts.VOLUNTEER:
        print(f'match found, need help: {consts.NEED_HELP_DICT[match]['name']} \n phone number: {consts.NEED_HELP_DICT[match]["phone number"]}')
    else:
        print(f'match found, can help: {consts.VOLUNTEER_DICT[match]['name']} \n phone number: {consts.VOLUNTEER_DICT[match]["phone number"]}')