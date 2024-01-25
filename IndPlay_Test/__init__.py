from PIL import Image, ImageDraw, ImageFont
import os
from otree.api import *
import numpy as np



doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'IndPlay_Test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 4
    TIME_PER_PROBLEM = 30


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    count_ind = models.IntegerField(label="Combien de zéros il y a-t-il dans ce tableau?")
    correct_ind = models.BooleanField(doc="Whether the first sum provided is correct.")
    count_test = models.IntegerField(label="Combien de zéros il y a-t-il dans ce tableau?", initial=4)
    count_error = models.IntegerField(label="Cette réponse est incorrecte, veuillez à nouveau entrer le nombre de zéros dans ce tableau.")





 #FUNCTIONS

def set_correct(player):
    correct_answers = [51, 46, 54, 51]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.count_ind == correct:
            correct_ind = True
        else:
            correct_ind = False

    player.correct_ind = correct_ind



# PAGES

class Instructions(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instructions_Exemple(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1



class WaitforComprehension(WaitPage):
    pass

class ComprehensionCheck(Page):
    form_model='player'
    form_fields = ['count_test']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class ComprehensionCheck_error(Page):
    form_model = 'player'
    form_fields = ['count_error']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.count_test!=4



class Start(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class WaitforCount(WaitPage):
    body_text = "En attente des autres participants pour passer à la première période."

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Count(Page):
    timeout_seconds = C.TIME_PER_PROBLEM
    form_model = 'player'
    form_fields = ['count_ind']
    timer_text = 'Temps restant pour compter ce tableau:'

    def before_next_page(player, timeout_happened):
        set_correct(player)



class WaitForCollective(WaitPage):
   pass





#page_sequence = [Instructions,Instructions_Exemple, WaitforComprehension, ComprehensionCheck,ComprehensionCheck_error,  Start, WaitforCount,  Count, WaitForCollective]
page_sequence = [ Instructions, WaitforCount, Count, WaitForCollective]