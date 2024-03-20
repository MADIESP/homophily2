from PIL import Image, ImageDraw, ImageFont
import os
from otree.api import *
import numpy as np



doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Partie1_Surbooking'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    Fnames = ["Jade", "Louise", "Ambre", "Alba", "Emma", "Rose", "Alice", "Romy", "Anna", "Lina"]
    Mnames = ["Gabriel", "Léo", "Raphaël", "Louis", "Noah", "Jules", "Arthur", "Adam", "Lucas", "Sacha"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
   pass



class Player(BasePlayer):
    survey_error_displayed = models.BooleanField(initial=False)
    gender = models.IntegerField(label="Quel est votre genre ?", widget=widgets.RadioSelectHorizontal,
                                 choices=[[0, "Femme"], [1, "Homme"]], initial=0)
    BornIDF = models.IntegerField(label="Etes vous né.e en  Ile de France ?", widget=widgets.RadioSelectHorizontal,
                                 choices=[[1, "Oui"], [0, "Non"]], initial=0)
    CommutingTime = models.IntegerField(
        label="Quel est votre temps de trajet quotidien (pour vous rendre à vos activités principales : travail, études, autres engagements,...) ?",
        widget=widgets.RadioSelectHorizontal,
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






 #FUNCTIONS

def Fnames(player):
    if player.chosen_nameF == "Jade":
        FemaleNames = 1
    elif player.chosen_nameF == "Louise":
        FemaleNames = 2
    elif player.chosen_nameF == "Ambre":
        FemaleNames = 3
    elif player.chosen_nameF == "Alba":
        FemaleNames = 4
    elif player.chosen_nameF == "Emma":
        FemaleNames = 5
    elif player.chosen_nameF == "Rose":
        FemaleNames = 6
    elif player.chosen_nameF == "Alice":
        FemaleNames = 7
    elif player.chosen_nameF == "Romy":
        FemaleNames = 8
    elif player.chosen_nameF == "Anna":
        FemaleNames = 9
    elif player.chosen_nameF == "Lina":
        FemaleNames = 10


    player.FemaleNames = FemaleNames


def Mnames(player):
    if player.chosen_nameM == "Gabriel":
        MaleNames = 1
    elif player.chosen_nameM == "Léo":
        MaleNames = 2
    elif player.chosen_nameM == "Raphaël":
        MaleNames = 3
    elif player.chosen_nameM == "Louis":
        MaleNames = 4
    elif player.chosen_nameM == "Noah":
        MaleNames = 5
    elif player.chosen_nameM == "Jules":
        MaleNames = 6
    elif player.chosen_nameM == "Arthur":
        MaleNames = 7
    elif player.chosen_nameM == "Adam":
        MaleNames = 8
    elif player.chosen_nameM == "Lucas":
        MaleNames = 9
    elif player.chosen_nameM == "Sacha":
        MaleNames = 10

    player.MaleNames = MaleNames

def gender(player):
    player.participant.gender = player.gender
    player.participant.BornIDF = player.BornIDF
    player.participant.CommutingTime = player.CommutingTime


def Femalename(player):
    player.participant.FemaleNames = player.FemaleNames
    player.participant.name = player.participant.FemaleNames


def Malename(player):
    player.participant.MaleNames = player.MaleNames
    player.participant.name = player.participant.MaleNames


# PAGES
class Instructions_general(Page):
    form_model = 'player'
class WaitforPartie1(WaitPage):
    pass


class Survey(Page):
    form_model = 'player'
    form_fields = ['gender', 'BornIDF', 'CommutingTime' ]

    def before_next_page(player, timeout_happened):
        gender(player)

    def error_message(player, timeout_happened):
        if not player.survey_error_displayed:
            player.survey_error_displayed = True  # Set the flag to True
            return "Merci de vérifier que vos informations sont exactes et cliquer sur Valider."


class WaitforInstructionPrenom(WaitPage):
    pass

class Prenom(Page):
    form_model = 'player'

    def vars_for_template(player):
        player.gender=player.participant.gender
        player.BornIDF=player.participant.BornIDF
        player.CommutingTime=player.participant.CommutingTime


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

    def js_vars(player):
        return dict(selected=[p.chosen_nameF for p in player.group.get_players()])
        
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

    def js_vars(player):
        return dict(selected=[p.chosen_nameM for p in player.group.get_players()])
        
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







page_sequence = [ Prenom, NameSelectionF, NameSelectionM, MyWaitPage]

#page_sequence = [Instructions, WaitForSurvey, Survey,WaitForNames, NameSelectionF, NameSelectionM, MyWaitPage]

#page_sequence = [ Instructions_general, WaitforPartie1,Survey,WaitforInstructionPrenom, Prenom, NameSelectionF, NameSelectionM, MyWaitPage]

#page_sequence = [Survey, NameSelectionF, NameSelectionM, MyWaitPage]