from otree.api import *
import os

doc = """
3 rounds played in teams
"""


class C(BaseConstants):
    NAME_IN_URL = 'Partie4'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 10
    CHOICES = ["cvA", "cvB", "cvC", "cvD"]


class Subsession(BaseSubsession):
    groupA_ch_round2 = models.LongStringField()
    groupB_ch_round2 = models.LongStringField()
    groupC_ch_round2 = models.LongStringField()
    groupD_ch_round2 = models.LongStringField()
    team_1_2_3_4_round2 = models.LongStringField()
    team_5_6_7_8_round2 = models.LongStringField()
    Treatment = models.IntegerField()
    team2_1 = models.LongStringField()
    team2_2 = models.LongStringField()
    team2_3 = models.LongStringField()
    team2_4 = models.LongStringField()
    team2_5 = models.LongStringField()
    team2_6 = models.LongStringField()
    team2_7 = models.LongStringField()
    team2_8 = models.LongStringField()


class Group(BaseGroup):
    selected_count = models.IntegerField()
    selected_player = models.IntegerField(default=2)
    all_names = models.IntegerField()
    all_gender = models.IntegerField()
    points4 = models.IntegerField()

class Player(BasePlayer):
    enjoy = models.IntegerField(label="", choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal, initial=3 )
    belief_own = models.IntegerField(label="",choices=[0,1,2,3,4,5,6],widget=widgets.RadioSelectHorizontal,initial=3)
    belief_partner = models.IntegerField(
        label="",choices=[0,1,2,3,4,5,6],widget=widgets.RadioSelectHorizontal, initial=3)
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
    count = models.IntegerField(label="Combien de zéros il y a-t-il dans ce tableau ?")
    correct = models.BooleanField(doc="Whether the count is correct.")
    correct_Group = models.BooleanField(doc="Whether the selected count is correct.")
    partner_selected = models.BooleanField(doc="Whether the count is correct.")
    Message = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                  choices=[[1, "Pas de pression, ce tableau n'est pas simple ! "],
                                           [2, "Ne t'inquiète pas, cela arrive de faire des erreurs !"],
                                           [3, "Je sais que c'est difficile mais essaye de te concentrer davantage. "],
                                           [4,
                                            "Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage. "]])

    points_partie4 = models.IntegerField()
    points_beliefs2 = models.IntegerField()
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


def creating_group_with_choices_round_2(subsession):
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
            Group_A_ch.append((player.id_in_subsession, (groupD[player.rank1st - 1],
                                                    groupD[player.rank2nd - 1],
                                                    groupD[player.rank3rd - 1],
                                                    groupD[player.rank4th - 1])))
        elif player.participant.InGroupB==True:
            Group_B_ch.append((player.id_in_subsession, (groupC[player.rank1st - 1],
                                                    groupC[player.rank2nd - 1],
                                                    groupC[player.rank3rd - 1],
                                                    groupC[player.rank4th -1])))

        elif player.participant.InGroupC==True:
            Group_C_ch.append((player.id_in_subsession, (groupB[player.rank1st - 1],
                                                    groupB[player.rank2nd - 1],
                                                    groupB[player.rank3rd - 1],
                                                    groupB[player.rank4th -1])))

        elif player.participant.InGroupD==True:
            Group_D_ch.append((player.id_in_subsession, (groupA[player.rank1st - 1],
                                                    groupA[player.rank2nd - 1],
                                                    groupA[player.rank3rd - 1],
                                                    groupA[player.rank4th -1])))


    subsession.groupA_ch_round2=str(Group_A_ch)
    subsession.groupB_ch_round2=str(Group_B_ch)
    subsession.session.groupA_ch_round2 = str(Group_A_ch)
    subsession.session.groupB_ch_round2 = str(Group_B_ch)
    subsession.groupC_ch_round2 = str(Group_C_ch)
    subsession.groupD_ch_round2 = str(Group_D_ch)
    subsession.session.groupC_ch_round2 = str(Group_C_ch)
    subsession.session.groupD_ch_round2 = str(Group_D_ch)

import random
def making_team_round_2(subsession):
    Group_D_ch=eval(subsession.session.groupD_ch_round2)
    Group_B_ch = eval(subsession.session.groupB_ch_round2)
    team_1_2_3_4=[]
    team_5_6_7_8 = []
    player_D_chosen= []
    player_B_chosen = []


    if subsession.round_number == 1:

        for i in range (4):
            player_D = random.choice([p_d for p_d in Group_D_ch if p_d not in player_D_chosen ])
            player_D_chosen.append(player_D)
            player_D_id = player_D[0]
            choices_A = player_D[1]  # Classement des choix du joueur A dans le groupe B

        # Recherche du choix préféré non encore pris
            for player_A_id in choices_A:
                if player_A_id not in (p_a_id for (p_d_id, p_a_id) in team_1_2_3_4):
                    team_1_2_3_4.append((player_D_id, player_A_id))
                    break

        team2_1 = team_1_2_3_4[0]
        team2_2 = team_1_2_3_4[1]
        team2_3 = team_1_2_3_4[2]
        team2_4 = team_1_2_3_4[3]
        subsession.session.team2_1 = str(team2_1)
        subsession.session.team2_2 = str(team2_2)
        subsession.session.team2_3 = str(team2_3)
        subsession.session.team2_4 = str(team2_4)


        for i in range(4):
            player_B = random.choice([p_b for p_b in Group_B_ch if p_b not in player_B_chosen])
            player_B_chosen.append(player_B)
            player_B_id = player_B[0]
            choices_C = player_B[1]  # Classement des choix du joueur A dans le groupe B

                # Recherche du choix préféré non encore pris
            for player_C_id in choices_C:
                if player_C_id not in (p_c_id for (p_b_id, p_c_id) in team_5_6_7_8):
                    team_5_6_7_8.append((player_B_id, player_C_id))
                    break


        team2_5 = team_5_6_7_8[0]
        team2_6 = team_5_6_7_8[1]
        team2_7 = team_5_6_7_8[2]
        team2_8 = team_5_6_7_8[3]
        subsession.session.team2_5 = str(team2_5)
        subsession.session.team2_6 = str(team2_6)
        subsession.session.team2_7 = str(team2_7)
        subsession.session.team2_8 = str(team2_8)

        new_matrix=[team2_1, team2_2, team2_3, team2_4, team2_5, team2_6, team2_7, team2_8]
        subsession.set_group_matrix(new_matrix)
        subsession.team_1_2_3_4_round2 = str(team_1_2_3_4)
        subsession.team_5_6_7_8_round2 = str(team_5_6_7_8)
        subsession.session.team_1_2_3_4_round2 = str(subsession.team_1_2_3_4_round2)
        subsession.session.team_5_6_7_8_round2 = str(subsession.team_5_6_7_8_round2)

    else:
        subsession.group_like_round(1)



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
    all_points = [player.participant.points_partie3 for player in group.get_players()]

    group.session.all_gender = str(all_gender)
    group.session.all_names = str(all_names)

    for player in group.get_players():
        partner_name = all_names[2 - player.id_in_group]
        partner_gender = all_gender[2 - player.id_in_group]
        partner_point = all_points[2 - player.id_in_group]

        player.participant.partner_name_round2 = partner_name
        player.participant.partner_gender_round2 = partner_gender
        player.participant.partner_point3 = partner_point

        if player.participant.partner_gender_round2 == 1 and player.participant.partner_name_round2 == 1:
            player.participant.name_partner_round2 = 'Gabriel'
        elif player.participant.partner_gender_round2 == 1 and player.participant.partner_name_round2 == 2:
            player.participant.name_partner_round2 = 'Léo'
        elif player.participant.partner_gender_round2 == 1 and player.participant.partner_name_round2 == 3:
            player.participant.name_partner_round2 = 'Raphaël'
        elif player.participant.partner_gender_round2 == 1 and player.participant.partner_name_round2 == 4:
            player.participant.name_partner_round2 = 'Louis'
        elif player.participant.partner_gender_round2 == 0 and player.participant.partner_name_round2 == 5:
            player.participant.name_partner_round2 = 'Noah'
        elif player.participant.partner_gender_round2 == 1 and player.participant.partner_name_round2 == 6:
            player.participant.name_partner_round2 = 'Jules'
        elif player.participant.partner_gender_round2 == 1 and player.participant.partner_name_round2 == 7:
            player.participant.name_partner_round2 = 'Arthur'
        elif player.participant.partner_gender_round2 == 1 and player.participant.partner_name_round2 == 8:
            player.participant.name_partner_round2 = 'Adam'
        elif player.participant.partner_gender_round2 == 1 and player.participant.partner_name_round2 == 9:
            player.participant.name_partner_round2 = 'Lucas'
        elif player.participant.partner_gender_round2 == 1 and player.participant.partner_name_round2 == 10:
            player.participant.name_partner_round2 = 'Sacha'
        elif player.participant.partner_gender_round2 == 0 and player.participant.partner_name_round2 == 1:
            player.participant.name_partner_round2 = 'Jade'
        elif player.participant.partner_gender_round2 == 0 and player.participant.partner_name_round2 == 2:
            player.participant.name_partner_round2 = 'Louise'
        elif player.participant.partner_gender_round2 == 0 and player.participant.partner_name_round2 == 3:
            player.participant.name_partner_round2 = 'Ambre'
        elif player.participant.partner_gender_round2 == 0 and player.participant.partner_name_round2 == 4:
            player.participant.name_partner_round2 = 'Alba'
        elif player.participant.partner_gender_round2 == 0 and player.participant.partner_name_round2 == 5:
            player.participant.name_partner_round2 = 'Emma'
        elif player.participant.partner_gender_round2 == 0 and player.participant.partner_name_round2 == 6:
            player.participant.name_partner_round2 = 'Rose'
        elif player.participant.partner_gender_round2 == 0 and player.participant.partner_name_round2 == 7:
            player.participant.name_partner_round2 = 'Alice'
        elif player.participant.partner_gender_round2 == 0 and player.participant.partner_name_round2 == 8:
            player.participant.name_partner_round2 = 'Romy'
        elif player.participant.partner_gender_round2 == 0 and player.participant.partner_name_round2 == 9:
            player.participant.name_partner_round2 = 'Anna'
        elif player.participant.partner_gender_round2 == 0 and player.participant.partner_name_round2 == 10:
            player.participant.name_partner_round2 = 'Lina'



def set_correct(player):
    correct_answers = [47, 52, 46, 61, 54, 50]
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
    player.participant.Message_round2 = player.Message


def send_message(group):
    for player in group.get_players():
        if player.partner_selected == False:
            if player.participant.Message_round2 == 1:
                player.session.Message_selected_round2 = '"Pas de pression, ce tabeau n’est pas simple !"'
            elif player.participant.Message_round2 == 2:
                player.session.Message_selected_round2 = '"Ne t’inquiète pas, cela arrive de faire des erreurs !"'
            elif player.participant.Message_round2 == 3:
                player.session.Message_selected_round2 = '"Je sais que c’est difficile, mais essaye de te concenter davantage."'
            elif player.participant.Message_round2 == 4:
                player.session.Message_selected_round2 = '"Il est très important de donner la bonne réponse, tu devrais essayer une autre technique de comptage."'


def set_correct_group(group):
    correct_answers = [47, 52, 46, 61, 54, 50]
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
    points4 = 0
    correct_answers = [47, 52, 46, 61, 54, 50]
    for group, correct in zip(group.in_all_rounds(), correct_answers):
        # print(p.answer, correct, p.answer == correct)
        points4 = points4 + 1 if group.selected_count==correct else points4
    group.points4 = points4

    for player in group.get_players():
        player.points_partie4 = group.points4
        player.participant.points_partie4 = player.points_partie4

def get_points_beliefs(player):
    points_beliefs = 0
    if player.belief_own== player.participant.points_partie3:
        points_beliefs= points_beliefs +1
    else:
        points_beliefs = points_beliefs

    if player.belief_partner==player.participant.partner_point3:
        points_beliefs1 = points_beliefs + 1
    else:
        points_beliefs1 = points_beliefs

    player.points_beliefs2=points_beliefs1
    player.participant.points_beliefs2=player.points_beliefs2

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
        return participant.InGroupA == False and player.round_number == 1

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

    #@staticmethod
    #def call_both_functions(subsession):
        #creating_group_with_choices_round_2(subsession)
        #making_team_round_2(subsession)

    #after_all_players_arrive = call_both_functions

    def is_displayed(player):
        return player.round_number == 1

    # after_all_players_arrive= creating_group_with_choices_round_1


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
        return player.correct_Group == False and player.partner_selected != True and player.subsession.Treatment == 3

    def before_next_page(player, timeout_happened):
        message(player)


class WaitforCommunication(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.subsession.Treatment == 3

    after_all_players_arrive = send_message
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




#page_sequence = [ WaitForMatching, WaitforPartnerName, Belief,WaitforTable1, Count,WaitforFeedback]

page_sequence = [Instructions,WaitforChoice, ChoiceCV_groupA, ChoiceCV_groupB, WaitForMatching, WaitforPartnerName,  NamePartner,WaitforBelief, Belief, WaitforTable1, Count, WaitforFeedback, FeedbackPositive, FeedbackNegControl, FeedbackNegative, FeedbackNeg2, Message, WaitforCommunication, MessageSent, MessageReceived,  WaitforNextTable, Enjoy, WaitforSurvey]


