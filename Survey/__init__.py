from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'Survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    strategy = models.LongStringField(
        label="  Which strategy did you set up with your partner to most efficiently complete the game?")

    gender = models.IntegerField(label="What gender do you identify with?", widget=widgets.RadioSelectHorizontal,
                                 choices=[[0, "Female"], [1, "Male"], [2, "Other"]])

class WaitCounting(WaitPage):
    wait_for_all_groups = True
    body_text = "Please wait for all participants to finish."

class Survey(Page):
    form_model = 'player'
    form_fields = ['strategy', 'gender']



page_sequence = [WaitCounting, Survey]








