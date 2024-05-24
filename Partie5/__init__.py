from otree.api import *
import os

doc = """
3 rounds played in teams
"""


class C(BaseConstants):
    NAME_IN_URL = 'Partie5'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 30
    CHOICES = ["cvA", "cvB", "cvC", "cvD"]


class Subsession(BaseSubsession):
    groupA_ch_round3 = models.LongStringField()
    groupB_ch_round3 = models.LongStringField()
    groupC_ch_round3 = models.LongStringField()
    groupD_ch_round3 = models.LongStringField()
    team_1_2_3_4_round3 = models.LongStringField()
    team_5_6_7_8_round3 = models.LongStringField()
    Treatment = models.IntegerField()
    team3_1 = models.LongStringField()
    team3_2 = models.LongStringField()
    team3_3 = models.LongStringField()
    team3_4 = models.LongStringField()
    team3_5 = models.LongStringField()
    team3_6 = models.LongStringField()
    team3_7 = models.LongStringField()
    team3_8 = models.LongStringField()


class Group(BaseGroup):
    selected_count = models.IntegerField()
    selected_player = models.IntegerField(default=2)
    all_names = models.IntegerField()
    all_gender = models.IntegerField()
    points5 = models.IntegerField()


class Player(BasePlayer):
    enjoy = models.IntegerField(label="", choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    belief_own = models.IntegerField(label="",choices=[0,1,2,3,4,5,6],widget=widgets.RadioSelectHorizontal)
    belief_partner = models.IntegerField(
        label="",choices=[0,1,2,3,4,5,6],widget=widgets.RadioSelectHorizontal)

    belief_own_part5 = models.IntegerField(label="", choices=[0, 1, 2, 3, 4, 5, 6], widget=widgets.RadioSelectHorizontal)
    belief_partner_part5 = models.IntegerField(
        label="", choices=[0, 1, 2, 3, 4, 5, 6], widget=widgets.RadioSelectHorizontal)

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
    gender = models.IntegerField()
    name_partner = models.IntegerField()
    partner_name = models.IntegerField()
    partner_gender = models.IntegerField()
    count = models.IntegerField(label="Combien il y a-t-il de zéros dans ce tableau ?")
    correct = models.BooleanField(doc="Whether the count is correct.")
    correct_Group = models.BooleanField(doc="Whether the selected count is correct.")
    partner_selected = models.BooleanField(doc="Whether the count is correct.")
    Message = models.IntegerField(verbose_name='', widget=widgets.RadioSelect, initial=0,
                                  choices=[[1, "Pas de pression, ce tableau n'est pas simple ! "],
                                           [2, "Ne t'inquiète pas, cela arrive de faire des erreurs !"],
                                           [3, "Je sais que c'est difficile mais essaye de te concentrer davantage. "],
                                           [4,
                                            "Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage. "]])
    Message_CD = models.IntegerField(verbose_name='', widget=widgets.RadioSelect, initial=0,
                                  choices=[[3, "Je sais que c'est difficile mais essaye de te concentrer davantage. "],
                                           [4,"Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage. "],
                                            [1, "Pas de pression, ce tableau n'est pas simple ! "],
                                            [2, "Ne t'inquiète pas, cela arrive de faire des erreurs !"]])

    points_partie5 = models.IntegerField()
    points_partie5_solo = models.IntegerField()
    points_beliefs3 = models.IntegerField()
    partner_point5=models.IntegerField()
    points_beliefs_last=models.IntegerField()
# FUNCTIONS

# def creating_session(subsession: Subsession):
# subsession.variant = subsession.session.config['variant']

def creating_session(subsession: Subsession):
    subsession.Treatment = subsession.session.config['Treatment']


def cv(player):
    if player.rank1 == "cvA":
        rank1st = 1
    elif player.rank1 == "cvB":
        rank1st = 2
    elif player.rank1 == "cvC":
        rank1st = 3
    elif player.rank1 == "cvD":
        rank1st = 4
    if player.rank2 == "cvA":
        rank2nd = 1
    elif player.rank2 == "cvB":
        rank2nd = 2
    elif player.rank2 == "cvC":
        rank2nd = 3
    elif player.rank2 == "cvD":
        rank2nd = 4
    if player.rank3 == "cvA":
        rank3rd = 1
    elif player.rank3 == "cvB":
        rank3rd = 2
    elif player.rank3 == "cvC":
        rank3rd = 3
    elif player.rank3 == "cvD":
        rank3rd = 4
    if player.rank4 == "cvA":
        rank4th = 1
    elif player.rank4 == "cvB":
        rank4th = 2
    elif player.rank4 == "cvC":
        rank4th = 3
    elif player.rank4 == "cvD":
        rank4th = 4

    player.rank1st = rank1st
    player.rank2nd = rank2nd
    player.rank3rd = rank3rd
    player.rank4th = rank4th


def creating_group_with_choices_round_3(subsession):
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
            Group_A_ch.append((player.id_in_subsession, (groupC[player.rank1st - 1],
                                                    groupC[player.rank2nd - 1],
                                                    groupC[player.rank3rd - 1],
                                                    groupC[player.rank4th - 1])))
        elif player.participant.InGroupB==True:
            Group_B_ch.append((player.id_in_subsession, (groupD[player.rank1st - 1],
                                                    groupD[player.rank2nd - 1],
                                                    groupD[player.rank3rd - 1],
                                                    groupD[player.rank4th -1])))

        elif player.participant.InGroupC==True:
            Group_C_ch.append((player.id_in_subsession, (groupA[player.rank1st - 1],
                                                    groupA[player.rank2nd - 1],
                                                    groupA[player.rank3rd - 1],
                                                    groupA[player.rank4th -1])))

        elif player.participant.InGroupD==True:
            Group_D_ch.append((player.id_in_subsession, (groupB[player.rank1st - 1],
                                                    groupB[player.rank2nd - 1],
                                                    groupB[player.rank3rd - 1],
                                                    groupB[player.rank4th -1])))


    subsession.groupA_ch_round3=str(Group_A_ch)
    subsession.groupB_ch_round3=str(Group_B_ch)
    subsession.session.groupA_ch_round3 = str(Group_A_ch)
    subsession.session.groupB_ch_round3 = str(Group_B_ch)
    subsession.groupC_ch_round3 = str(Group_C_ch)
    subsession.groupD_ch_round3 = str(Group_D_ch)
    subsession.session.groupC_ch_round3 = str(Group_C_ch)
    subsession.session.groupD_ch_round3 = str(Group_D_ch)

import random


def partner_name(group):
    for player in group.get_players():
        # if player.participant.gender == 0:
        # player.participant.name = player.participant.FemaleNames
        # else:
        # player.participant.name = player.participant.MaleNames

        player.gender = player.participant.gender
        player.name = player.participant.name

    all_names = [player.participant.name for player in group.get_players()]
    all_gender = [player.participant.gender for player in group.get_players()]
    all_points = [player.participant.points_partie4_solo for player in group.get_players()]
    all_points_equipe = [player.participant.points_partie4 for player in group.get_players()]

    group.session.all_gender = str(all_gender)
    group.session.all_names = str(all_names)

    for player in group.get_players():
        partner_name = all_names[2 - player.id_in_group]
        partner_gender = all_gender[2 - player.id_in_group]
        partner_point = all_points[2 - player.id_in_group]
        partner_point_equipe = all_points_equipe[2 - player.id_in_group]


        player.participant.partner_name_round3 = partner_name
        player.participant.partner_gender_round3 = partner_gender
        player.participant.partner_point4 = partner_point
        player.participant.partner_point4_equipe = partner_point_equipe

        if player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 1:
            player.participant.name_partner_round3 = 'Gabriel'
        elif player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 2:
            player.participant.name_partner_round3 = 'Léo'
        elif player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 3:
            player.participant.name_partner_round3 = 'Raphaël'
        elif player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 4:
            player.participant.name_partner_round3 = 'Louis'
        elif player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 5:
            player.participant.name_partner_round3 = 'Noah'
        elif player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 6:
            player.participant.name_partner_round3 = 'Jules'
        elif player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 7:
            player.participant.name_partner_round3 = 'Arthur'
        elif player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 8:
            player.participant.name_partner_round3 = 'Adam'
        elif player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 9:
            player.participant.name_partner_round3 = 'Lucas'
        elif player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 10:
            player.participant.name_partner_round3 = 'Sacha'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 1:
            player.participant.name_partner_round3 = 'Jade'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 2:
            player.participant.name_partner_round3 = 'Louise'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 3:
            player.participant.name_partner_round3 = 'Ambre'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 4:
            player.participant.name_partner_round3 = 'Alba'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 5:
            player.participant.name_partner_round3 = 'Emma'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 6:
            player.participant.name_partner_round3 = 'Rose'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 7:
            player.participant.name_partner_round3 = 'Alice'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 8:
            player.participant.name_partner_round3 = 'Romy'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 9:
            player.participant.name_partner_round3 = 'Anna'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 10:
            player.participant.name_partner_round3 = 'Lina'




def set_correct(player):
    correct_answers = [44, 55, 49, 40, 50, 52]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.count == correct:
            correct = True
        else:
            correct = False

    player.correct = correct


def get_points_solo(player:BasePlayer):
    points_partie5 = 0
    correct_answers = [44, 55, 49, 40, 50, 52]
    for p, correct in zip(player.in_all_rounds(), correct_answers):
        # print(p.answer, correct, p.answer == correct)
        points_partie5 = points_partie5 + 1 if p.count == correct else points_partie5
    player.points_partie5_solo = points_partie5

    player.participant.points_partie5_solo = player.points_partie5_solo


import random
def select_group_answer(group):
    selected_player = random.choice(group.get_players())
    selected_player_id = selected_player.id_in_group
    group.selected_player= selected_player_id

    for player in group.get_players():
        if player.id_in_group == group.selected_player:
            player.partner_selected = True
            selected_count=player.count
        else:
            player.partner_selected = False

    group.selected_count=selected_count

def send_message(group):
    for player in group.get_players():
        if player.round_number==1:
            if player.participant.InGroupC==True or player.participant.InGroupD==True:
                all_messages1 = [player.Message for player in group.get_players()]
            elif player.participant.InGroupA == True or player.participant.InGroupB == True:
                all_messages1 = [player.Message_CD for player in group.get_players()]
            partner_message1=all_messages1[2-player.id_in_group]
            player.participant.partner_message13= partner_message1

        elif player.round_number==2:
            if player.participant.InGroupD==True or player.participant.InGroupC==True:
                all_messages2 = [player.Message for player in group.get_players()]
            elif player.participant.InGroupA == True or player.participant.InGroupB == True:
                all_messages2 = [player.Message_CD for player in group.get_players()]
            partner_message2=all_messages2[2-player.id_in_group]
            player.participant.partner_message14= partner_message2

        elif player.round_number==3:
            if player.participant.InGroupD==True or player.participant.InGroupC==True:
                all_messages3 = [player.Message for player in group.get_players()]
            elif player.participant.InGroupA == True or player.participant.InGroupB == True:
                all_messages3 = [player.Message_CD for player in group.get_players()]
            partner_message3=all_messages3[2-player.id_in_group]
            player.participant.partner_message15= partner_message3

        elif player.round_number==4:
            if player.participant.InGroupD==True or player.participant.InGroupC==True:
                all_messages4 = [player.Message for player in group.get_players()]
            elif player.participant.InGroupA == True or player.participant.InGroupB == True:
                all_messages4 = [player.Message_CD for player in group.get_players()]
            partner_message4=all_messages4[2-player.id_in_group]
            player.participant.partner_message16= partner_message4

        elif player.round_number==5:
            if player.participant.InGroupD==True or player.participant.InGroupC==True:
                all_messages5 = [player.Message for player in group.get_players()]
            elif player.participant.InGroupA == True or player.participant.InGroupB == True:
                all_messages5 = [player.Message_CD for player in group.get_players()]
            partner_message5=all_messages5[2-player.id_in_group]
            player.participant.partner_message17= partner_message5

        elif player.round_number==6:
            if player.participant.InGroupD == True or player.participant.InGroupC == True:
                all_messages6 = [player.Message for player in group.get_players()]
            elif player.participant.InGroupA == True or player.participant.InGroupB == True:
                all_messages6 = [player.Message_CD for player in group.get_players()]
            partner_message6 = all_messages6[2 - player.id_in_group]
            player.participant.partner_message18 = partner_message6




    for player in group.get_players():
        if player.partner_selected == True and player.round_number ==1:
            if player.participant.partner_message13 == 1:
                player.participant.Message_selected13 = '"Pas de pression, ce tableau n’est pas simple !"'
            elif player.participant.partner_message13 == 2:
                player.participant.Message_selected13 = '"Ne t’inquiète pas, cela arrive de faire des erreurs !"'
            elif player.participant.partner_message13 == 3:
                player.participant.Message_selected13 = '"Je sais que c’est difficile mais essaye de te concentrer davantage."'
            elif player.participant.partner_message13 == 4:
                player.participant.Message_selected13 = '"Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage."'

        elif player.partner_selected == True and player.round_number ==2:
            if player.participant.partner_message14 == 1:
                player.participant.Message_selected14 = '"Pas de pression, ce tableau n’est pas simple !"'
            elif player.participant.partner_message14 == 2:
                player.participant.Message_selected14 = '"Ne t’inquiète pas, cela arrive de faire des erreurs !"'
            elif player.participant.partner_message14 == 3:
                player.participant.Message_selected14 = '"Je sais que c’est difficile mais essaye de te concentrer davantage."'
            elif player.participant.partner_message14 == 4:
                player.participant.Message_selected14 = '"Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage."'

        elif player.partner_selected == True and player.round_number ==3:
            if player.participant.partner_message15 == 1:
                player.participant.Message_selected15 = '"Pas de pression, ce tableau n’est pas simple !"'
            elif player.participant.partner_message15 == 2:
                player.participant.Message_selected15 = '"Ne t’inquiète pas, cela arrive de faire des erreurs !"'
            elif player.participant.partner_message15 == 3:
                player.participant.Message_selected15 = '"Je sais que c’est difficile mais essaye de te concentrer davantage."'
            elif player.participant.partner_message15 == 4:
                player.participant.Message_selected15 = '"Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage."'

        elif player.partner_selected == True and player.round_number ==4:
            if player.participant.partner_message16 == 1:
                player.participant.Message_selected16 = '"Pas de pression, ce tableau n’est pas simple !"'
            elif player.participant.partner_message16 == 2:
                player.participant.Message_selected16 = '"Ne t’inquiète pas, cela arrive de faire des erreurs !"'
            elif player.participant.partner_message16 == 3:
                player.participant.Message_selected16 = '"Je sais que c’est difficile mais essaye de te concentrer davantage."'
            elif player.participant.partner_message16 == 4:
                player.participant.Message_selected16 = '"Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage."'


        elif player.partner_selected == True and player.round_number ==5:
            if player.participant.partner_message17 == 1:
                player.participant.Message_selected17 = '"Pas de pression, ce tableau n’est pas simple !"'
            elif player.participant.partner_message17 == 2:
                player.participant.Message_selected17 = '"Ne t’inquiète pas, cela arrive de faire des erreurs !"'
            elif player.participant.partner_message17 == 3:
                player.participant.Message_selected17 = '"Je sais que c’est difficile mais essaye de te concentrer davantage."'
            elif player.participant.partner_message17 == 4:
                player.participant.Message_selected17 = '"Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage."'


        elif player.partner_selected == True and player.round_number ==6:
            if player.participant.partner_message18 == 1:
                player.participant.Message_selected18 = '"Pas de pression, ce tableau n’est pas simple !"'
            elif player.participant.partner_message18 == 2:
                player.participant.Message_selected18 = '"Ne t’inquiète pas, cela arrive de faire des erreurs !"'
            elif player.participant.partner_message18 == 3:
                player.participant.Message_selected18 = '"Je sais que c’est difficile mais essaye de te concentrer davantage."'
            elif player.participant.partner_message18 == 4:
                player.participant.Message_selected18 = '"Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage."'


def set_correct_group(group):
    correct_answers = [44, 55, 49, 40, 50, 52]
    for group, correct in zip(group.in_all_rounds(), correct_answers):
        if group.selected_count == correct:
            correct_group = True
        else:
            correct_group = False

    for player in group.get_players():
        if correct_group == True:
            correct_Group = True
        else:
            correct_Group = False

        player.correct_Group = correct_Group

def get_points(group):
    points5 = 0
    correct_answers = [44, 55, 49, 40, 50, 52]
    for group, correct in zip(group.in_all_rounds(), correct_answers):
        # print(p.answer, correct, p.answer == correct)
        points5 = points5 + 1 if group.selected_count==correct else points5
    group.points5 = points5

    for player in group.get_players():
        player.points_partie5 = group.points5
        player.participant.points_partie5 = player.points_partie5


def get_points_beliefs(player):
    points_beliefs = 0
    if player.belief_own== player.participant.points_partie4_solo:
        points_beliefs= points_beliefs +1
    else:
        points_beliefs = points_beliefs

    if player.belief_partner==player.participant.partner_point4:
        points_beliefs1 = points_beliefs + 1
    else:
        points_beliefs1 = points_beliefs

    player.points_beliefs3=points_beliefs1
    player.participant.points_beliefs3=player.points_beliefs3

def point_partner(group):

    all_points = [player.participant.points_partie5_solo for player in group.get_players()]

    for player in group.get_players():
        partner_point = all_points[2 - player.id_in_group]
        player.partner_point5=partner_point
        player.participant.partner_point5 = partner_point


def get_points_beliefs_last(player):
    points_beliefs_last = 0
    if player.belief_own_part5== player.participant.points_partie5_solo:
        points_beliefs_last= points_beliefs_last +1
    else:
        points_beliefs_last = points_beliefs_last

    if player.belief_partner_part5==player.participant.partner_point5:
        points_beliefs_last1 = points_beliefs_last + 1
    else:
        points_beliefs_last1 = points_beliefs_last

    player.points_beliefs_last=points_beliefs_last1
    player.participant.points_beliefs_last=player.points_beliefs_last
    player.participant.points_beliefs_part5= player.participant.points_beliefs3 +  player.participant.points_beliefs_last





# PAGES

class Instructions(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1



class WaitforChoice(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class ChoiceCV_groupA(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.InGroupA == True and player.round_number == 1

    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3', 'rank4']

    def before_next_page(player, timeout_happened):
        cv(player)
        #creating_m(player)


class ChoiceCV_groupB(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.InGroupB == True and player.round_number == 1

    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3', 'rank4']

    def before_next_page(player, timeout_happened):
        cv(player)
        # partner_name(group)
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
        creating_group_with_choices_round_3(subsession)

    after_all_players_arrive = call_both_functions

    def is_displayed(player):
        return player.round_number == 1



class Matching(WaitPage):

    wait_for_all_groups = True

    def making_team_round_3(subsession):
        Group1 = eval(subsession.session.groupA_ch_round3)
        Group2 = eval(subsession.session.groupB_ch_round3)
        Group_C_ch = eval(subsession.session.groupC_ch_round3)
        Group_D_ch = eval(subsession.session.groupD_ch_round3)
        team_1_2_3_4 = []
        team_5_6_7_8 = []
        group1_chosen = []
        group2_chosen = []

        if subsession.round_number == 1:
            Group1.extend(Group_C_ch)
            Group2.extend(Group_D_ch)

            # Forming teams from Group1
            for player in range(4):
                player_group1 = random.choice([p_1 for p_1 in Group1 if p_1[0] not in group1_chosen])
                player_group1_id = player_group1[0]
                player_group1_choices = player_group1[1]
                group1_chosen.append(player_group1_id)

                # Choosing a player for the team
                chosen_player_id = None
                for player_id in player_group1_choices:
                    if player_id not in group1_chosen:
                        chosen_player_id = player_id
                        break

                if chosen_player_id is not None:
                    team_1_2_3_4.append((player_group1_id, chosen_player_id))
                    group1_chosen.append(chosen_player_id)

            # Forming teams from Group2
            for player in range(4):
                player_group2 = random.choice([p_2 for p_2 in Group2 if p_2[0] not in group2_chosen])
                player_group2_id = player_group2[0]
                player_group2_choices = player_group2[1]
                group2_chosen.append(player_group2_id)

                # Choosing a player for the team
                chosen_player_id = None
                for player_id in player_group2_choices:
                    if player_id not in group2_chosen:
                        chosen_player_id = player_id
                        break

                if chosen_player_id is not None:
                    team_5_6_7_8.append((player_group2_id, chosen_player_id))
                    group2_chosen.append(chosen_player_id)

            new_matrix = team_1_2_3_4 + team_5_6_7_8
            subsession.set_group_matrix(new_matrix)
            subsession.team_1_2_3_4_round3 = str(team_1_2_3_4)
            subsession.team_5_6_7_8_round3 = str(team_5_6_7_8)
            subsession.session.team_1_2_3_4_round3 = str(team_1_2_3_4)
            subsession.session.team_5_6_7_8_round3 = str(team_5_6_7_8)

        else:
            subsession.group_like_round(1)

    after_all_players_arrive = making_team_round_3


class WaitforPartnerName(WaitPage):
    after_all_players_arrive = partner_name

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class NamePartner(Page):
    form_model='player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

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
        return player.round_number == 1

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
        get_points_solo(player)


class WaitforFeedback(WaitPage):
    body_text = "En attente de votre partenaire."

    @staticmethod
    def call_functions(group):
        # partner_name(group)
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
        return player.correct_Group == False and player.partner_selected == True and player.subsession.Treatment != 1

    # @staticmethod
    # def is_displayed(player: Player):
    # return player.partner_selected == True


class FeedbackNegControl(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.subsession.Treatment == 1


class FeedbackNeg2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected != True and player.subsession.Treatment == 2


class Message(Page):
    form_model = 'player'
    form_fields = ['Message']

    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected != True and player.subsession.Treatment == 3 and player.participant.InGroupA==True or player.correct_Group == False and player.partner_selected != True and player.subsession.Treatment == 3 and player.participant.InGroupB== True



class Message_CD(Page):
    form_model = 'player'
    form_fields = ['Message_CD']

    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected != True and player.subsession.Treatment == 3 and player.participant.InGroupC== True or player.correct_Group == False and player.partner_selected != True and player.subsession.Treatment == 3 and player.participant.InGroupD== True

class WaitforCommunicationReceived(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.subsession.Treatment==3 and player.partner_selected==True

    after_all_players_arrive = send_message
    body_text = "En attente de votre partenaire."

class WaitforCommunication(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.subsession.Treatment==3 and player.partner_selected==False

    body_text = "En attente de votre partenaire."


class MessageSent(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected != True and player.subsession.Treatment == 3


class MessageReceived(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected == True and player.subsession.Treatment == 3


class WaitforNextTable(WaitPage):
    body_text = "En attente de votre partenaire."

class WaitforBeliefsLast(WaitPage):
    body_text = "En attente de votre partenaire."

    after_all_players_arrive = point_partner
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 6


class Belief_last_Instructions(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 6

class Belief_last(Page):
    form_model = 'player'
    form_fields = ['belief_own_part5', 'belief_partner_part5']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 6

    def before_next_page(player, timeout_happened):
        get_points_beliefs_last(player)

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


page_sequence = [Instructions,WaitforChoice, ChoiceCV_groupA, ChoiceCV_groupB, ChoiceCV_groupC, ChoiceCV_groupD,  WaitForMatching,Matching, WaitforPartnerName,  NamePartner,WaitforBelief, Belief, WaitforTable1, Count, WaitforFeedback, FeedbackPositive, FeedbackNegControl, FeedbackNegative, FeedbackNeg2, Message, Message_CD, WaitforCommunicationReceived, WaitforCommunication, MessageSent, MessageReceived,  WaitforNextTable, WaitforBeliefsLast,Belief_last_Instructions,Belief_last, Enjoy, WaitforSurvey]

#page_sequence = [ WaitForMatching, WaitforPartnerName, Belief,WaitforTable1, Count,WaitforFeedback]

