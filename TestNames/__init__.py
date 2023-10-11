from otree.api import *


doc = """
Your app description
"""
# models.py
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'TestNames'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    Fnames = ["Mary", "Emma", "Patricia", "Elizabeth"]
    Mnames= ["James", "David", "John", "Robert"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(label="What gender do you identify with?", widget=widgets.RadioSelectHorizontal,
                                 choices=[[0, "Female"], [1, "Male"]])
    chosen_nameF = models.StringField(
        choices=C.Fnames,
        label="Please select a name that will be assigned to you throughout the experiment:",
        initial="",
    )
    chosen_nameM = models.StringField(
        choices=C.Mnames,
        label="Please select a name that will be assigned to you throughout the experiment:",
        initial="",
    )

    FemaleNames = models.IntegerField()
    MaleNames = models.IntegerField()




# FUNCTIONS

def Fnames(player):
    if player.chosen_nameF=="Mary":
        FemaleNames=1
    elif player.chosen_nameF=="Emma":
        FemaleNames=2
    elif player.chosen_nameF=="Patricia":
        FemaleNames = 3
    elif player.chosen_nameF=="Elizabeth":
        FemaleNames = 4

    player.FemaleNames=FemaleNames


def Mnames(player):

    if player.chosen_nameM == "James":
        MaleNames = 1
    elif player.chosen_nameM == "David":
        MaleNames = 2
    elif player.chosen_nameM == "John":
        MaleNames = 3
    elif player.chosen_nameM == "Robert":
        MaleNames = 4


    player.MaleNames = MaleNames



# PAGES
class Gender(Page):
    form_model = 'player'
    form_fields = ['gender']

class WaitforNames(WaitPage):
    pass


class NameSelectionF(Page):
    form_model = 'player'
    form_fields = ['chosen_nameF']

    def is_displayed(player):
         return player.chosen_nameF == "" and player.gender==0

        # Show the page if the player hasn't chosen a name yet

    def error_message(self, values):
        chosen_nameF = values['chosen_nameF']
        if chosen_nameF in [p.chosen_nameF for p in self.group.get_players()]:
            return "This name was already taken. Please select another name."

    def before_next_page(player, timeout_happened):
        Fnames(player)


class NameSelectionM(Page):
    form_model = 'player'
    form_fields = ['chosen_nameM']

    def is_displayed(player):
         return player.chosen_nameM == "" and player.gender==1

        # Show the page if the player hasn't chosen a name yet

    def error_message(self, values):
        chosen_nameM = values['chosen_nameM']
        if chosen_nameM in [p.chosen_nameM for p in self.group.get_players()]:
            return "This name was already taken. Please select another name."

    def before_next_page(player, timeout_happened):
        Mnames(player)


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Gender, WaitforNames, NameSelectionF,NameSelectionM, ResultsWaitPage, Results]
