from PIL import Image, ImageDraw, ImageFont
import os
from otree.api import *
import numpy as np



doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Exemple_Tableau'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIME_PER_PROBLEM = 30


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    count_ind = models.IntegerField(label="Combien de 0s il y a-t-il dans ce tableau?")




class Count(Page):
    timeout_seconds = C.TIME_PER_PROBLEM
    form_model = 'player'
    form_fields = ['count_ind']
    timer_text = 'Temps restant pour compter ce tableau:'


page_sequence = [ Count]