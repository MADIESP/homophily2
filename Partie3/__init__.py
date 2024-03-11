from otree.api import *
import os


doc = """
3 rounds played in teams
"""


class C(BaseConstants):
    NAME_IN_URL = 'Partie3'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 10
    CHOICES = ["cvA", "cvB", "cvC", "cvD"]



class Subsession(BaseSubsession):
    groupA_ch = models.LongStringField()
    groupB_ch = models.LongStringField()
    groupC_ch = models.LongStringField()
    groupD_ch = models.LongStringField()
    team_1_2_3_4= models.LongStringField()
    team_5_6_7_8 = models.LongStringField()
    Treatment = models.IntegerField()
    team1_1=models.LongStringField()
    team1_2 = models.LongStringField()
    team1_3 = models.LongStringField()
    team1_4 = models.LongStringField()
    team1_5 = models.LongStringField()
    team1_6 = models.LongStringField()
    team1_7 = models.LongStringField()
    team1_8 = models.LongStringField()




class Group(BaseGroup):
    selected_count = models.IntegerField()
    selected_player=models.IntegerField(default=2)
    all_names=models.IntegerField()
    all_gender=models.IntegerField()
    points3 = models.IntegerField()


class Player(BasePlayer):
    enjoy=models.IntegerField(label="", choices=[1,2,3,4,5,6,7],widget=widgets.RadioSelectHorizontal, initial=3)
    test_ranking1 = models.IntegerField(
        label="1- Avez-vous <b> plus de chance </b> d’être apparié au joueur que vous avez classé en première position ou en deuxième position ? ",
        widget=widgets.RadioSelectHorizontal,
        choices=[[0, "1ère position"], [1, "2ème position"]],initial=0)
    test_ranking2 = models.IntegerField(
        label="2- Avez-vous <b> moins de chance </b> d’être apparié au joueur que vous avez classé en troisième position ou en quatrième position ? ",
        widget=widgets.RadioSelectHorizontal,
        choices=[[0, "3ème position"], [1, "4ème position"]], initial=1)
    test_JeuCollectif = models.IntegerField(
        label="3- A chaque période, quelle réponse sera sélectionnée pour être la <b> réponse de l’équipe </b> ? ",
        widget=widgets.RadioSelect,
        choices=[[0, "Ma réponse sera toujours sélectionnée. "],
                 [1, "La réponse de mon partenaire sera toujours sélectionnée. "],
                 [2, "Une de nos réponses sera sélectionnée de manière aléatoire. "]], initial=2)

    belief_own = models.IntegerField(label="", choices=[0,1,2,3,4],widget=widgets.RadioSelectHorizontal,initial=3)
    belief_partner = models.IntegerField(
        label="",choices=[0,1,2,3,4],widget=widgets.RadioSelectHorizontal,initial=3)

    rank1 = models.StringField(
        choices=C.CHOICES,
        label="<b> 1er Rang : </b>"
    )

    rank2 = models.StringField(
        choices=C.CHOICES,
        label="<b> 2ème Rang : </b>"
    )

    rank3 = models.StringField(
        choices=C.CHOICES,
        label="<b> 3ème Rang : </b>"
    )

    rank4 = models.StringField(
        choices=C.CHOICES,
        label="<b> 4ème Rang : </b>"
    )

    rank1st = models.IntegerField()

    rank2nd = models.IntegerField()

    rank3rd = models.IntegerField()

    rank4th = models.IntegerField()
    name = models.IntegerField()
    gender=models.IntegerField()
    name_partner=models.IntegerField()
    partner_name = models.IntegerField()
    partner_gender = models.IntegerField()
    count = models.IntegerField(label="Combien de zéros il y a-t-il dans ce tableau?")
    correct = models.BooleanField(doc="Whether the count is correct.")
    correct_Group = models.BooleanField(doc="Whether the selected count is correct.")
    partner_selected = models.BooleanField()
    Message = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                  choices=[[1, "Pas de pression, ce tableau n'est pas simple ! "],
                                           [2, "Ne t'inquiète pas, cela arrive de faire des erreurs !"],
                                           [3, "Je sais que c'est difficile mais essaye de te concentrer davantage. "],
                                           [4, "Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage. "]])
    points_partie3 = models.IntegerField()
    points_beliefs1= models.IntegerField()
# FUNCTIONS

#def creating_session(subsession: Subsession):
    #subsession.variant = subsession.session.config['variant']

def creating_session(subsession: Subsession):
    subsession.Treatment = subsession.session.config['Treatment']

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
        rank3rd=4
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


def creating_group_with_choices_round_1(subsession):
    Group_A_ch= []
    Group_B_ch = []
    Group_C_ch = []
    Group_D_ch = []
    groupA=eval(subsession.session.Group_A)
    groupB=eval(subsession.session.Group_B)
    groupC=eval(subsession.session.Group_C)
    groupD=eval(subsession.session.Group_D)

    for player in subsession.get_players():
        if player.participant.InGroupA==True:
            Group_A_ch.append((player.id_in_subsession, (groupB[player.rank1st - 1],
                                                    groupB[player.rank2nd - 1],
                                                    groupB[player.rank3rd - 1],
                                                    groupB[player.rank4th - 1])))
        elif player.participant.InGroupB==True:
            Group_B_ch.append((player.id_in_subsession, (groupA[player.rank1st - 1],
                                                    groupA[player.rank2nd - 1],
                                                    groupA[player.rank3rd - 1],
                                                    groupA[player.rank4th -1])))

        elif player.participant.InGroupC==True:
            Group_C_ch.append((player.id_in_subsession, (groupD[player.rank1st - 1],
                                                    groupD[player.rank2nd - 1],
                                                    groupD[player.rank3rd - 1],
                                                    groupD[player.rank4th -1])))

        elif player.participant.InGroupD==True:
            Group_D_ch.append((player.id_in_subsession, (groupC[player.rank1st - 1],
                                                    groupC[player.rank2nd - 1],
                                                    groupC[player.rank3rd - 1],
                                                    groupC[player.rank4th -1])))


    subsession.groupA_ch=str(Group_A_ch)
    subsession.groupB_ch=str(Group_B_ch)
    subsession.session.groupA_ch = str(Group_A_ch)
    subsession.session.groupB_ch = str(Group_B_ch)
    subsession.groupC_ch = str(Group_C_ch)
    subsession.groupD_ch = str(Group_D_ch)
    subsession.session.groupC_ch = str(Group_C_ch)
    subsession.session.groupD_ch = str(Group_D_ch)

import random
def making_team_round_1(subsession):
    Group_A_ch=eval(subsession.session.groupA_ch)
    Group_C_ch = eval(subsession.session.groupC_ch)
    GroupA=eval(subsession.session.Group_A)

    #Group_B_ch=eval(subsession.session.groupB_ch)

    team1_1 = []
    team1_2 = []
    team1_3 = []
    team1_4 = []
    team_1_2_3_4=[]
    team_5_6_7_8 = []
    player_C_chosen= []
    player_A_chosen = []


    if subsession.round_number == 1:

        for i in range (4):
            player_A = random.choice([p_a for p_a in Group_A_ch if p_a not in player_A_chosen ])
            player_A_chosen.append(player_A)
            player_A_id = player_A[0]
            choices_B = player_A[1]  # Classement des choix du joueur A dans le groupe B

        # Recherche du choix préféré non encore pris
            for player_B_id in choices_B:
                if player_B_id not in (p_b_id for (p_a_id, p_b_id) in team_1_2_3_4):
                    team_1_2_3_4.append((player_A_id, player_B_id))
                    break

        team1_1 = team_1_2_3_4[0]
        team1_2 = team_1_2_3_4[1]
        team1_3 = team_1_2_3_4[2]
        team1_4 = team_1_2_3_4[3]
        subsession.session.team1_1 = str(team1_1)
        subsession.session.team1_2 = str(team1_2)
        subsession.session.team1_3 = str(team1_3)
        subsession.session.team1_4 = str(team1_4)


        for i in range(4):
            player_C = random.choice([p_c for p_c in Group_C_ch if p_c not in player_C_chosen])
            player_C_chosen.append(player_C)
            player_C_id = player_C[0]
            choices_D = player_C[1]  # Classement des choix du joueur A dans le groupe B

                # Recherche du choix préféré non encore pris
            for player_D_id in choices_D:
                if player_D_id not in (p_d_id for (p_c_id, p_d_id) in team_5_6_7_8):
                    team_5_6_7_8.append((player_C_id, player_D_id))
                    break


        team1_5 = team_5_6_7_8[0]
        team1_6 = team_5_6_7_8[1]
        team1_7 = team_5_6_7_8[2]
        team1_8 = team_5_6_7_8[3]
        subsession.session.team1_5 = str(team1_5)
        subsession.session.team1_6 = str(team1_6)
        subsession.session.team1_7 = str(team1_7)
        subsession.session.team1_8 = str(team1_8)

        new_matrix=[team1_1, team1_2, team1_3, team1_4, team1_5, team1_6, team1_7, team1_8]
        subsession.set_group_matrix(new_matrix)
        subsession.team_1_2_3_4 = str(team_1_2_3_4)
        subsession.team_5_6_7_8 = str(team_5_6_7_8)
        subsession.session.team_1_2_3_4 = str(subsession.team_1_2_3_4)
        subsession.session.team_5_6_7_8 = str(subsession.team_5_6_7_8)

    else:
        subsession.group_like_round(1)




import numpy as np
from PIL import Image
import otree.settings
import matplotlib.pyplot as plt


def partner_name(group):

    for player in group.get_players():
        #if player.participant.gender == 0:
            #player.participant.name = player.participant.FemaleNames
        #else:
            #player.participant.name = player.participant.MaleNames

        player.gender=player.participant.gender
        player.name=player.participant.name

    all_names = [player.participant.name for player in group.get_players()]
    all_gender = [player.participant.gender for player in group.get_players()]
    all_points= [player.participant.points_partie2 for player in group.get_players()]


    group.session.all_gender=str(all_gender)
    group.session.all_names=str(all_names)



    for player in group.get_players():
        partner_name=all_names[2-player.id_in_group]
        partner_gender = all_gender[2-player.id_in_group]
        partner_point= all_points[2-player.id_in_group]

        player.participant.partner_name= partner_name
        player.participant.partner_gender=partner_gender
        player.participant.partner_point2=partner_point



        if player.participant.partner_gender==1 and player.participant.partner_name==1:
            player.participant.name_partner='Gabriel'
        elif player.participant.partner_gender==1 and player.participant.partner_name==2:
            player.participant.name_partner='Léo'
        elif player.participant.partner_gender==1 and player.participant.partner_name==3:
            player.participant.name_partner='Raphaël'
        elif player.participant.partner_gender==1 and player.participant.partner_name==4:
            player.participant.name_partner='Louis'
        elif player.participant.partner_gender == 1 and player.participant.partner_name == 5:
            player.participant.name_partner = 'Noah'
        elif player.participant.partner_gender == 1 and player.participant.partner_name == 6:
            player.participant.name_partner = 'Jules'
        elif player.participant.partner_gender == 1 and player.participant.partner_name == 7:
            player.participant.name_partner = 'Arthur'
        elif player.participant.partner_gender == 1 and player.participant.partner_name == 8:
            player.participant.name_partner = 'Adam'
        elif player.participant.partner_gender == 1 and player.participant.partner_name == 9:
            player.participant.name_partner = 'Lucas'
        elif player.participant.partner_gender == 1 and player.participant.partner_name == 10:
            player.participant.name_partner = 'Sacha'
        elif player.participant.partner_gender==0 and player.participant.partner_name==1:
            player.participant.name_partner='Jade'
        elif player.participant.partner_gender==0 and player.participant.partner_name==2:
            player.participant.name_partner='Louise'
        elif player.participant.partner_gender==0 and player.participant.partner_name==3:
            player.participant.name_partner='Ambre'
        elif player.participant.partner_gender==0 and player.participant.partner_name==4:
            player.participant.name_partner='Alba'
        elif player.participant.partner_gender == 0 and player.participant.partner_name == 5:
            player.participant.name_partner = 'Emma'
        elif player.participant.partner_gender == 0 and player.participant.partner_name == 6:
            player.participant.name_partner = 'Rose'
        elif player.participant.partner_gender == 0 and player.participant.partner_name == 7:
            player.participant.name_partner = 'Alice'
        elif player.participant.partner_gender == 0 and player.participant.partner_name == 8:
            player.participant.name_partner = 'Romy'
        elif player.participant.partner_gender == 0 and player.participant.partner_name == 9:
            player.participant.name_partner = 'Anna'
        elif player.participant.partner_gender == 0 and player.participant.partner_name == 10:
            player.participant.name_partner = 'Lina'



def set_correct(player):
    correct_answers = [49, 42, 45, 48,49,51]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.count == correct:
            correct = True
        else:
            correct = False

    player.correct = correct


import random
def select_group_answer(group):
    all_counts = [player.count for player in group.get_players()]
    selected_count = random.choice(all_counts)
    group.selected_count= selected_count
    selected_player = random.choice(group.get_players())
    selected_player_id = selected_player.id_in_group
    group.selected_player= selected_player_id

    for player in group.get_players():
        if player.id_in_group == group.selected_player:
            player.partner_selected = True
        else:
            player.partner_selected = False



def message(player):
    player.participant.Message=player.Message

def send_message(group):
    for player in group.get_players():
        if player.partner_selected == False:
            if player.participant.Message == 1:
                player.session.Message_selected = '"Pas de pression, ce tableau n’est pas simple !"'
            elif player.participant.Message == 2:
                player.session.Message_selected = '"Ne t’inquiète pas, cela arrive de faire des erreurs !"'
            elif player.participant.Message == 3:
                player.session.Message_selected = '"Je sais que c’est difficile mais essaye de te concentrer davantage."'
            elif player.participant.Message == 4:
                player.session.Message_selected = '"Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage."'




def set_correct_group(group):
    correct_answers = [49, 42, 45, 48,49,51]
    for group, correct in zip(group.in_all_rounds(), correct_answers):
        if group.selected_count == correct:
            correct_group = True
        else:
            correct_group = False


    for player in group.get_players():
        if correct_group==True:
            correct_Group=True
        else:
            correct_Group=False

        player.correct_Group=correct_Group

def get_points(group):
    points3 = 0
    correct_answers = [49, 42, 45, 48, 49, 51]
    for group, correct in zip(group.in_all_rounds(), correct_answers):
        # print(p.answer, correct, p.answer == correct)
        points3 = points3 + 1 if group.selected_count==correct else points3
    group.points3 = points3

    for player in group.get_players():
        player.points_partie3 = group.points3
        player.participant.points_partie3 = player.points_partie3


def get_points_beliefs(player):
    points_beliefs = 0
    if player.belief_own== player.participant.points_partie2:
        points_beliefs= points_beliefs +1
    else:
        points_beliefs = points_beliefs

    if player.belief_partner==player.participant.partner_point2:
        points_beliefs1 = points_beliefs + 1
    else:
        points_beliefs1 = points_beliefs

    player.points_beliefs1=points_beliefs1
    player.participant.points_beliefs1=player.points_beliefs1

# PAGES

class InstructionsRanking(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    

class WaitforInstructions2(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class InstructionsRanking2(Page):
    
    form_model= 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 

class WaitforInstructions3(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instructions (Page):
    
    form_model='player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number==1 and player.subsession.Treatment !=3


class InstructionsTreatment2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.subsession.Treatment == 3

class WaitforInstructions4(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class InstructionsPos(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class WaitforInstructions5(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class InstructionsNegControl(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.subsession.Treatment == 1

class InstructionsNegTreatment1(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.subsession.Treatment == 2

class InstructionsNegTreatment2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.subsession.Treatment == 3

class WaitPage1(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class TestCompréhension(Page):
    form_model = 'player'
    form_fields = ['test_ranking1','test_ranking2', 'test_JeuCollectif']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Compréhension_Error(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.test_ranking1!=0 or player.round_number ==1 and player.test_ranking2!=1 or player.round_number ==1 and player.test_JeuCollectif!=2



class WaitforChoice(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class ChoiceCV_groupA(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant=player.participant
        return participant.InGroupA== True and player.round_number == 1

    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3', 'rank4']

    def before_next_page(player, timeout_happened):
        cv(player)





class ChoiceCV_groupB(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.InGroupB == True and player.round_number == 1

    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3', 'rank4']

    def before_next_page(player, timeout_happened):
        cv(player)
        #partner_name(group)


class ChoiceCV_groupC(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.InGroupC == True and player.round_number == 1

    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3', 'rank4']

    def before_next_page(player, timeout_happened):
        cv(player)


class ChoiceCV_groupD(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.InGroupD == True and player.round_number == 1

    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3', 'rank4']

    def before_next_page(player, timeout_happened):
        cv(player)


class WaitForMatching(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def call_both_functions(subsession):
        creating_group_with_choices_round_1(subsession)
        making_team_round_1(subsession)



    after_all_players_arrive = call_both_functions

    def is_displayed(player):
        return player.round_number == 1

    #after_all_players_arrive= creating_group_with_choices_round_1

class WaitforPartnerName(WaitPage):
    after_all_players_arrive =partner_name

    @staticmethod
    def is_displayed(player: Player):
        return  player.round_number == 1

class NamePartner(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class TestCompréhensionBeliefs(Page):
    form_model = 'player'
    form_fields = ['test_Belief1','test_Belief2','test_Belief3','test_Belief4']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Compréhension_Belief_Error(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.test_Belief1 != 3 or player.round_number == 1 and player.test_Belief2 != 3 or player.round_number == 1 and player.test_Belief3 != 1 or player.round_number == 1 and player.test_Belief4 != 1






class WaitforBelief(WaitPage):
    wait_for_all_groups = True
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Belief(Page):
    form_model = 'player'
    form_fields = ['belief_own', 'belief_partner']

    @staticmethod
    def is_displayed(player: Player):
        return  player.round_number == 1

    def before_next_page(player, timeout_happened):
        get_points_beliefs(player)

class WaitforTable1(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1




class Count(Page):

    timeout_seconds = C.TIME_PER_PROBLEM
    form_model = 'player'
    form_fields = ['count']
    timer_text = 'Temps restant pour compter ce tableau:'

    def before_next_page(player, timeout_happened):
        set_correct(player)

class WaitforFeedback(WaitPage):
    body_text = "En attente de votre partenaire."

    @staticmethod
    def call_functions(group):
        #partner_name(group)
        select_group_answer(group)
        set_correct_group(group)
        get_points(group)



    after_all_players_arrive = call_functions



class FeedbackPositive(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == True


class FeedbackNegative(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected==True and player.subsession.Treatment != 1

    #@staticmethod
    #def is_displayed(player: Player):
        #return player.partner_selected == True

class FeedbackNegControl(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False  and player.subsession.Treatment == 1

class FeedbackNeg2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False  and player.partner_selected!=True and player.subsession.Treatment == 2

class Message(Page):

    form_model = 'player'
    form_fields = ['Message']

    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected!=True and player.subsession.Treatment==3

    def before_next_page(player, timeout_happened):
        message(player)


class WaitforCommunication(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.subsession.Treatment==3

    after_all_players_arrive = send_message
    body_text = "En attente de votre partenaire."

class MessageSent(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected != True and player.subsession.Treatment==3

class MessageReceived(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected == True and player.subsession.Treatment==3


class WaitforNextTable(WaitPage):
    body_text = "En attente de votre partenaire."

class Point(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 6


class Enjoy(Page):
    form_model = 'player'
    form_fields = ['enjoy']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 6


class WaitforSurvey(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 6


page_sequence = [InstructionsRanking, WaitforInstructions2, InstructionsRanking2, WaitforInstructions3, Instructions, InstructionsTreatment2, WaitforInstructions4, InstructionsPos, WaitforInstructions5, InstructionsNegControl, InstructionsNegTreatment1, InstructionsNegTreatment2, WaitPage1, TestCompréhension, Compréhension_Error,WaitforChoice, ChoiceCV_groupA, ChoiceCV_groupB, ChoiceCV_groupC, ChoiceCV_groupD, WaitForMatching,WaitforPartnerName, NamePartner,WaitforBelief ,Belief, WaitforTable1, Count, WaitforFeedback, FeedbackPositive, FeedbackNegControl, FeedbackNegative, FeedbackNeg2, Message, WaitforCommunication, MessageSent, MessageReceived, WaitforNextTable, Enjoy, WaitforSurvey]

#page_sequence = [ChoiceCV_groupA, ChoiceCV_groupB, WaitForMatching, WaitforPartnerName, Belief,WaitforTable1, Count,WaitforFeedback]

#page_sequence = [ChoiceCV_groupA, ChoiceCV_groupB, WaitForMatching,WaitforPartnerName, WaitforMatching2, Belief, Count,  WaitforNextTable, WaitforSurvey]

