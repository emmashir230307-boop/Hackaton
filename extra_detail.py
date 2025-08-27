from consts import LONELY_SOLDIER, EVICTED_FAM,MILITARY_SERVICE_FAM

def receive_food ():
    # need to fix the way of getting usert ype from the dict
    if user_type==LONELY_SOLDIER:
        soldier_choice=input("enter what you like, \n type 1 for getting invitation for dinner or kidosh \n type 2 to get a hot meal: ")
        return soldier_choice
    elif user_type==EVICTED_FAM or user_type==MILITARY_SERVICE_FAM:
        fam_choice=input("type 1 to get hot meal")
        return fam_choice

def receive_babysitter ():
    baby=input("if you have baby enter 1 if not enter 0")
    child_num=input("enter your number of children: ")
    return baby,child_num

def receive_lessons ():
    lesson_sub=input("press 1 to get math lesson \n press 2 to get english lesson \n press 3 to get science lesson")
    return lesson_sub

def receive_clothes():
    clothes_type=input("press 1 to get laundry \n press 2 to get  mending and sewing")
    return clothes_type