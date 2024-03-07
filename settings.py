from os import environ

SESSION_CONFIGS = [
dict(
        name='tables',
        app_sequence=['tables'],
        num_demo_participants=1,

    ),



dict(
        name='Post_Experiment_Survey',
        app_sequence=['Partie6_Surbooking'],
        num_demo_participants=1,
    ),


dict(
        name='Test_FR_Control',
        app_sequence=['Partie1', 'Partie2','Partie3','Partie4','Partie5','Partie6'],
        num_demo_participants=8,
        Treatment=1,
    ),
dict(
        name='Test_FR_T1',
        app_sequence=['Partie1', 'Partie2','Partie3','Partie4','Partie5','Partie6'],
        num_demo_participants=8,
        Treatment=2,
    ),
dict(
        name='Test_FR_T2',
        app_sequence=['Partie1', 'Partie2','Partie3','Partie4','Partie5','Partie6'],
        num_demo_participants=8,
        Treatment=3,
    ),
dict(
        name='Test_Surbooking_Control',
        app_sequence=['Partie1_Surbooking','Partie2_Surbooking','Partie3_Surbooking','Partie4_Surbooking','Partie5_Surbooking','Partie6_Surbooking'],
        num_demo_participants=2,
        Treatment=1,

    ),

dict(
        name='Test_Surbooking_T1',
        app_sequence=['Partie1_Surbooking','Partie2_Surbooking','Partie3_Surbooking','Partie4_Surbooking','Partie5_Surbooking','Partie6_Surbooking'],
        num_demo_participants=5,
        Treatment=2,
    ),

]

ROOMS = [

    dict(
        name='Class',
        display_name='Class'
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['nb_participants','solo','points_beliefs1', 'points_beliefs2', 'points_beliefs3', 'points_beliefs4','partner_point2', 'partner_point3', 'partner_point4','points_partie2', 'points_partie3', 'points_partie4','points_partie5','expiry', 'sum1', 'InGroupA', 'InGroupB', 'InGroupC', 'InGroupD',  'ind_payoff', 'vec_couple', 'vec_cv', 'vec_cv_round2', 'vec_cv_round3', 'vec_matching', 'vec_matching_round2', 'vec_matching_round3', 'name_partner', 'name_partner_round2', 'name_partner_round3', 'gender', 'name', 'name_round2', 'name_round3', 'FemaleNames','FemaleNames_round2', 'FemaleNames_round3',  'MaleNames', 'MaleNames_round2', 'MaleNames_round3', 'Message', 'Message_round2', 'Message_round3', 'partner_name', 'partner_name_round2', 'partner_name_round3', 'partner_gender', 'partner_gender_round2', 'partner_gender_round3', 'Job',  'BornPA',  'College']
SESSION_FIELDS = ['solo','Group_A', 'Group_B','Group_C', 'Group_D', 'cv_A_1',  'cv_A_2', 'cv_A_3', 'cv_A_4', 'cv_B_1', 'cv_B_2', 'cv_B_3', 'cv_B_4','cv_C_1',  'cv_C_2', 'cv_C_3', 'cv_C_4', 'cv_D_1', 'cv_D_2', 'cv_D_3', 'cv_D_4', 'cvA','cvB','cvC','cvD', 'groupA_ch', 'groupA_ch_round2', 'groupA_ch_round3', 'groupB_ch', 'groupB_ch_round2', 'groupB_ch_round3','groupC_ch', 'groupC_ch_round2',  'groupC_ch_round3','groupD_ch',  'groupD_ch_round2',  'groupD_ch_round3','team_1_2_3_4', 'team_5_6_7_8', 'team_1_2_3_4_round2', 'team_1_2_3_4_round3','team_5_6_7_8_round2', 'team_5_6_7_8_round3','zeros_counts', 'zeros_counts2', 'all_names','all_gender', 'Message_selected' , 'Message_selected_round2', 'Message_selected_round3', 'team1_1', 'team1_2', 'team1_3', 'team1_4','team1_5','team1_6','team1_7','team1_8', 'team2_1', 'team2_2', 'team2_3', 'team2_4','team2_5','team2_6','team2_7','team2_8', 'team3_1', 'team3_2', 'team3_3', 'team3_4','team3_5','team3_6','team3_7','team3_8' ]
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
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
use_browser_bots=True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable


DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4308297569828'


environ['OTREE_ADMIN_PASSWORD'] = '0812'
environ['OTREE_PRODUCTION'] = '1'
environ['OTREE_AUTH_LEVEL'] ='STUDY'

ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})
AUTH_LEVEL= environ.get('OTREE_AUTH_LEVEL')