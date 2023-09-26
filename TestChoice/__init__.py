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
   # MEN_NAMES = [(1, 'James'), (2, 'David'), (3, 'John'), (4, 'Robert')]
    #WOMEN_NAMES =[(1, 'Mary'), (2, 'Emma'), (3, 'Patricia'), (4, 'Elizabeth')]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Other player-level variables you may have...

    # Variables for ranking CVs
    rank1st = models.StringField(
        choices=["cvA", "cvB", "cvC", "cvD"],
        label="Rank 1st:"
    )

    rank2nd = models.StringField(
        choices=[],  # This will be dynamically populated based on the choice for rank1st
        label="Rank 2nd:"
    )

    rank3rd = models.StringField(
        choices=[],  # This will be dynamically populated based on the choices for rank1st and rank2nd
        label="Rank 3rd:"
    )

    rank4th = models.StringField(
        choices=[],# This will be dynamically populated based on the choices for rank1st, rank2nd, and rank3rd
        label="Rank 4th:"
    )


 #FUNCTIONS
# myapp/pages.py

from otree.api import *

class Ranking(Page):
    form_model = 'player'
    form_fields = ['rank1st', 'rank2nd', 'rank3rd', 'rank4th']

    @staticmethod
    def is_displayed(player):
        # You can use this method to conditionally display the ranking page if needed
        return True

    def vars_for_template(player):
        # You can pass context variables to the template here if needed
        return {}

    def before_next_page(player, timeout_happened):
        # Optionally, you can add custom logic here before moving to the next page
        pass

    @staticmethod
    def js_vars(player):
        # You can pass variables from Python to JavaScript here if needed
        return {}


page_sequence = [Ranking]

