from PIL import Image, ImageDraw, ImageFont
import os
from otree.api import *
import numpy as np



doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'IndPlay'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 4
    TIME_PER_PROBLEM = 30
    CHOICES = ["cvA", "cvB", "cvC", "cvD"]
   # MEN_NAMES = [(1, 'James'), (2, 'David'), (3, 'John'), (4, 'Robert')]
    #WOMEN_NAMES =[(1, 'Mary'), (2, 'Emma'), (3, 'Patricia'), (4, 'Elizabeth')]



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
    groupA_ch = models.LongStringField()
    groupB_ch =models.LongStringField()



class Player(BasePlayer):
    gender = models.IntegerField(label="What gender do you identify with?", widget=widgets.RadioSelectHorizontal,
                                     choices=[[0, "Female"], [1, "Male"]], initial=1)
    BornPA = models.IntegerField(label="Were you born in Pennsylvania?", widget=widgets.RadioSelectHorizontal,
                                     choices=[[1, "Yes"], [0, "No"]], initial=1)
    Job = models.IntegerField(label="Do you have a part-time job?", widget=widgets.RadioSelectHorizontal,
                                  choices=[[1, "Yes"], [0, "No"]], initial=1)
    College = models.IntegerField(label="Which year of college are you in?", widget=widgets.RadioSelectHorizontal,
                                      choices=[[0, "<=2"], [1, ">2"]], initial=1)
    FemaleNames = models.IntegerField(label="Please select one name.", widget=widgets.RadioSelect,
                                 choices=[[1, "Mary"], [2, "Emma"],[3, "Patricia"],[4, "Elizabeth"]], initial=1 )
    MaleNames = models.IntegerField(label="Please select one name.", widget=widgets.RadioSelect,
                                      choices=[[1, "James"], [2, "David"], [3, "John"], [4, "Robert"]], initial=1)

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

    InGroupA= models.BooleanField(default=False,)
    InGroupB=models.BooleanField(default=False,)
    vec_couple = models.LongStringField()
    vec_cv = models.LongStringField()
    vec_matching = models.LongStringField()
    count_ind = models.IntegerField(label="How many 0s are in the table?")
    correct_ind = models.BooleanField(doc="Whether the first sum provided is correct.")





 #FUNCTIONS

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
        rank4th=4
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


def creating_couple_id_gender(player):
    vec_couple = []
    vec_couple.extend((player.id_in_subsession, player.gender))
    player.vec_couple = str(vec_couple)
    player.participant.vec_couple = player.vec_couple

def live_update_choices(self):
    # Get a list of options that have been chosen by other players
    chosen_options = [
        p.FemaleNames for p in self.subsession.get_players() if p != self and p.gender == 0 and p.FemaleNames is not None
    ]

    # Create a list of available options by removing chosen options
    available_options = [
        [1, "Mary"], [2, "Emma"], [3, "Patricia"], [4, "Elizabeth"]
    ]

    # Remove chosen options from available options
    for chosen_option in chosen_options:
        if chosen_option in available_options:
            available_options.remove(chosen_option)

    # Send the updated list of available options to the player's page
    self.group.broadcast({
        'available_options': available_options
    })




def creating_CV_ind(player):
    vec_cv = []
    vec_cv.extend((player.gender, player.College, player.BornPA, player.Job))
    player.vec_cv = str(vec_cv)
    player.participant.vec_cv = player.vec_cv

    # if player.gender==0:
    # vec_cv.extend((player.FemaleNames, player.College, player.BornPA, player.Job))
    # elif player.gender==1:
    # vec_cv.extend(( player.MaleNames, player.College, player.BornPA, player.Job))

def creating_vec_matching(player):
    vec_matching = []
    vec_matching.extend((player.id_in_subsession, player.rank1st, player.rank2nd, player.rank3rd, player.rank4th))
    player.vec_matching = str(vec_matching)
    player.participant.vec_matching = player.vec_matching

def creatingGroups(group):
    Group_A = []
    Group_B = []
    cvA = []
    cvB = []
    sum_hA = 0
    sum_fA = 0
    sum_hB = 0
    sum_fB = 0


    for player in group.get_players():
        if player.gender == 1:
            if sum_hA < 2:
                Group_A.append(player.id_in_subsession)
                cvA.append(player.participant.vec_cv)
                player.InGroupA = True # only the id is useful in group_A
                player.participant.InGroupA=True
                sum_hA += 1
            else:
                player.InGroupA= False
                player.participant.InGroupA=False
        else:
            if sum_fA < 2:
                Group_A.append(player.id_in_subsession)
                cvA.append(player.participant.vec_cv)
                player.InGroupA=True
                player.participant.InGroupA= True
                sum_fA += 1
            else:
                player.InGroupA=False
                player.participant.InGroupA=False
    #participant=player.participant
    #participant.InGroupA=player.InGroupA
    #player.participant.InGroupA = player.InGroupA
    group.Group_A = str(Group_A)
    session=group.session
    session.Group_A=group.Group_A
    #group.session.Group_A = str(Group_A)
    group.cvA=str(cvA)
    #session.cvA=group.cvA
    group.session.cvA=str(cvA)



    for player in group.get_players():
        if  player.InGroupA==False:
            if player.gender == 1:
                if sum_hB < 2:
                    Group_B.append(player.id_in_subsession)  # only the id is usefull in group_A
                    cvB.append(player.participant.vec_cv)
                    player.InGroupB=True
                    player.participant.InGroupB=True
                    sum_hB += 1
                else:
                    player.InGroupB=False
                    player.participant.InGroupB=False
            else:
                if sum_fB < 2:
                    Group_B.append(player.id_in_subsession)
                    cvB.append(player.participant.vec_cv)
                    player.InGroupB=True
                    player.participant.InGroupB=True
                    sum_fB += 1
                else:
                    player.InGroupB=False
                    player.participant.InGroupB=False
    #participant = player.participant
    #participant.InGroupB=player.InGroupB
    #player.participant.InGroupB = player.InGroupB
    group.Group_B = str(Group_B)
    session.Group_B=group.Group_B
    #group.session.Group_B = str(Group_B)
    group.cvB=str(cvB)
    group.session.cvB=str(cvB)
    group.cv_A_1 = str(cvA[0])
    group.session.cv_A_1 = str(cvA[0])
    group.cv_A_2 = str(cvA[1])
    group.session.cv_A_2 = str(cvA[1])
    group.cv_A_3 = str(cvA[2])
    group.session.cv_A_3 = str(cvA[2])
    group.cv_A_4 = str(cvA[3])
    group.session.cv_A_4 = str(cvA[3])
    group.cv_B_1 = str(cvB[0])
    group.session.cv_B_1 = str(cvB[0])
    group.cv_B_2 = str(cvB[1])
    group.session.cv_B_2 = str(cvB[1])
    group.cv_B_3 = str(cvB[2])
    group.session.cv_B_3 = str(cvB[2])
    group.cv_B_4 = str(cvB[3])
    group.session.cv_B_4 = str(cvB[3])
    #player.participant.InGroupA=player.InGroupA
    #player.participant.InGroupB = player.InGroupB
    #participant = player.participant
    #participant.InGroupA=player.InGroupA
    #participant.InGroupB=player.InGroupB


def create_image_cv(cv_1, cv_2, cv_3, cv_4):
    # Création de l'image vide
        image = Image.new("RGB", (800, 600), "white")
        draw = ImageDraw.Draw(image)

        # Définition des coordonnées pour les encadrés et les cadres
        frame_padding = 20
        frame_width = image.width // 2 - frame_padding * 2
        frame_height = image.height // 2 - frame_padding * 2

        top_left_frame = (frame_padding, frame_padding)
        top_right_frame = (image.width // 2 + frame_padding, frame_padding)
        bottom_left_frame = (frame_padding, image.height // 2 + frame_padding)
        bottom_right_frame = (image.width // 2 + frame_padding, image.height // 2 + frame_padding)

        top_left = (top_left_frame[0] + 10, top_left_frame[1] + 10)
        top_right = (top_right_frame[0] + 10, top_right_frame[1] + 10)
        bottom_left = (bottom_left_frame[0] + 10, bottom_left_frame[1] + 10)
        bottom_right = (bottom_right_frame[0] + 10, bottom_right_frame[1] + 10)

        # Définition des questions et réponses pour chaque CV
        questions = ["Gender:", "Year in college:", "Born in PA:", "Job:"]
        answers = [
            ["Female", "Male"],
            ["<=2", ">=2"],
            ["No", "Yes"],
            ["No", "Yes"]

        ]

        # Chargement de la police
        font = ImageFont.truetype("arial.ttf", 18)  # Remplacez "arial.ttf" par le chemin vers votre police
        font_gras = ImageFont.truetype("arialbd.ttf", 18)

        # Dessin des cadres autour de chaque CV
        draw.rectangle([top_left_frame, (top_left_frame[0] + frame_width, top_left_frame[1] + frame_height)],
                        outline="black", width=2)
        draw.rectangle([top_right_frame, (top_right_frame[0] + frame_width, top_right_frame[1] + frame_height)],
                        outline="black", width=2)
        draw.rectangle([bottom_left_frame, (bottom_left_frame[0] + frame_width, bottom_left_frame[1] + frame_height)],
                        outline="black", width=2)
        draw.rectangle(
            [bottom_right_frame, (bottom_right_frame[0] + frame_width, bottom_right_frame[1] + frame_height)],
            outline="black", width=2)

    # Affichage du premier CV en haut à gauche
        draw.text((top_left[0], top_left[1]), "Player A", fill="black", font=font_gras)
        for i, question in enumerate(questions):
            answer = answers[i][cv_1[i]]
            draw.text((top_left[0], top_left[1] + 30 * (i + 1)), question, fill="black", font=font_gras)
            draw.text((top_left[0] + 225, top_left[1] + 30 * (i + 1)), answer, fill="black", font=font)

    # Affichage du deuxième CV en haut à droite
        draw.text((top_right[0], top_right[1]), " Player B", fill="black", font=font_gras)
        for i, question in enumerate(questions):
            answer = answers[i][cv_2[i]]
            draw.text((top_right[0], top_right[1] + 30 * (i + 1)), question, fill="black", font=font_gras)
            draw.text((top_right[0] + 225, top_right[1] + 30 * (i + 1)), answer, fill="black", font=font)

        # Affichage du troisième CV en bas à gauche
        draw.text((bottom_left[0], bottom_left[1]), "Player C", fill="black", font=font_gras)
        for i, question in enumerate(questions):
            answer = answers[i][cv_3[i]]
            draw.text((bottom_left[0], bottom_left[1] + 30 * (i + 1)), question, fill="black", font=font_gras)
            draw.text((bottom_left[0] + 225, bottom_left[1] + 30 * (i + 1)), answer, fill="black", font=font)

    # Affichage du quatrième CV en bas à
        draw.text((bottom_right[0], bottom_right[1]), "Player D", fill="black", font=font_gras)
        for i, question in enumerate(questions):
            answer = answers[i][cv_4[i]]
            draw.text((bottom_right[0], bottom_right[1] + 30 * (i + 1)), question, fill="black", font=font_gras)
            draw.text((bottom_right[0] + 225, bottom_right[1] + 30 * (i + 1)), answer, fill="black", font=font)

        return image





import otree.settings

def image_cv(group):

    cvA1=eval(group.session.cv_A_1)
    cvA2=eval(group.session.cv_A_2)
    cvA3 = eval(group.session.cv_A_3)
    cvA4 = eval(group.session.cv_A_4)
    cvB1 = eval(group.session.cv_B_1)
    cvB2 = eval(group.session.cv_B_2)
    cvB3 = eval(group.session.cv_B_3)
    cvB4 = eval(group.session.cv_B_4)

    image_A = create_image_cv(cvA1, cvA2, cvA3, cvA4)
    image_B = create_image_cv(cvB1, cvB2, cvB3, cvB4)

    #static_path = os.path.join(group.subsession.session.path, 'static')
    #image_A_path = os.path.join(static_path, f'image_A.png')
    #static_path = os.path.join(group.subsession.session.path, 'static')
    #image_B_path = os.path.join(static_path, f'_image_B.png')

    static_path = otree.settings.STATIC_ROOT
    image_A_path = os.path.join(static_path, 'image_A.png')
    image_B_path = os.path.join(static_path, 'image_B.png')

    image_A.save(image_A_path)
    image_B.save(image_B_path)


def creating_group_with_choices_round_1(group):
    Group_A_ch= []
    Group_B_ch = []
    groupA=eval(group.session.Group_A)
    groupB=eval(group.session.Group_B)

    for player in group.get_players():
        if player.InGroupA==True:
            Group_A_ch.append((player.id_in_subsession, (groupB[player.rank1st - 1],
                                                    groupB[player.rank2nd - 1],
                                                    groupB[player.rank3rd - 1],
                                                    groupB[player.rank4th - 1])))
        elif player.InGroupB==True:
            Group_B_ch.append((player.id_in_subsession, (groupA[player.rank1st - 1],
                                                    groupA[player.rank2nd - 1],
                                                    groupA[player.rank3rd - 1],
                                                    groupA[player.rank4th -1])))
    group.groupA_ch=str(Group_A_ch)
    group.groupB_ch=str(Group_B_ch)
    group.session.groupA_ch = str(Group_A_ch)
    group.session.groupB_ch = str(Group_B_ch)

def making_team_round_1(group):
    Group_A_ch=eval(group.session.groupA_ch)
    Group_B_ch=eval(group.session.groupB_ch)

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

    for player in group.get_players:
        player_A = random.choice(Group_A_ch)
        player_A_id=player_A[0]
        choices_B = player_A[1]  # Classement des choix du joueur A dans le groupe B

        # Recherche du choix préféré non encore pris
        for player_B_id in choices_B:
            if player_B_id not in team_1_2_3_4:
                team_1_2_3_4.append(player_A_id, player_B_id)
                break
    team1_1.append(team_1_2_3_4[0],team_1_2_3_4[1])
    team1_2.append(team_1_2_3_4[2], team_1_2_3_4[3])
    team1_3.append(team_1_2_3_4[4], team_1_2_3_4[5])
    team1_4.append(team_1_2_3_4[6], team_1_2_3_4[7])

    new_matrix=[team1_1, team1_2, team1_3, team1_4]
    subsession.set_group_matrix(new_matrix)


import numpy as np
from PIL import Image
import otree.settings
import matplotlib.pyplot as plt



def creating_m(player):
    session = player.session
    subsession = player.subsession
    np.random.seed(0)

    # Define the dimensions of the table
    rows, columns = 10, 10

    # Initialize a dictionary to store the counts of 0s for each table
    zeros_counts = {}

    # Generate and save 4 tables as images
    for i in range(4):
        # Generate a table of random 0s and 1s
        table = np.random.randint(2, size=(rows, columns))

        # Count the number of 0s in the table
        num_zeros = np.sum(table == 0)

        # Store the count in the dictionary with a unique key
        zeros_counts[f'table_{i + 1}'] = num_zeros

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
        image_filename = f'tableInd_{i + 1}.png'
        static_path = otree.settings.STATIC_ROOT
        image_path = os.path.join(static_path, image_filename)
        plt.savefig(image_path, bbox_inches='tight')
        plt.close(fig)

    # Store the dictionary of zero counts in the session vars

    session.vars['zeros_counts'] = zeros_counts
    session.zeros_counts=zeros_counts



def set_correct(player):
    correct_answers = [51, 46, 54, 51]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.count_ind == correct:
            correct_ind = True
        else:
            correct_ind = False

    player.correct_ind = correct_ind



# PAGES

class Instructions(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class WaitforStart(WaitPage):
    pass
class Count(Page):
    timeout_seconds = C.TIME_PER_PROBLEM
    form_model = 'player'
    form_fields = ['count_ind']
    timer_text = 'Time left to count this table:'

    def before_next_page(player, timeout_happened):
        set_correct(player)



class WaitForCollective(WaitPage):
    body_text = "Please wait for the other participants to finish"











page_sequence = [Instructions, WaitforStart, Count, WaitForCollective]
#page_sequence = [ Count, WaitForCollective]