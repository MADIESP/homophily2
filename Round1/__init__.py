from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Matching'
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
        pass

class Player(BasePlayer):
class WaitMatching(WaitPage):
            # wait_for_all_groups = True
            import random
            @staticmethod
            def after_all_players_arrive(subsession):





def creating_group_with_choices_round_1(subsession):
    Group_A_ch=copy(participant.InGroup_A)
    Group_B_ch = copy(participant.InGroup_B)
    Group_C_ch = copy(participant.InGroup_C)
    Group_D_ch = copy(participant.InGroup_D)
    for player in get_players():
        if player.participant.InGroup_A==True:
            for i in range(4):
                if player.id_in_subsession==Group_A[i]:
                    Group_A_ch[i]=(Group_A[i],[Group_B[player.rank1st - 1],Group_B[player.rank2nd - 1],
                                               Group_B[player.rank3rd - 1],Group_B[player.rank4th - 1]])
        elif player.participant.Group_B==True:
                for i in range(4):
                    if player.id_in_subsession==Group_B[i]:
                        Group_B_ch[i]=(Group_B[i],[Group_A[player.rank1st - 1],Group_A[player.rank2nd - 1],
                                               Group_A[player.rank3rd - 1],Group_A[player.rank4th - 1]])
        elif player.participant.Group_C==True:
                for i in range(4):
                    if player.id_in_subsession==Group_C[i]:
                        Group_C_ch[i]=(Group_C[i],[Group_D[player.rank1st - 1],Group_D[player.rank2nd - 1],
                                               Group_D[player.rank3rd - 1],Group_D[player.rank4th - 1]])
        else:
            for i in range(4):
                if player.id_in_subsession==Group_D[i]:
                    Group_D_ch[i]=(Group_D[i],[Group_C[player.rank1st - 1],Group_C[player.rank2nd - 1],
                                               Group_C[player.rank3rd - 1],Group_C[player.rank4th - 1]])


def making_team_round_1(Subsession):
    team1_1 = []
    team1_2 = []
    team1_3 = []
    team1_4 = []
    team1_5 = []
    team1_6 = []
    team1_7 = []
    team1_8 = []
    team_1_2_3_4=[]
    team_5_6_7_8=[]
    #Je suis parti du principe que le vecteur group_A avait changé de forme, il est formé de 4 éléments  de la forme
    # (id,choix) où choix est un vecteur de taille 4 avec dans le premier élément correspondant à l'id_in_subsession du
    # 1er choix du joueur etc
    # Formation des équipes avec les groupes A et B
    for i in range(4):
        player_A = random.choice(group_A_ch)
        player_A_id=player_A[0]
        choices_B = player_A[1]  # Classement des choix du joueur A dans le groupe B

        # Recherche du choix préféré non encore pris
        for player_B_id in choices_B:
            if player_B_id not in team_1_2_3_4:
                team_1_2_3_4.append(player_A_id, player_B_id)
                break
    team1_1=[team_1_2_3_4[0],team_1_2_3_4[1]]
    team1_2 = [team_1_2_3_4[2], team_1_2_3_4[3]]
    team1_3 = [team_1_2_3_4[4], team_1_2_3_4[5]]
    team1_4 = [team_1_2_3_4[6], team_1_2_3_4[7]]

    new_matrix=[team1_1, team1_2, team1_3, team1_4]
    subsession.set_group_matrix(new_matrix)

    class Survey(Page):
        form_model = 'player'
        form_fields = ['strategy', 'gender']

    page_sequence = [WaitCounting, Survey]