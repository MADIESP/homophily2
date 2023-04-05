from os import environ

SESSION_CONFIGS = [
dict(
        name='Counting',
        app_sequence=['Counting_part1','Counting_Collab', 'Survey'],
        num_demo_participants=2,
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

PARTICIPANT_FIELDS = ['expiry', 'sum1', 'answerA', 'answerB', 'sum2', 'sumE', 'answer1','sum', 'answerA_ind', 'answerB_ind', 'ind_payoff']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

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