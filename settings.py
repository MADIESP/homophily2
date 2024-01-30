from os import environ

SESSION_CONFIGS = [
dict(
        name='tables',
        app_sequence=['tables'],
        num_demo_participants=1,

    ),



dict(
        name='Post_Experiment_Survey',
        app_sequence=['Post_Survey_FR'],
        num_demo_participants=1,
    ),


dict(
        name='Test_FR_Control',
        app_sequence=['CV_FR','IndPlay_FR','CollectivePlay_FR','Round2_FR', 'Round3_FR','Post_Survey_FR'],
        num_demo_participants=8,
        Treatment=1,
    ),
dict(
        name='Test_FR_T1',
        app_sequence=['CV_FR','IndPlay_FR','CollectivePlay_FR','Round2_FR', 'Round3_FR','Post_Survey_FR'],
        num_demo_participants=8,
        Treatment=2,
    ),
dict(
        name='Test_FR_T2',
        app_sequence=['CV_FR','IndPlay_FR','CollectivePlay_FR','Round2_FR', 'Round3_FR','Post_Survey_FR'],
        num_demo_participants=8,
        Treatment=3,
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

PARTICIPANT_FIELDS = ['expiry', 'sum1', 'InGroupA', 'InGroupB', 'InGroupB_round2', 'InGroupB_round3', 'InGroupA_round2', 'InGroupA_round3', 'ind_payoff', 'vec_couple', 'vec_cv', 'vec_cv_round2', 'vec_cv_round3', 'vec_matching', 'vec_matching_round2', 'vec_matching_round3', 'name_partner', 'name_partner_round2', 'name_partner_round3', 'gender', 'name', 'name_round2', 'name_round3', 'FemaleNames','FemaleNames_round2', 'FemaleNames_round3',  'MaleNames', 'MaleNames_round2', 'MaleNames_round3', 'Message', 'Message_round2', 'Message_round3', 'partner_name', 'partner_name_round2', 'partner_name_round3', 'partner_gender', 'partner_gender_round2', 'partner_gender_round3', 'Job',  'BornPA',  'College']
SESSION_FIELDS = ['Group_A', 'Group_B', 'Group_A_round2', 'Group_A_round3', 'Group_B_round2', 'Group_B_round3', 'cv_A_1', 'cv_A_1_round2', 'cv_A_1_round3', 'cv_A_2', 'cv_A_2_round2', 'cv_A_2_round3', 'cv_A_3', 'cv_A_3_round2', 'cv_A_3_round3', 'cv_A_4', 'cv_A_4_round2', 'cv_A_4_round3', 'cv_B_1', 'cv_B_1_round2', 'cv_B_1_round3', 'cv_B_2', 'cv_B_2_round2', 'cv_B_2_round3', 'cv_B_3', 'cv_B_3_round2', 'cv_B_3_round3', 'cv_B_4', 'cv_B_4_round2', 'cv_B_4_round3', 'cvA', 'cvA_round2', 'cvA_round3','cvB', 'cvB_round2', 'cvB_round3', 'groupA_ch', 'groupA_ch_round2', 'groupA_ch_round3', 'groupB_ch', 'groupB_ch_round2', 'groupB_ch_round3', 'team_1_2_3_4', 'team_1_2_3_4_round2', 'team_1_2_3_4_round3','zeros_counts', 'zeros_counts2', 'all_names', 'all_names_round2', 'all_names_round3','all_gender','name_selected','name_selected_round2', 'name_selected_round3',  'name_NOTselected', 'name_NOTselected_round2', 'name_NOTselected_round3', 'Message_selected' , 'Message_selected_round2', 'Message_selected_round3', 'team1_4', 'team1_4_round2', 'team1_4_round3', 'team1_3', 'team1_3_round2', 'team1_3_round3', 'team1_2', 'team1_2_round2', 'team1_2_round3', 'team1_1', 'team1_1_round2', 'team1_1_round3']
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