from otree.api import *
import os

doc = """
3 rounds played in teams
"""


class C(BaseConstants):
    NAME_IN_URL = 'Round3'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 4
    CHOICES = ["cvA", "cvB", "cvC", "cvD"]


class Subsession(BaseSubsession):
    groupA_ch = models.LongStringField()
    groupB_ch = models.LongStringField()
    team_1_2_3_4 = models.LongStringField()
    Treatment = models.IntegerField()
    team1_1 = models.LongStringField()
    team1_2 = models.LongStringField()
    team1_3 = models.LongStringField()
    team1_4 = models.LongStringField()
    # variant = models.BooleanField()


class Group(BaseGroup):
    selected_count = models.IntegerField()
    selected_player = models.IntegerField(default=2)
    all_names = models.IntegerField()
    all_gender = models.IntegerField()


class Player(BasePlayer):
    belief_own = models.IntegerField(label="", initial=0)
    belief_partner = models.IntegerField(
        label="", initial=0)

    rank1 = models.StringField(
        choices=C.CHOICES,
        label="<b> Rank 1st: </b>"
    )

    rank2 = models.StringField(
        choices=C.CHOICES,
        label="<b> Rank 2nd: </b>"
    )

    rank3 = models.StringField(
        choices=C.CHOICES,
        label="<b> Rank 3rd: </b>"
    )

    rank4 = models.StringField(
        choices=C.CHOICES,
        label="<b> Rank 4th: </b>"
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
    count = models.IntegerField(label="How many 0s are in the table?")
    correct = models.BooleanField(doc="Whether the count is correct.")
    correct_Group = models.BooleanField(doc="Whether the selected count is correct.")
    partner_selected = models.BooleanField(doc="Whether the count is correct.")
    Message = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                  choices=[[1, "It’s okay, this matrix is tricky."],
                                           [2, "Don't worry, mistakes happen."],
                                           [3, "You need to be more careful with these matrices."],
                                           [4, "It’s crucial to get the exact count; this was off."]])


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


def creating_group_with_choices_round_1(subsession):
    Group_A_ch = []
    Group_B_ch = []
    groupA = eval(subsession.session.Group_A_round3)
    groupB = eval(subsession.session.Group_B_round3)

    for player in subsession.get_players():
        if player.participant.InGroupA == True:
            Group_A_ch.append((player.id_in_subsession, (groupB[player.rank1st - 1],
                                                         groupB[player.rank2nd - 1],
                                                         groupB[player.rank3rd - 1],
                                                         groupB[player.rank4th - 1])))
        elif player.participant.InGroupB == True:
            Group_B_ch.append((player.id_in_subsession, (groupA[player.rank1st - 1],
                                                         groupA[player.rank2nd - 1],
                                                         groupA[player.rank3rd - 1],
                                                         groupA[player.rank4th - 1])))
    subsession.groupA_ch = str(Group_A_ch)
    subsession.groupB_ch = str(Group_B_ch)
    subsession.session.groupA_ch_round3 = str(Group_A_ch)
    subsession.session.groupB_ch_round3 = str(Group_B_ch)


import random


def making_team_round_1(subsession):
    Group_A_ch = eval(subsession.session.groupA_ch_round3)
    GroupA = eval(subsession.session.Group_A_round3)

    # Group_B_ch=eval(subsession.session.groupB_ch)

    team1_1 = []
    team1_2 = []
    team1_3 = []
    team1_4 = []
    team_1_2_3_4 = []
    player_B_chosen = []
    player_A_chosen = []

    if subsession.round_number == 1:

        for i in range(4):
            player_A = random.choice([p_a for p_a in Group_A_ch if p_a not in player_A_chosen])
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
        subsession.session.team1_1_round3 = str(team1_1)
        subsession.session.team1_2_round3 = str(team1_2)
        subsession.session.team1_3_round3 = str(team1_3)
        subsession.session.team1_4_round3 = str(team1_4)

        new_matrix = [team1_1, team1_2, team1_3, team1_4]
        subsession.set_group_matrix(new_matrix)
        #subsession.team_1_2_3_4 = str(team_1_2_3_4)
        subsession.session.team_1_2_3_4_round3 = str(team_1_2_3_4)

    else:
        subsession.group_like_round(1)


import numpy as np
from PIL import Image
import otree.settings
import matplotlib.pyplot as plt



def partner_name(group):
    for player in group.get_players():
        # if player.participant.gender == 0:
        # player.participant.name = player.participant.FemaleNames
        # else:
        # player.participant.name = player.participant.MaleNames

        player.gender = player.participant.gender
        player.name = player.participant.name_round3

    all_names = [player.participant.name_round3 for player in group.get_players()]
    all_gender = [player.participant.gender for player in group.get_players()]

    group.session.all_gender = str(all_gender)
    group.session.all_names = str(all_names)

    for player in group.get_players():
        partner_name = all_names[2 - player.id_in_group]
        partner_gender = all_gender[2 - player.id_in_group]

        player.participant.partner_name_round3 = partner_name
        player.participant.partner_gender_round3 = partner_gender

        if player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 1:
            player.participant.name_partner_round3 = 'Thomas'
        elif player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 2:
            player.participant.name_partner_round3 = 'Christopher'
        elif player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 3:
            player.participant.name_partner_round3 = 'Charles'
        elif player.participant.partner_gender_round3 == 1 and player.participant.partner_name_round3 == 4:
            player.participant.name_partner_round3 = 'Daniel'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 1:
            player.participant.name_partner_round3 = 'Jessica'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 2:
            player.participant.name_partner_round3 = 'Sarah'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 3:
            player.participant.name_partner_round3 = 'Karen'
        elif player.participant.partner_gender_round3 == 0 and player.participant.partner_name_round3 == 4:
            player.participant.name_partner_round3 = 'Lisa'


def creating_m(player):
    session = player.session
    subsession = player.subsession
    np.random.seed(0)

    # Define the dimensions of the table
    rows, columns = 10, 10

    # Initialize a dictionary to store the counts of 0s for each table
    zeros_counts = {}

    # Generate and save 10 tables as images
    for i in range(10):
        # Generate a table of random 0s and 1s
        table = np.random.randint(2, size=(rows, columns))

        # Count the number of 0s in the table
        num_zeros = np.sum(table == 0)

        # Store the count in the dictionary with a unique key
        zeros_counts[f'TABLE{i + 1}'] = num_zeros

        # Create a figure and axis for the table
        fig, ax = plt.subplots()

        # Hide axis labels and ticks
        ax.axis('off')

        # Create a table with 0s and 1s displayed as text, without cell borders
        table_obj = ax.table(cellText=table, loc='center', cellLoc='center', edges='open', bbox=[0, 0, 1, 1])
        for key, cell in table_obj._cells.items():
            cell.set_text_props(fontsize=14)  # Adjust font size as needed
            if key[0] == 0 or key[1] == -1 or key[1] == columns:
                cell.set_facecolor('none')
                cell.set_edgecolor('none')
            else:
                cell.set_facecolor('white')

        # Save the table as an image
        image_filename = f'table_{i + 1}.png'
        static_path = otree.settings.STATIC_ROOT
        image_path = os.path.join(static_path, image_filename)
        plt.savefig(image_path, bbox_inches='tight')
        plt.close(fig)

    # Store the dictionary of zero counts in the session vars

    session.vars['zeros_counts'] = zeros_counts
    session.zeros_counts2 = zeros_counts


def set_correct(player):
    correct_answers = [49, 42, 45, 48, 49, 51]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.count == correct:
            correct = True
        else:
            correct = False

    player.correct = correct


def select_group_answer(group):
    all_counts = [player.count for player in group.get_players()]
    selected_count = random.choice(all_counts)

    # Assign selected_count to the group before using it for player comparisons
    group.selected_count = selected_count

    # Choose a player based on selected_count
    selected_player = random.choice([p for p in group.get_players() if p.count == selected_count])
    selected_player_id = selected_player.id_in_group
    group.selected_player = selected_player_id

    for player in group.get_players():
        if player.id_in_group == group.selected_player:
            player.partner_selected = True
        else:
            player.partner_selected = False


import random

import random


def select_group_answer(group):
    all_counts = [player.count for player in group.get_players()]
    selected_count = random.choice(all_counts)
    group.selected_count = selected_count
    selected_player = random.choice(group.get_players())
    selected_player_id = selected_player.id_in_group
    group.selected_player = selected_player_id

    for player in group.get_players():
        if player.id_in_group == group.selected_player:
            player.partner_selected = True
            if player.participant.gender == 1 and player.participant.name_round3 == 1:
                player.session.name_selected_round3 = 'James'
            elif player.participant.gender == 1 and player.participant.name_round3 == 2:
                player.session.name_selected_round3 = 'David'
            elif player.participant.gender == 1 and player.participant.name_round3 == 3:
                player.session.name_selected_round3 = 'John'
            elif player.participant.gender == 1 and player.participant.name_round3 == 4:
                player.session.name_selected_round3 = 'Robert'
            elif player.participant.gender == 0 and player.participant.name_round3 == 1:
                player.session.name_selected_round3 = 'Mary'
            elif player.participant.gender == 0 and player.participant.name_round3 == 2:
                player.session.name_selected_round3 = 'Emma'
            elif player.participant.gender == 0 and player.participant.name_round3 == 3:
                player.session.name_selected_round3 = 'Patricia'
            elif player.participant.gender == 1 and player.participant.name_round3 == 4:
                player.session.name_selected_round3 = 'Elizabeth'

        else:
            player.partner_selected = False
            if player.participant.gender == 1 and player.participant.name_round3 == 1:
                player.session.name_NOTselected_round3 = 'Liam'
            elif player.participant.gender == 1 and player.participant.name_round3 == 2:
                player.session.name_NOTselected_round3 = 'Noah'
            elif player.participant.gender == 1 and player.participant.name_round3 == 3:
                player.session.name_NOTselected_round3 = 'William'
            elif player.participant.gender == 1 and player.participant.name_round3 == 4:
                player.session.name_NOTselected_round3 = 'Henry'
            elif player.participant.gender == 0 and player.participant.name_round3 == 1:
                player.session.name_NOTselected_round3 = 'Charlotte'
            elif player.participant.gender == 0 and player.participant.name_round3 == 2:
                player.session.name_NOTselected_round3 = 'Olivia'
            elif player.participant.gender == 0 and player.participant.name_round3 == 3:
                player.session.name_NOTselected_round3 = 'Sophia'
            elif player.participant.gender == 1 and player.participant.name_round3 == 4:
                player.session.name_NOTselected_round3 = 'Amelia'


def message(player):
    player.participant.Message_round3 = player.Message


def send_message(group):
    for player in group.get_players():
        if player.partner_selected == False:
            if player.participant.Message_round3 == 1:
                player.session.Message_selected_round3 = '"It’s okay, this matrix is tricky."'
            elif player.participant.Message_round3 == 2:
                player.session.Message_selected_round3 = '"Don’t worry; mistakes happen."'
            elif player.participant.Message_round3 == 3:
                player.session.Message_selected_round3 = '"You need to be more careful with these matrices."'
            elif player.participant.Message_round3 == 4:
                player.session.Message_selected_round3 = '"It’s crucial to get the exact count; this was off."'


def set_correct_group(group):
    correct_answers = [49, 42, 45, 48, 49, 51]
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


# PAGES

class InstructionsRanking(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class WaitforInstructions2(WaitPage):
    wait_for_all_groups = True


class InstructionsRanking2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class WaitforInstructions3(WaitPage):
    wait_for_all_groups = True


class Instructions(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.subsession.Treatment != 3


class InstructionsTreatment2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.subsession.Treatment == 3


class WaitforInstructions4(WaitPage):
    wait_for_all_groups = True


class InstructionsPos(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class WaitforInstructions5(WaitPage):
    wait_for_all_groups = True


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


class WaitforChoice(WaitPage):
    wait_for_all_groups = True


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


class WaitForMatching(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def call_both_functions(subsession):
        creating_group_with_choices_round_1(subsession)
        making_team_round_1(subsession)

    after_all_players_arrive = call_both_functions

    def is_displayed(player):
        return player.round_number == 1

    # after_all_players_arrive= creating_group_with_choices_round_1


class WaitforPartnerName(WaitPage):
    after_all_players_arrive = partner_name

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class WaitforMatching2(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = making_team_round_1

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number != 1


class Belief(Page):
    form_model = 'player'
    form_fields = ['belief_own', 'belief_partner']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Count(Page):
    timeout_seconds = C.TIME_PER_PROBLEM
    form_model = 'player'
    form_fields = ['count']
    timer_text = 'Time left to count this table:'

    def before_next_page(player, timeout_happened):
        set_correct(player)


class WaitforFeedback(WaitPage):
    body_text = "Waiting for your partner."

    @staticmethod
    def call_functions(group):
        # partner_name(group)
        select_group_answer(group)
        set_correct_group(group)

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
    body_text = "Waiting for your partner."


class MessageSent(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected != True and player.subsession.Treatment == 3


class MessageReceived(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected == True and player.subsession.Treatment == 3


class WaitforNextTable(WaitPage):
    body_text = "Waiting for your partner."


class WaitforSurvey(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 6


page_sequence = [ ChoiceCV_groupA, ChoiceCV_groupB, WaitForMatching, WaitforPartnerName, WaitforMatching2, Belief, Count, WaitforFeedback, FeedbackPositive, FeedbackNegControl, FeedbackNegative, FeedbackNeg2, Message, WaitforCommunication, MessageSent, MessageReceived,  WaitforNextTable, WaitforSurvey]

# page_sequence = [ChoiceCV_groupA, ChoiceCV_groupB, WaitForMatching,Count, WaitforNextTable]


