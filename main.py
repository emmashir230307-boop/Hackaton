import connections
import menu

def main():
    search_help=False #change later to input of user to search
    id_num=int(input("Enter ID: "))
    password=input("Enter Password: ")
    menu.start(id_num,password)
    if search_help:
        user_type=connections.find_user_type(id_num)
        match_id=connections.match_donor_to_needy(id_num,user_type)
        connections.contacting(match_id)
    else:
        pass