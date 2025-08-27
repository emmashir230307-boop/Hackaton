# pair matching:
import menu
import consts
def match_donor_to_needy(volunteer_id,VOLUNTEER_DICT,NEED_HELP_DICT):
    matched_need_help = []
    # # for donor in donor_dict:
    for needy in NEED_HELP_DICT:
        if VOLUNTEER_DICT[volunteer_id][consts.HELP_OPTIONS] and NEED_HELP_DICT[needy][consts.HELP_OPTIONS] == 'BABYSITTER':
            matched_need_help.append((NEED_HELP_DICT(needy)))
        elif VOLUNTEER_DICT[volunteer_id][consts.HELP_OPTIONS] and NEED_HELP_DICT[needy][consts.HELP_OPTIONS] == 'CLOTHES':
            if VOLUNTEER_DICT[volunteer_id][consts.SUB_CLOTHES] == NEED_HELP_DICT[needy][consts.SUB_CLOTHES]:
                matched_need_help.append((NEED_HELP_DICT(needy)))
        elif VOLUNTEER_DICT[volunteer_id][consts.HELP_OPTIONS] and NEED_HELP_DICT[needy][consts.HELP_OPTIONS] == 'FOOD':
            if VOLUNTEER_DICT[volunteer_id][consts.SUB_FOOD] == NEED_HELP_DICT[needy][consts.SUB_FOOD]:
                matched_need_help.append((NEED_HELP_DICT(needy)))
        elif VOLUNTEER_DICT[volunteer_id][consts.HELP_OPTIONS] and NEED_HELP_DICT[needy][consts.HELP_OPTIONS] == 'PRIVATE LESSONS':
            if VOLUNTEER_DICT[volunteer_id][consts.SUB_LESSONS] == NEED_HELP_DICT[needy][consts.SUB_LESSONS]:
                matched_need_help.append((NEED_HELP_DICT(needy)))

def contacting():



