from PIL import Image, ImageDraw, ImageFont
import os
from otree.api import *
import numpy as np



doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Partie1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    Fnames = ["Jade", "Louise", "Ambre", "Alba", "Emma", "Rose", "Alice", "Romy", "Anna", "Lina"]
    Mnames = ["Gabriel", "Léo", "Raphaël", "Louis", "Noah", "Jules", "Arthur", "Adam", "Lucas", "Sacha"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    Group_A = models.LongStringField()
    Group_B = models.LongStringField()
    Group_C = models.LongStringField()
    Group_D = models.LongStringField()
    cvA = models.LongStringField()
    cvB = models.LongStringField()
    cvC = models.LongStringField()
    cvD = models.LongStringField()
    cv_A_1 = models.LongStringField()
    cv_A_2 = models.LongStringField()
    cv_A_3 = models.LongStringField()
    cv_A_4 = models.LongStringField()
    cv_B_1 = models.LongStringField()
    cv_B_2 = models.LongStringField()
    cv_B_3 = models.LongStringField()
    cv_B_4 = models.LongStringField()
    cv_C_1 = models.LongStringField()
    cv_C_2 = models.LongStringField()
    cv_C_3 = models.LongStringField()
    cv_C_4 = models.LongStringField()
    cv_D_1 = models.LongStringField()
    cv_D_2 = models.LongStringField()
    cv_D_3 = models.LongStringField()
    cv_D_4 = models.LongStringField()



class Player(BasePlayer):
    survey_error_displayed = models.BooleanField(initial=False)
    gender = models.IntegerField(label="Quel est votre genre ?", widget=widgets.RadioSelectHorizontal,
                                 choices=[[0, "Femme"], [1, "Homme"]], initial=0)
    BornIDF = models.IntegerField(label="Etes vous né.e en  Ile de France ?", widget=widgets.RadioSelectHorizontal,
                                 choices=[[1, "Oui"], [0, "Non"]], initial=0)
    CommutingTime = models.IntegerField(
        label="Quel est votre temps de trajet quotidien (pour vous rendre à vos activités principales: travail, études, autres engagements,...) ?",
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

    InGroupA= models.BooleanField(default=False,)
    InGroupB=models.BooleanField(default=False,)
    InGroupC = models.BooleanField(default=False, )
    InGroupD = models.BooleanField(default=False, )
    vec_couple = models.LongStringField()
    vec_cv = models.LongStringField()
    name = models.IntegerField()
    partner_name = models.IntegerField()
    partner_gender = models.IntegerField(label="What gender do you identify with?", widget=widgets.RadioSelectHorizontal,
                                     choices=[[0, "Female"], [1, "Male"]])






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


def creating_couple_id_gender(player):
    vec_couple = []
    vec_couple.extend((player.id_in_group, player.gender))
    player.vec_couple = str(vec_couple)
    player.participant.vec_couple = player.vec_couple


def gender(player):
    player.participant.gender = player.gender
    player.participant.BornPA=player.BornIDF
    player.participant.Job=player.CommutingTime


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
            (player.id_in_group, player.FemaleNames,player.gender, player.BornIDF, player.CommutingTime, player.gender))
    elif player.gender == 1:
        vec_cv.extend((player.id_in_group, player.MaleNames,player.gender, player.BornIDF, player.CommutingTime, player.gender))
    player.vec_cv = str(vec_cv)
    player.participant.vec_cv = player.vec_cv


def creatingGroups(group):
    Group_A = []
    Group_B = []
    Group_C= []
    Group_D=[]
    cvA = []
    cvB = []
    cvC=[]
    cvD=[]
    female= []
    male= []
    femaleB=[]
    maleB=[]
    femaleC = []
    maleC = []
    femaleD = []
    maleD = []
    sum_hA = 0
    sum_fA = 0
    sum_hB = 0
    sum_fB = 0
    sum_hC = 0
    sum_fC = 0
    sum_hD = 0
    sum_fD = 0

    for player in group.get_players():
        if player.gender == 1:
            if sum_hA < 2:
                Group_A.append(player.id_in_group)
                cvA.append(player.vec_cv)
                player.InGroupA = True  # only the id is useful in group_A
                player.participant.InGroupA = True
                player.InGroupB = False
                player.participant.InGroupB = False
                player.InGroupC = False
                player.participant.InGroupC = False
                player.InGroupD = False
                player.participant.InGroupD = False
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
                player.InGroupB = False
                player.participant.InGroupB = False
                player.InGroupC = False
                player.participant.InGroupC = False
                player.InGroupD = False
                player.participant.InGroupD = False

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
                    player.InGroupA = False
                    player.participant.InGroupA = False
                    player.InGroupC = False
                    player.participant.InGroupC = False
                    player.InGroupD = False
                    player.participant.InGroupD = False
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
                    player.InGroupA = False
                    player.participant.InGroupA = False
                    player.InGroupC = False
                    player.participant.InGroupC = False
                    player.InGroupD = False
                    player.participant.InGroupD = False
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

    for player in group.get_players():
        if player.InGroupA == False and player.InGroupB == False:
            if player.gender == 1:
                if sum_hC < 2:
                    Group_C.append(player.id_in_group)  # only the id is usefull in group_A
                    cvC.append(player.vec_cv)
                    player.InGroupC = True
                    player.participant.InGroupC = True
                    player.InGroupB = False
                    player.participant.InGroupB = False
                    player.InGroupA = False
                    player.participant.InGroupA = False
                    player.InGroupD = False
                    player.participant.InGroupD = False
                    sum_hC += 1
                else:
                    player.InGroupC = False
                    player.participant.InGroupC = False
            else:
                if sum_fC < 2:
                    Group_C.append(player.id_in_group)
                    cvC.append(player.vec_cv)
                    player.InGroupC = True
                    player.participant.InGroupC = True
                    player.InGroupB = False
                    player.participant.InGroupB = False
                    player.InGroupA = False
                    player.participant.InGroupA = False
                    player.InGroupD = False
                    player.participant.InGroupD = False
                    sum_fC += 1
                else:
                    player.InGroupC = False
                    player.participant.InGroupC = False

    cv_C = [eval(cv) for cv in cvC]
    for cv in cv_C:
        if cv[-1] == 0:
            femaleC.append(cv)
        else:
            maleC.append(cv)

    cv_C = [maleC[0], femaleC[0], maleC[1], femaleC[1]]
    Group_C[0] = maleC[0][0]

    Group_C[1] = femaleC[0][0]

    Group_C[2] = maleC[1][0]

    Group_C[3] = femaleC[1][0]

    group.Group_C = str(Group_C)
    group.session.Group_C = str(Group_C)
    group.cvC = str(cv_C)
    group.session.cvC = str(cv_C)

    for player in group.get_players():
        if player.InGroupA == False and player.InGroupB == False and player.InGroupC==False:
                Group_D.append(player.id_in_group)  # only the id is usefull in group_A
                cvD.append(player.vec_cv)
                player.InGroupD = True
                player.participant.InGroupD = True
                player.InGroupB = False
                player.participant.InGroupB = False
                player.InGroupC = False
                player.participant.InGroupC = False
                player.InGroupA = False
                player.participant.InGroupA = False

        else:
            player.InGroupD = False
            player.participant.InGroupD = False

    cv_D = [eval(cv) for cv in cvD]
    for cv in cv_D:
        if cv[-1] == 0:
            femaleD.append(cv)
        else:
            maleD.append(cv)
    if len(femaleD) == 2:
        cv_D = [femaleD[0], maleD[0], femaleD[1], maleD[1]]
        Group_D[0] = femaleD[0][0]

        Group_D[1] = maleD[0][0]

        Group_D[2] = femaleD[1][0]

        Group_D[3] = maleD[1][0]

    elif len(femaleD) == 1:
        cv_D = [maleD[0], femaleD[0], maleD[1], maleD[2]]
        Group_D[0] = maleD[0][0]

        Group_D[1] = femaleD[0][0]

        Group_D[2] = maleD[1][0]

        Group_D[3] = maleD[2][0]

    elif len(femaleD) == 3:
        cv_D = [femaleD[0], maleD[0], femaleD[1], femaleD[2]]
        Group_D[0] = femaleD[0][0]

        Group_D[1] = maleD[0][0]

        Group_D[2] = femaleD[1][0]

        Group_D[3] = femaleD[2][0]

    elif len(femaleD) == 4:
        cv_D = [femaleD[0], femaleD[1], femaleD[2], femaleD[3]]
        Group_D[0] = femaleD[0][0]

        Group_D[1] = femaleD[1][0]

        Group_D[2] = femaleD[2][0]

        Group_D[3] = femaleD[3][0]





    group.Group_D = str(Group_D)
    group.session.Group_D = str(Group_D)
    group.cvD = str(cv_D)
    group.session.cvD = str(cv_D)



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
    group.cv_C_1 = str(cvC[0])
    group.session.cv_C_1 = str(cv_C[0])
    group.cv_C_2 = str(cvC[1])
    group.session.cv_C_2 = str(cv_C[1])
    group.cv_C_3 = str(cvC[2])
    group.session.cv_C_3 = str(cv_C[2])
    group.cv_C_4 = str(cvC[3])
    group.session.cv_C_4 = str(cv_C[3])
    group.cv_D_1 = str(cvD[0])
    group.session.cv_D_1 = str(cv_D[0])
    group.cv_D_2 = str(cvD[1])
    group.session.cv_D_2 = str(cv_D[1])
    group.cv_D_3 = str(cvD[2])
    group.session.cv_D_3 = str(cv_D[2])
    group.cv_D_4 = str(cvD[3])
    group.session.cv_D_4 = str(cv_D[3])


def create_image_cv(cv_1, cv_2, cv_3, cv_4):

    # Création de l'image vide
    image = Image.new("RGB", (800, 600), "white")
    draw = ImageDraw.Draw(image)

    # Définition des coordonnées pour les encadrés et les cadres
    frame_padding = 20
    frame_width = image.width // 2 - frame_padding * 2
    frame_height = image.height // 2 - frame_padding * 2

    # Adjust padding values to control the space
    top_padding = 50
    bottom_padding = 10
    top_padding_within_frame = 20

    top_left_frame = (frame_padding, frame_padding + top_padding)
    top_right_frame = (image.width // 2 + frame_padding, frame_padding + top_padding)
    bottom_left_frame = (frame_padding, image.height // 2 + frame_padding - bottom_padding)
    bottom_right_frame = (image.width // 2 + frame_padding, image.height // 2 + frame_padding - bottom_padding)

    top_left = (top_left_frame[0] + 10, top_left_frame[1] + 10)
    top_right = (top_right_frame[0] + 10, top_right_frame[1] + 10)
    bottom_left = (bottom_left_frame[0] + 10, bottom_left_frame[1] + 10)
    bottom_right = (bottom_right_frame[0] + 10, bottom_right_frame[1] + 10)


    # Définition des questions et réponses pour chaque CV
    questions = ["Prénom :","Genre :",  "Naissance Ile De France :", "Temps de Trajet :"]
    answers = [
        [["Jade", "Gabriel"], ["Louise", "Léo"], ["Ambre", "Raphaël"], ["Alba", "Louis"],["Emma", "Noah"],["Rose", "Jules"],["Alice", "Arthur"],["Romy", "Adam"],["Anna", "Lucas"],["Lina", "Sacha"]],
        ["Femme", "Homme"],
        ["Non", "Oui"],
        ["> 30 min", "< 30 min"]

    ]

    import otree.settings
    static_path = otree.settings.STATIC_ROOT
    font_path = os.path.join(static_path, 'arial.ttf')
    # Chargement de la police
    font = ImageFont.truetype(font_path, 18)
    # font = ImageFont.truetype("arial.ttf", 18)  # Remplacez "arial.ttf" par le chemin vers votre police
    font_gras = ImageFont.truetype(font_path, 18)

    # Dessin des cadres autour de chaque CV
    # Adjusting frames to reduce space
    top_left_frame_adjusted = (
        top_left_frame[0],
        top_left_frame[1] + top_padding_within_frame,  # Adjusted vertical position
        top_left_frame[0] + frame_width,
        top_left_frame[1] + frame_height - 50 * 2
    )
    draw.rectangle(top_left_frame_adjusted, outline="black", width=2)

    top_right_frame_adjusted = (
        top_right_frame[0],
        top_right_frame[1] + top_padding_within_frame,  # Adjusted vertical position
        top_right_frame[0] + frame_width,
        top_right_frame[1] + frame_height - 50 * 2
    )
    draw.rectangle(top_right_frame_adjusted, outline="black", width=2)

    bottom_left_frame_adjusted = (
        bottom_left_frame[0],
        bottom_left_frame[1] + top_padding_within_frame,  # Adjusted vertical position
        bottom_left_frame[0] + frame_width,
        bottom_left_frame[1] + frame_height - 50 * 2
    )
    draw.rectangle(bottom_left_frame_adjusted, outline="black", width=2)

    bottom_right_frame_adjusted = (
        bottom_right_frame[0],
        bottom_right_frame[1] + top_padding_within_frame,  # Adjusted vertical position
        bottom_right_frame[0] + frame_width,
        bottom_right_frame[1] + frame_height - 50 * 2
    )
    draw.rectangle(bottom_right_frame_adjusted, outline="black", width=2)

    # Displaying player names above the frames
    name_padding = 10  # Adjust the padding between the names and the upper border

    draw.text((top_left_frame[0] + frame_width // 2, top_left_frame[1] - name_padding), "Joueur A", fill="black",
              font=font_gras)
    draw.text((top_right_frame[0] + frame_width // 2, top_right_frame[1] - name_padding), "Joueur B", fill="black",
              font=font_gras)
    draw.text((bottom_left_frame[0] + frame_width // 2, bottom_left_frame[1] - name_padding), "Joueur C", fill="black",
              font=font_gras)
    draw.text((bottom_right_frame[0] + frame_width // 2, bottom_right_frame[1] - name_padding), "Joueur D",
              fill="black", font=font_gras)


    # Affichage du premier CV en haut à gauche

    #draw.text((top_left[0], top_left[1]),  fill="black", font=font_gras)
    for i, question in enumerate(questions):
        if i == 0:
            answer = answers[0][cv_1[1] - 1][cv_1[-1]]
        else:
            answer = answers[i][cv_1[i+1]]


        draw.text((top_left[0], top_left[1] + 30 * (i + 1)), question, fill="black", font=font_gras)
        draw.text((top_left[0] + 225, top_left[1] + 30 * (i + 1)), answer, fill="black", font=font)

    # Affichage du deuxième CV en haut à droite
    #draw.text((top_right[0], top_right[1]),  fill="black", font=font_gras)
    for i, question in enumerate(questions):
        if i == 0:
            answer = answers[0][cv_2[1] - 1][cv_2[-1]]
        else:
            answer = answers[i][cv_2[i+1]]
        draw.text((top_right[0], top_right[1] + 30 * (i + 1)), question, fill="black", font=font_gras)
        draw.text((top_right[0] + 225, top_right[1] + 30 * (i + 1)), answer, fill="black", font=font)

        # Affichage du troisième CV en bas à gauche
    #draw.text((bottom_left[0], bottom_left[1]),  fill="black", font=font_gras)
    for i, question in enumerate(questions):
        if i == 0:
            answer = answers[0][cv_3[1] - 1][cv_3[-1]]
        else:
            answer = answers[i][cv_3[i+1]]
        draw.text((bottom_left[0], bottom_left[1] + 30 * (i + 1)), question, fill="black", font=font_gras)
        draw.text((bottom_left[0] + 225, bottom_left[1] + 30 * (i + 1)), answer, fill="black", font=font)

    # Affichage du quatrième CV en bas à
    #draw.text((bottom_right[0], bottom_right[1]),  fill="black", font=font_gras)
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
    cvC1 = eval(group.session.cv_C_1)
    cvC2 = eval(group.session.cv_C_2)
    cvC3 = eval(group.session.cv_C_3)
    cvC4 = eval(group.session.cv_C_4)
    cvD1 = eval(group.session.cv_D_1)
    cvD2 = eval(group.session.cv_D_2)
    cvD3 = eval(group.session.cv_D_3)
    cvD4 = eval(group.session.cv_D_4)

    image_A = create_image_cv(cvA1, cvA2, cvA3, cvA4)
    image_B = create_image_cv(cvB1, cvB2, cvB3, cvB4)
    image_C = create_image_cv(cvC1, cvC2, cvC3, cvC4)
    image_D = create_image_cv(cvD1, cvD2, cvD3, cvD4)

    # static_path = os.path.join(group.subsession.session.path, 'static')
    # image_A_path = os.path.join(static_path, f'image_A.png')
    # static_path = os.path.join(group.subsession.session.path, 'static')
    # image_B_path = os.path.join(static_path, f'_image_B.png')

    static_path = otree.settings.STATIC_ROOT
    image_A_path = os.path.join(static_path, 'Image1.png')
    image_B_path = os.path.join(static_path, 'Image2.png')
    image_C_path = os.path.join(static_path, 'Image3.png')
    image_D_path = os.path.join(static_path, 'Image4.png')

    image_A.save(image_A_path)
    image_B.save(image_B_path)
    image_C.save(image_C_path)
    image_D.save(image_D_path)


# PAGES
class Instructions_general(Page):
    form_model = 'player'
class WaitforPartie1(WaitPage):
    pass

class Instructions(Page):
    form_model = 'player'

class WaitForSurvey(WaitPage):
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
            return "Ce prénom a déjà été choisi par un autre participant. Veuillez en sélectionner un nouveau."

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









#page_sequence = [ Survey, NameSelectionF, NameSelectionM, MyWaitPage]

page_sequence = [ Instructions_general, WaitforPartie1,Instructions, WaitForSurvey,Survey,WaitforInstructionPrenom, Prenom, NameSelectionF, NameSelectionM, MyWaitPage]