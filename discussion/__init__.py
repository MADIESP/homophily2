from otree.api import *


doc = """
Non work-related discussion 
"""


class C(BaseConstants):
    NAME_IN_URL = 'discussion'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Topic= models.FloatField(widget=widgets.RadioSelectHorizontal,
                                              choices=[[1,'Taylor Swift songs'], [2,'US cities'], [3,'Football teams']], label="<b>Please select your preferred discussion topic: </b>")
    Topic2= models.FloatField(widget=widgets.RadioSelectHorizontal,
                                              choices=[[1,'I agree'], [2,' I propose to discuss US cities'], [3,'I propose to discuss Football teams']], label="If yes, press the bottom I agree. If not, propose another topic to your partner.")

    Topic3=models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=[[1,'Yes'], [2,'No']], label="Do you agree?")
    question= models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=[[1, 'Yes'], [2, 'No']],
                                 label=" <b>Does player 1 like NYC? </b>")


# PAGES
class Topic(Page):
    form_model = 'player'
    form_fields = ['Topic']

class Topic2(Page):
    form_model = 'player'
    form_fields = ['Topic2']


class Topic3(Page):
    form_model = 'player'
    form_fields = ['Topic3']

class end(Page):
        form_model = 'player'
        form_fields = ['question']



page_sequence = [Topic, Topic2, Topic3, end]

