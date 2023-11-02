from PIL import Image, ImageDraw, ImageFont
import os
from otree.api import *
import numpy as np



doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'CV'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    Fnames = ["Mary", "Emma", "Patricia", "Elizabeth"]
    Mnames = ["James", "David", "John", "Robert"]


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
    gender = models.IntegerField(label="What gender do you identify with?", widget=widgets.RadioSelectHorizontal,
                                     choices=[[0, "Female"], [1, "Male"]])
    BornPA = models.IntegerField(label="Did you do your undergraduate studies (licence) in Ile de France?", widget=widgets.RadioSelectHorizontal,
                                     choices=[[1, "Yes"], [0, "No"]])
    Job = models.IntegerField(label="Do you have a Student job?", widget=widgets.RadioSelectHorizontal,
                                  choices=[[1, "Yes"], [0, "No"]])
    College = models.IntegerField(label="What is your level of study?", widget=widgets.RadioSelectHorizontal,
                                      choices=[[0, "Licence"], [1, "Master"]])
    FemaleNames = models.IntegerField()
    MaleNames = models.IntegerField()
    chosen_nameF = models.StringField(
        choices=C.Fnames,
        label="Please select a name that will be assigned to you for Part 3 of the experiment:",
        initial="",
    )
    chosen_nameM = models.StringField(
        choices=C.Mnames,
        label="Please select a name that will be assigned to you for Part 3 of the experiment:",
        initial="",
    )

    rank1st = models.IntegerField(
        choices=[[1, ' A'],
                 [2, 'B'],
                 [3, '  C'],
                 [4, ' D'], ],
        # widget=widgets.Select,
        verbose_name='<b>Rank 1st:</b>',
        widget=widgets.RadioSelectHorizontal,

    )

    rank2nd = models.IntegerField(
        choices=[[1, 'A'],
                 [2, 'B'],
                 [3, ' C'],
                 [4, ' D'], ],
        # widget=widgets.Select,
        verbose_name='<b>Rank 2nd: </b>',
        widget=widgets.RadioSelectHorizontal,

    )

    rank3rd = models.IntegerField(
        choices=[[1, ' A'],
                 [2, 'B'],
                 [3, ' C'],
                 [4, ' D'], ],
        # widget=widgets.Select,
        verbose_name='<b>Rank 3rd: </b>',
        widget=widgets.RadioSelectHorizontal,

    )

    rank4th = models.IntegerField( choices=[[1, ' A'],[2, 'B'],[3, ' C'],[4, ' D'], ],
        # widget=widgets.Select,
        verbose_name='<b>Rank 4th: </b>',
        widget=widgets.RadioSelectHorizontal)

    InGroupA= models.BooleanField(default=False,)
    InGroupB=models.BooleanField(default=False,)
    vec_couple = models.LongStringField()
    vec_cv = models.LongStringField()
    name = models.IntegerField()
    partner_name = models.IntegerField()
    partner_gender = models.IntegerField(label="What gender do you identify with?", widget=widgets.RadioSelectHorizontal,
                                     choices=[[0, "Female"], [1, "Male"]])






 #FUNCTIONS

def Fnames(player):
    if player.chosen_nameF == "Mary":
        FemaleNames = 1
    elif player.chosen_nameF == "Emma":
        FemaleNames = 2
    elif player.chosen_nameF == "Patricia":
        FemaleNames = 3
    elif player.chosen_nameF == "Elizabeth":
        FemaleNames = 4

    player.FemaleNames = FemaleNames


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


def creating_couple_id_gender(player):
    vec_couple = []
    vec_couple.extend((player.id_in_group, player.gender))
    player.vec_couple = str(vec_couple)
    player.participant.vec_couple = player.vec_couple


def gender(player):
    player.participant.gender = player.gender
    player.participant.College=player.College
    player.participant.BornPA=player.BornPA
    player.participant.Job=player.Job


def Femalename(player):
    player.participant.FemaleNames = player.FemaleNames
    player.participant.name = player.participant.FemaleNames


def Malename(player):
    player.participant.MaleNames = player.MaleNames
    player.participant.name = player.participant.MaleNames


def creating_CV_ind(player):
    vec_cv = []
    if player.gender == 0:
        vec_cv.extend(
            (player.id_in_group, player.FemaleNames, player.College, player.BornPA, player.Job, player.gender))
    elif player.gender == 1:
        vec_cv.extend((player.id_in_group, player.MaleNames, player.College, player.BornPA, player.Job, player.gender))
    player.vec_cv = str(vec_cv)
    player.participant.vec_cv = player.vec_cv


def creatingGroups(group):
    Group_A = []
    Group_B = []
    cvA = []
    cvB = []
    cv_A=[]
    female= []
    male= []
    femaleB=[]
    maleB=[]
    sum_hA = 0
    sum_fA = 0
    sum_hB = 0
    sum_fB = 0

    for player in group.get_players():
        if player.gender == 1:
            if sum_hA < 2:
                Group_A.append(player.id_in_group)
                cvA.append(player.vec_cv)
                player.InGroupA = True  # only the id is useful in group_A
                player.participant.InGroupA = True
                sum_hA += 1
            else:
                player.InGroupA = False
                player.participant.InGroupA = False
        else:
            if sum_fA < 2:
                Group_A.append(player.id_in_group)
                cvA.append(player.vec_cv)
                player.InGroupA = True
                player.participant.InGroupA = True

                sum_fA += 1
            else:
                player.InGroupA = False
                player.participant.InGroupA = False

    cv_A = [eval(cv) for cv in cvA]
    for cv in cv_A:
        if cv[-1] == 0:
            female.append(cv)
        else:
            male.append(cv)

    #female = [cv for cv in cvA if cv[-1] == 0]
    #male = [cv for cv in cvA if cv[-1] == 1]
    cv_A = [female[0], male[0], female[1], male[1]]
    Group_A[0] = female[0][0]

    Group_A[1] = male[0][0]

    Group_A[2] = female[1][0]

    Group_A[3] = male[1][0]

    group.Group_A = str(Group_A)
    group.session.Group_A = str(Group_A)
    group.cvA = str(cv_A)
    group.session.cvA = str(cv_A)

    for player in group.get_players():
        if player.InGroupA == False:
            if player.gender == 1:
                if sum_hB < 2:
                    Group_B.append(player.id_in_group)  # only the id is usefull in group_A
                    cvB.append(player.vec_cv)
                    player.InGroupB = True
                    player.participant.InGroupB = True
                    sum_hB += 1
                else:
                    player.InGroupB = False
                    player.participant.InGroupB = False
            else:
                if sum_fB < 2:
                    Group_B.append(player.id_in_group)
                    cvB.append(player.vec_cv)
                    player.InGroupB = True
                    player.participant.InGroupB = True
                    sum_fB += 1
                else:
                    player.InGroupB = False
                    player.participant.InGroupB = False

    cv_B = [eval(cv) for cv in cvB]
    for cv in cv_B:
        if cv[-1] == 0:
            femaleB.append(cv)
        else:
            maleB.append(cv)


    cv_B = [maleB[0], femaleB[0], maleB[1], femaleB[1]]
    Group_B[0] = maleB[0][0]

    Group_B[1] = femaleB[0][0]

    Group_B[2] = maleB[1][0]

    Group_B[3] = femaleB[1][0]

    group.Group_B = str(Group_B)
    group.session.Group_B = str(Group_B)
    group.cvB = str(cv_B)
    group.session.cvB = str(cv_B)
    group.cv_A_1 = str(cvA[0])
    group.session.cv_A_1 = str(cv_A[0])
    group.cv_A_2 = str(cvA[1])
    group.session.cv_A_2 = str(cv_A[1])
    group.cv_A_3 = str(cvA[2])
    group.session.cv_A_3 = str(cv_A[2])
    group.cv_A_4 = str(cvA[3])
    group.session.cv_A_4 = str(cv_A[3])
    group.cv_B_1 = str(cvB[0])
    group.session.cv_B_1 = str(cv_B[0])
    group.cv_B_2 = str(cvB[1])
    group.session.cv_B_2 = str(cv_B[1])
    group.cv_B_3 = str(cvB[2])
    group.session.cv_B_3 = str(cv_B[2])
    group.cv_B_4 = str(cvB[3])
    group.session.cv_B_4 = str(cv_B[3])


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
    questions = ["Name:", "Level of Study:", "Licence in Ile De France:", "Student Job:"]
    answers = [
        [["Mary", "James"], ["Emma", "David"], ["Patricia", "John"], ["Elizabeth", "Robert"]],
        ["Licence", "Master"],
        ["No", "Yes"],
        ["No", "Yes"]

    ]

    import otree.settings
    static_path = otree.settings.STATIC_ROOT
    font_path = os.path.join(static_path, 'arial.ttf')
    # Chargement de la police
    font = ImageFont.truetype(font_path, 18)
    # font = ImageFont.truetype("arial.ttf", 18)  # Remplacez "arial.ttf" par le chemin vers votre police
    font_gras = ImageFont.truetype(font_path, 18)

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
        if i == 0:
            answer = answers[0][cv_1[1] - 1][cv_1[-1]]
        else:
            answer = answers[i][cv_1[i+1]]
        draw.text((top_left[0], top_left[1] + 30 * (i + 1)), question, fill="black", font=font_gras)
        draw.text((top_left[0] + 225, top_left[1] + 30 * (i + 1)), answer, fill="black", font=font)

    # Affichage du deuxième CV en haut à droite
    draw.text((top_right[0], top_right[1]), " Player B", fill="black", font=font_gras)
    for i, question in enumerate(questions):
        if i == 0:
            answer = answers[0][cv_2[1] - 1][cv_2[-1]]
        else:
            answer = answers[i][cv_2[i+1]]
        draw.text((top_right[0], top_right[1] + 30 * (i + 1)), question, fill="black", font=font_gras)
        draw.text((top_right[0] + 225, top_right[1] + 30 * (i + 1)), answer, fill="black", font=font)

        # Affichage du troisième CV en bas à gauche
    draw.text((bottom_left[0], bottom_left[1]), "Player C", fill="black", font=font_gras)
    for i, question in enumerate(questions):
        if i == 0:
            answer = answers[0][cv_3[1] - 1][cv_3[-1]]
        else:
            answer = answers[i][cv_3[i+1]]
        draw.text((bottom_left[0], bottom_left[1] + 30 * (i + 1)), question, fill="black", font=font_gras)
        draw.text((bottom_left[0] + 225, bottom_left[1] + 30 * (i + 1)), answer, fill="black", font=font)

    # Affichage du quatrième CV en bas à
    draw.text((bottom_right[0], bottom_right[1]), "Player D", fill="black", font=font_gras)
    for i, question in enumerate(questions):
        if i == 0:
            answer = answers[0][cv_4[1] - 1][cv_4[-1]]
        else:
            answer = answers[i][cv_4[i+1]]
        draw.text((bottom_right[0], bottom_right[1] + 30 * (i + 1)), question, fill="black", font=font_gras)
        draw.text((bottom_right[0] + 225, bottom_right[1] + 30 * (i + 1)), answer, fill="black", font=font)

    return image


import otree.settings


def image_cv(group):
    cvA1 = eval(group.session.cv_A_1)
    cvA2 = eval(group.session.cv_A_2)
    cvA3 = eval(group.session.cv_A_3)
    cvA4 = eval(group.session.cv_A_4)
    cvB1 = eval(group.session.cv_B_1)
    cvB2 = eval(group.session.cv_B_2)
    cvB3 = eval(group.session.cv_B_3)
    cvB4 = eval(group.session.cv_B_4)

    image_A = create_image_cv(cvA1, cvA2, cvA3, cvA4)
    image_B = create_image_cv(cvB1, cvB2, cvB3, cvB4)

    # static_path = os.path.join(group.subsession.session.path, 'static')
    # image_A_path = os.path.join(static_path, f'image_A.png')
    # static_path = os.path.join(group.subsession.session.path, 'static')
    # image_B_path = os.path.join(static_path, f'_image_B.png')

    static_path = otree.settings.STATIC_ROOT
    image_A_path = os.path.join(static_path, 'Image1.png')
    image_B_path = os.path.join(static_path, 'Image2.png')

    image_A.save(image_A_path)
    image_B.save(image_B_path)


# PAGES
class Instructions(Page):
    form_model = 'player'

class WaitForSurvey(WaitPage):
    pass
class Survey(Page):
    form_model = 'player'
    form_fields = ['gender', 'College', 'BornPA', 'Job' ]

    def before_next_page(player, timeout_happened):
        gender(player)

    def error_message(player, timeout_happened):
        if not player.survey_error_displayed:
            player.survey_error_displayed = True  # Set the flag to True
            return "Please confirm your answers and press Next."




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
            return "This name was already taken. Please select another name."

    def before_next_page(player, timeout_happened):
        Fnames(player)
        creating_couple_id_gender(player)
        creating_CV_ind(player)
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
            return "This name was already taken. Please select another name."

    def before_next_page(player, timeout_happened):
        Mnames(player)
        creating_couple_id_gender(player)
        creating_CV_ind(player)
        Malename(player)



class FemaleNames(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.gender== 0

    form_model = 'player'
    form_fields = ['FemaleNames']

    def before_next_page(player, timeout_happened):
        creating_couple_id_gender(player)
        creating_CV_ind(player)
        Femalename(player)

class MaleNames(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.gender== 1

    form_model = 'player'
    form_fields = ['MaleNames']

    def before_next_page(player, timeout_happened):
        creating_couple_id_gender(player)
        creating_CV_ind(player)
        Malename(player)

class MyWaitPage(WaitPage):
    # ...

    # Define a new function that calls both functions
    @staticmethod
    def call_both_functions(group):
        creatingGroups(group)
        image_cv(group)

    # Assign the new function to after_all_players_arrive
    after_all_players_arrive = call_both_functions
    #after_all_players_arrive = creatingGroups







class ChoiceCV_groupA(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.InGroupA== True

    form_model = 'player'
    form_fields = ['rank1st', 'rank2nd', 'rank3rd', 'rank4th']


class ChoiceCV_groupB(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.InGroupB == True

    form_model = 'player'
    form_fields = ['rank1st', 'rank2nd', 'rank3rd', 'rank4th']

class end(Page):
    pass







page_sequence = [Instructions, WaitForSurvey, Survey,WaitForNames, NameSelectionF, NameSelectionM, MyWaitPage]

#page_sequence = [ Survey,WaitForNames, NameSelectionF, NameSelectionM, MyWaitPage]