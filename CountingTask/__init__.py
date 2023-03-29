from otree.api import *
import random



doc = """
Counting Task 
"""

class C(BaseConstants):
    NAME_IN_URL = 'CountingTask'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIME_PER_PROBLEM = 45  # 20 was announced but 45 was actually allotted per question
    #PAYMENT_CURRENT_PER_ITEM = cu(1)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

            pass


class Player(BasePlayer):
     answer= models.IntegerField(label="Please enter the correct number of 0s.")



class Counting(Page):
    timeout_seconds = C.TIME_PER_PROBLEM

    form_model = 'player'
    form_fields = ['answer']


page_sequence = [Counting]