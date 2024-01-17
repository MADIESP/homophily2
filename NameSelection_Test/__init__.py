from PIL import Image, ImageDraw, ImageFont
import os
from otree.api import *
import numpy as np



doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'NameSelection_Test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    Fnames = ["Mary", "Emma", "Patricia", "Elizabeth", "Charlotte", "Lisa", "Amelia", "Jessica", "Sarah", "Karen"]
    Mnames = ["James", "David", "John", "Robert", "Liam", "Noah", "William", "Henry", "Thomas", "Christopher"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    Group_A = models.LongStringField()
    Group_B = models.LongStringField()
    cvA = models.LongStringField()
    cvB = models.LongStringField()
    cv_A_1 = models.LongStringField()
    cv_A_2 = models.LongStringField()
    cv_A_3 = models.LongStringField()
    cv_A_4 = models.LongStringField()
    cv_B_1 = models.LongStringField()
    cv_B_2 = models.LongStringField()
    cv_B_3 = models.LongStringField()
    cv_B_4 = models.LongStringField()



class Player(BasePlayer):
    survey_error_displayed = models.BooleanField(initial=False)
    gender = models.IntegerField(label="À quel genre vous identifiez-vous ?", widget=widgets.RadioSelectHorizontal,
                                     choices=[[0, "Femme"], [1, "Homme"]])
    BornPA = models.IntegerField(label="Etes vous né.e en  Ile de France?", widget=widgets.RadioSelectHorizontal,
                                     choices=[[1, "Oui"], [0, "Non"]], initial=0)
    Job = models.IntegerField(label="Quel est votre temps de trajet quotidien (pour vous rendre à vos activités principales (travail, études, autres engagements)) ?", widget=widgets.RadioSelectHorizontal,
                                  choices=[[1, " < 30 minutes"], [0, "> 30 minutes"]], initial=0)
    FemaleNames = models.IntegerField()
    MaleNames = models.IntegerField()
    chosen_nameF = models.StringField(
        choices=C.Fnames,
        label="Veuillez choisir un prénom fictif qui vous sera attribué durant toute l'expérience:",
        initial="",
    )
    chosen_nameM = models.StringField(
        choices=C.Mnames,
        label="Veuillez choisir un prénom fictif qui vous sera attribué durant toute l'expérience:",
        initial="",
    )
    name = models.IntegerField()
    partner_name = models.IntegerField()
    partner_gender = models.IntegerField(label="What gender do you identify with?", widget=widgets.RadioSelectHorizontal,
                                     choices=[[0, "Female"], [1, "Male"]])






 #FUNCTIONS

def Fnames(player):
    if player.chosen_nameF=="Mary":
        FemaleNames=1
    elif player.chosen_nameF=="Emma":
        FemaleNames=2
    elif player.chosen_nameF=="Patricia":
        FemaleNames = 3
    elif player.chosen_nameF=="Elizabeth":
        FemaleNames = 4
    elif player.chosen_nameF == "Charlotte":
        FemaleNames = 5
    elif player.chosen_nameF == "Lisa":
        FemaleNames = 6
    elif player.chosen_nameF == "Amelia":
        FemaleNames = 7
    elif player.chosen_nameF == "Jessica":
        FemaleNames = 8
    elif player.chosen_nameF == "Sarah":
        FemaleNames = 9
    elif player.chosen_nameF == "Karen":
        FemaleNames = 10


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
    elif player.chosen_nameM == "Liam":
        MaleNames = 5
    elif player.chosen_nameM == "Noah":
        MaleNames = 6
    elif player.chosen_nameM == "William":
        MaleNames = 7
    elif player.chosen_nameM == "Henry":
        MaleNames = 8
    elif player.chosen_nameM == "Thomas":
        MaleNames = 9
    elif player.chosen_nameM == "Christopher":
        MaleNames = 10


    player.MaleNames = MaleNames


def gender(player):
    player.participant.gender = player.gender
    player.participant.BornPA=player.BornPA
    player.participant.Job=player.Job


def Femalename(player):
    player.participant.FemaleNames = player.FemaleNames
    player.participant.name = player.participant.FemaleNames


def Malename(player):
    player.participant.MaleNames = player.MaleNames
    player.participant.name = player.participant.MaleNames




# PAGES
class Instructions(Page):
    form_model = 'player'

class WaitForSurvey(WaitPage):
    pass
class Survey(Page):
    form_model = 'player'
    form_fields = ['gender' ]

    def before_next_page(player, timeout_happened):
        gender(player)

    def error_message(player, timeout_happened):
        if not player.survey_error_displayed:
            player.survey_error_displayed = True  # Set the flag to True
            return "Veuillez confirmer votre réponse et cliquer sur Valider."




class WaitForNames(WaitPage):
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
            return "Ce prénom a déjà été choisi par un autre participant. Veuillez en sélectionner un nouveau."

    def before_next_page(player, timeout_happened):
        Fnames(player)
        Femalename(player)


class NameSelectionM(Page):
    form_model = 'player'
    form_fields = ['chosen_nameM']

    def is_displayed(player):
         return player.chosen_nameM == "" and player.gender==1

        # Show the page if the player hasn't chosen a name yet

    def error_message(self, values):
        chosen_nameM = values['chosen_nameM']
        if chosen_nameM in [p.chosen_nameM for p in self.group.get_players()]:
            return "Ce prénom a déjà été choisi par un autre participant. Veuillez en sélectionner un nouveau."

    def before_next_page(player, timeout_happened):
        Mnames(player)
        Malename(player)



class FemaleNames(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.gender== 0

    form_model = 'player'
    form_fields = ['FemaleNames']

    def before_next_page(player, timeout_happened):
        Femalename(player)

class MaleNames(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.gender== 1

    form_model = 'player'
    form_fields = ['MaleNames']

    def before_next_page(player, timeout_happened):
        Malename(player)

class MyWaitPage(WaitPage):
    pass













page_sequence = [Survey,WaitForNames, NameSelectionF, NameSelectionM, MyWaitPage]

#page_sequence = [ Survey,WaitForNames, NameSelectionF, NameSelectionM, MyWaitPage]