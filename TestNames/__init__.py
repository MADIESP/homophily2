from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'TestNames'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    available_FemaleNames=[ "Mary","Emma","Patricia","Elizabeth"]
    available_MaleNames= [ "James","David","John","Robert"]
    available_names= [ "James","David","John","Robert"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    chosen_name = models.StringField()


def get_available_names(group):
    chosen_names = [player.chosen_name for player in group.get_players() if player.chosen_name]
    return [name for name in C.available_names if name not in chosen_names]

# PAGES
class ChooseName(Page):
    form_model = 'player'
    form_fields = ['chosen_name']


    def before_next_page(player):
        chosen_name = player.chosen_name
        group=player.group
        if chosen_name:
            group.get_available_names().remove(chosen_name)

    def vars_for_template(player):
        available_names = player.group.available_names()
        return {'available_names': available_names}







page_sequence = [ChooseName]
