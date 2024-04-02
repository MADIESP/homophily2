from os import environ

SESSION_CONFIGS = [
dict(
        name='Sondage',
        app_sequence=['Partie0','redirectapp'],
        num_demo_participants=18,
        Tr='one of : Control, T1, T2'
    ),

dict(
        name='Control_Main',
        app_sequence=['Partie1', 'Partie2','Partie3','Partie4','Partie5','Partie6'],
        num_demo_participants=16,
        Treatment=1,
    ),
dict(
        name='T1_Main',
        app_sequence=['Partie1', 'Partie2','Partie3','Partie4','Partie5','Partie6'],
        num_demo_participants=8,
        Treatment=2,
    ),
dict(
        name='T2_Main',
        app_sequence=['Partie1', 'Partie2','Partie3','Partie4','Partie5','Partie6'],
        num_demo_participants=16,
        Treatment=3,
    ),
dict(
        name='Control_Surbooking',
        app_sequence=['Partie1_Surbooking','Partie2_Surbooking','Partie3_Surbooking','Partie4_Surbooking','Partie5_Surbooking','Partie6_Surbooking'],
        num_demo_participants=2,
        Treatment=1,

    ),

dict(
        name='T1_Surbooking',
        app_sequence=['Partie1_Surbooking','Partie2_Surbooking','Partie3_Surbooking','Partie4_Surbooking','Partie5_Surbooking','Partie6_Surbooking'],
        num_demo_participants=2,
        Treatment=2,
    ),

]

ROOMS = [
    {
        'name': 'LEEP',
        'display_name': 'Laboratoire d’Economie Expérimentale de Paris',
        'participant_label_file': '_rooms/LEEP.txt',
    },

    dict(
        name='Class',
        display_name='Class'
    ),
    
    dict(
        name='Control_Main',
        display_name='Control_Main'
    ),
    dict(
        name='T1_Main',
        display_name='T1_Main'
    ),
    dict(
        name='T2_Main',
        display_name='T2_Main'
    ),
    dict(
        name='Control_Surbooking',
        display_name='Control_Surbooking'
    ),
    dict(
        name='T1_Surbooking',
        display_name='T1_Surbooking'
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

bot_labels=[]
for i in range(24): bot_labels.append("bot%d"%(i+1))

# bot_labels+=["AMS", "ATH", "BER", "BRU", "BUD", "DUB", "HEL", "LIS", "LON", "MAD", "MOS", "OSL", "PRA", "RIG", "ROM", "SOF", "VAR", "VIE", "VIL", "ZUR", "LAB", "BOX1", "BOX2", "BOX3", "BOX4", "BOX5", "BOX6", "BOX7", "BOX8"]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc="", bot_labels=bot_labels,
    SERVER_URL=open("config.txt").read().split(";")[1],
    REST_KEY=open("config.txt").read().split(";")[0],
)

PARTICIPANT_FIELDS = ['points_partie4_solo', 'points_partie3_solo','partner_message1', 'partner_message2', 'partner_message3', 'partner_message4', 'partner_message5', 'partner_message6', 'partner_message7', 'partner_message8', 'partner_message9', 'partner_message10', 'partner_message11', 'partner_message12','partner_message13', 'partner_message14', 'partner_message15', 'partner_message16', 'partner_message17', 'partner_message18','Message_selected1', 'Message_selected2', 'Message_selected3', 'Message_selected4','Message_selected5', 'Message_selected6', 'Message_selected7', 'Message_selected8', 'Message_selected9', 'Message_selected10','Message_selected11', 'Message_selected12', 'Message_selected13', 'Message_selected14', 'Message_selected15', 'Message_selected16','Message_selected17', 'Message_selected18','payoff_euros','nb_participants','solo','points_beliefs1', 'points_beliefs2', 'points_beliefs3', 'points_beliefs4','partner_point2', 'partner_point3', 'partner_point4','points_partie2', 'points_partie3', 'points_partie4','points_partie5','expiry', 'sum1', 'InGroupA', 'InGroupB', 'InGroupC', 'InGroupD', 'Main', 'Surbooking', 'ind_payoff', 'vec_couple', 'vec_cv', 'vec_cv_round2', 'vec_cv_round3', 'vec_matching', 'vec_matching_round2', 'vec_matching_round3', 'name_partner', 'name_partner_round2', 'name_partner_round3', 'gender', 'name', 'name_round2', 'name_round3', 'FemaleNames','FemaleNames_round2', 'FemaleNames_round3',  'MaleNames', 'MaleNames_round2', 'MaleNames_round3', 'Message', 'Message_round2', 'Message_round3', 'partner_name', 'partner_name_round2', 'partner_name_round3', 'partner_gender', 'partner_gender_round2', 'partner_gender_round3', 'Job',  'BornIDF', 'CommutingTime','vars_done','error','err_msg']
SESSION_FIELDS = ['initial_grouping','Group_Main','solo','Group_A', 'Group_B','Group_C', 'Group_D', 'cv_A_1',  'cv_A_2', 'cv_A_3', 'cv_A_4', 'cv_B_1', 'cv_B_2', 'cv_B_3', 'cv_B_4','cv_C_1',  'cv_C_2', 'cv_C_3', 'cv_C_4', 'cv_D_1', 'cv_D_2', 'cv_D_3', 'cv_D_4', 'cvA','cvB','cvC','cvD', 'groupA_ch', 'groupA_ch_round2', 'groupA_ch_round3', 'groupB_ch', 'groupB_ch_round2', 'groupB_ch_round3','groupC_ch', 'groupC_ch_round2',  'groupC_ch_round3','groupD_ch',  'groupD_ch_round2',  'groupD_ch_round3','team_1_2_3_4', 'team_5_6_7_8', 'team_1_2_3_4_round2', 'team_1_2_3_4_round3','team_5_6_7_8_round2', 'team_5_6_7_8_round3','zeros_counts', 'zeros_counts2', 'all_names','all_gender' , 'Message_selected_round2', 'Message_selected_round3', 'team1_1', 'team1_2', 'team1_3', 'team1_4','team1_5','team1_6','team1_7','team1_8', 'team2_1', 'team2_2', 'team2_3', 'team2_4','team2_5','team2_6','team2_7','team2_8', 'team3_1', 'team3_2', 'team3_3', 'team3_4','team3_5','team3_6','team3_7','team3_8' ]
STATIC_ROOT = '_static/global'
# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
STATIC_URL = '/static/'

LANGUAGE_CODE = 'fr'
#LANGUAGE_CODE = 'en'
INSTALLED_APPS = [
    'CV',
    'CollectivePlay',
    ...
]

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True
use_browser_bots=True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable


DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4308297569828'


environ['OTREE_ADMIN_PASSWORD'] = '0812'
environ['OTREE_PRODUCTION'] = '1'
environ['OTREE_AUTH_LEVEL'] ='STUDY'

environ['OTREE_REST_KEY'] = SESSION_CONFIG_DEFAULTS['REST_KEY']

ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})
AUTH_LEVEL= environ.get('OTREE_AUTH_LEVEL')