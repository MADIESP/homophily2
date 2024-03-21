from PIL import Image, ImageDraw, ImageFont
import os
from otree.api import *
import numpy as np



doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Partie0'
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
                                 choices=[[0, "Femme"], [1, "Homme"]])
    BornIDF = models.IntegerField(label="Etes vous né.e en  Ile de France ?", widget=widgets.RadioSelectHorizontal,
                                 choices=[[1, "Oui"], [0, "Non"]])
    CommutingTime = models.IntegerField(
        label="Quel est votre temps de trajet quotidien (pour vous rendre à vos activités principales: travail, études, autres engagements,...) ?",
        widget=widgets.RadioSelectHorizontal,
        choices=[[1, " < 30 minutes"], [0, "> 30 minutes"]])

    Main= models.BooleanField(default=False, )
    Main1 = models.BooleanField(default=False, )
    Surbooking = models.BooleanField(default=False, )






 #FUNCTIONS

def gender(player):
    player.participant.gender = player.gender
    player.participant.BornIDF=player.BornIDF
    player.participant.CommutingTime=player.CommutingTime




def creatingMain(group):
    Group_Main=[]
    sum_h = 0
    sum_f = 0



    for player in group.get_players():
        if player.gender == 1:
            if sum_h < 8:
                player.Main1=True
                Group_Main.append(player.id_in_group)
                sum_h += 1
            else:
                pass
        else:
            if sum_f < 8:
                player.Main1=True
                Group_Main.append(player.id_in_group)
                sum_f += 1
            else:
                pass

    for player in group.get_players():
        if player.gender == 1:
            if player.Main1==False and len(Group_Main)<16:
                player.Main = True
                Group_Main.append(player.id_in_group)
            else:
                pass

        else:
            if player.Main1==False and len(Group_Main)<16:
                player.Main= True
                Group_Main.append(player.id_in_group)
            else:
                pass

    for player in group.get_players():
        if player.Main==True:
            player.participant.Main=True
            player.Surbooking=False
            player.participant.Surbooking=False
        elif player.Main1==True:
            player.participant.Main = True
            player.Surbooking=False
            player.participant.Surbooking=False
        elif player.Main1==False and player.Main== False:
            player.participant.Main= False
            player.Surbooking=True
            player.participant.Surbooking=True

    group.session.Group_Main = str(Group_Main)




# PAGES
class Instructions_general(Page):
    form_model = 'player'
class WaitforPartie1(WaitPage):
    pass

class Survey(Page):
    form_model = 'player'
    form_fields = ['gender', 'BornIDF', 'CommutingTime']

    def before_next_page(player, timeout_happened):
        gender(player)

    #def error_message(player, timeout_happened):
        #if not player.survey_error_displayed:
            #player.survey_error_displayed = True  # Set the flag to True

class WaitforSessionName(WaitPage):
    after_all_players_arrive = creatingMain

class Main(Page):
    def is_displayed(player):
         return player.participant.Main==True

class Surbooking(Page):

    def is_displayed(player):
         return player.Surbooking==True

class WaitforInstructionPrenom(WaitPage):
    pass





#page_sequence = [ Survey, NameSelectionF, NameSelectionM, MyWaitPage]

# page_sequence = [ Instructions_general, WaitforPartie1,Survey, WaitforSessionName,Main, Surbooking , WaitforInstructionPrenom]
page_sequence = [ Instructions_general, WaitforPartie1,Survey, WaitforSessionName]