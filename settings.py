from os import environ

SESSION_CONFIGS = [
dict(
        name='TestControl',
        app_sequence=['TestGame'],
        num_demo_participants=2,
        Treatment=1,
    ),

dict(
        name='TestFeedback',
        app_sequence=['TestGame'],
        num_demo_participants=2,
        Treatment=2,
    ),

dict(
        name='TestMessage',
        app_sequence=['TestGame'],
        num_demo_participants=2,
        Treatment=3,
    ),


dict(
        name='CVPlayControl',
        app_sequence=['CV','IndPlay','CollectivePlay'],
        num_demo_participants=8,
        Treatment=1,
    ),
dict(
        name='CVPlayFeedback',
        app_sequence=['CV','IndPlay','CollectivePlay'],
        num_demo_participants=8,
        Treatment=2,
    ),

dict(
        name='CVPlayMessage',
        app_sequence=['CV','IndPlay','CollectivePlay'],
        num_demo_participants=8,
        Treatment=3,
    ),
dict(
        name='TestNames',
        app_sequence=['TestNames'],
        num_demo_participants=2,
    ),
dict(
        name='CV',
        app_sequence=['CV'],
        num_demo_participants=8,
        Treatment=3,

    ),
dict(
        name='CVIndPlay',
        app_sequence=['CV', 'IndPlay'],
        num_demo_participants=8,
        Treatment=3
    ),
dict(
        name='TestChoice',
        app_sequence=['TestChoice'],
        num_demo_participants=1,
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

PARTICIPANT_FIELDS = ['expiry', 'sum1', 'InGroupA', 'InGroupB', 'InGroupC', 'InGroupD', 'ind_payoff', 'vec_couple', 'vec_cv', 'vec_matching', 'name_partner', 'gender', 'name', 'FemaleNames', 'MaleNames', 'Message', 'partner_name', 'partner_gender']
SESSION_FIELDS = ['Group_A', 'Group_B', 'Group_C', 'Group_D', 'cv_A_1', 'cv_A_2', 'cv_A_3', 'cv_A_4', 'cv_B_1', 'cv_B_2', 'cv_B_3', 'cv_B_4', 'cvA','cvB', 'groupA_ch', 'groupB_ch', 'team_1_2_3_4','zeros_counts', 'zeros_counts2', 'all_names','all_gender','name_selected', 'name_NOTselected', 'Message_selected' ]
STATIC_ROOT = '_static/global'
# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
STATIC_URL = '/static/'

LANGUAGE_CODE = 'en'
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


#environ['OTREE_ADMIN_PASSWORD'] = '0812'
#environ['OTREE_PRODUCTION'] = '1'
#environ['OTREE_AUTH_LEVEL'] ='STUDY'

#ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
#DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})
#AUTH_LEVEL= environ.get('OTREE_AUTH_LEVEL')