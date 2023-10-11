from PIL import Image, ImageDraw, ImageFont
import os
from otree.api import *
import numpy as np



doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'TestChoice'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIME_PER_PROBLEM = 5
    CHOICES= ["cvA", "cvB", "cvC", "cvD"]
   # MEN_NAMES = [(1, 'James'), (2, 'David'), (3, 'John'), (4, 'Robert')]
    #WOMEN_NAMES =[(1, 'Mary'), (2, 'Emma'), (3, 'Patricia'), (4, 'Elizabeth')]




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Other player-level variables you may have...

    # Variables for ranking CVs
    rank1 = models.StringField(
        choices=C.CHOICES,
        label="<b> Rank 1st: </b>"
    )

    rank2 = models.StringField(
        choices=C.CHOICES,
        label="<b> Rank 2nd: </b>"
    )

    rank3 = models.StringField(
        choices=C.CHOICES,
        label="<b> Rank 3rd: </b>"
    )

    rank4 = models.StringField(
        choices=C.CHOICES,
        label="<b> Rank 4th: </b>"
    )

    rank1st = models.IntegerField()

    rank2nd = models.IntegerField()

    rank3rd = models.IntegerField()

    rank4th = models.IntegerField()


#FUNCTIONS
def cv(player):

    if player.rank1=="cvA":
        rank1st=1
    elif player.rank1=="cvB":
        rank1st=2
    elif player.rank1=="cvC":
        rank1st=3
    elif player.rank1=="cvD":
        rank1st=4
    if player.rank2=="cvA":
        rank2nd=1
    elif player.rank2=="cvB":
        rank2nd=2
    elif player.rank2=="cvC":
        rank2nd=3
    elif player.rank2=="cvD":
        rank2nd=4
    if player.rank3=="cvA":
        rank3rd=1
    elif player.rank3=="cvB":
        rank3rd=2
    elif player.rank3=="cvC":
        rank3rd=3
    elif player.rank3=="cvD":
        rank4th=4
    if player.rank4=="cvA":
        rank4th=1
    elif player.rank4=="cvB":
        rank4th=2
    elif player.rank4=="cvC":
        rank4th=3
    elif player.rank4=="cvD":
        rank4th=4

    player.rank1st=rank1st
    player.rank2nd=rank2nd
    player.rank3rd=rank3rd
    player.rank4th=rank4th


#def get_choices(player, field_name):
    #return eval(getattr(player, f"{field_name}_choices", "[]"))

from otree.api import *

#class Ranking(Page):
    #form_model = 'player'
    #form_fields = ['rank1st', 'rank2nd', 'rank3rd', 'rank4th']

    #@staticmethod
    #def is_displayed(player):
        # You can use this method to conditionally display the ranking page if needed
        #return True



from otree.api import *

class Ranking(Page):
    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3', 'rank4']

    def before_next_page(player, timeout_happened):
        cv(player)






page_sequence = [Ranking]

