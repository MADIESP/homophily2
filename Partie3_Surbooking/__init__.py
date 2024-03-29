from otree.api import *
import os


doc = """
3 rounds played in teams
"""


class C(BaseConstants):
    NAME_IN_URL = 'Partie3_Surbooking'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 30


class Subsession(BaseSubsession):
    Treatment = models.IntegerField()



class Group(BaseGroup):
    selected_count = models.IntegerField()
    selected_player=models.IntegerField(default=2)
    points3 = models.IntegerField()
    solo = models.BooleanField()


class Player(BasePlayer):
    nb_participants=models.IntegerField()
    enjoy = models.IntegerField(label="", choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal)
    Treatment = models.IntegerField()
    test_JeuCollectif = models.IntegerField(
        label="A chaque période, quelle réponse sera sélectionnée pour être la <b> réponse de l’équipe </b> ? ",
        widget=widgets.RadioSelect,
        choices=[[0, "Ma réponse sera toujours sélectionnée. "],
                 [1, "La réponse de mon partenaire sera toujours sélectionnée. "],
                 [2, "Une de nos réponses sera sélectionnée de manière aléatoire. "]])
    test_JeuCollectif_equipe = models.IntegerField(
        label="Si vous jouez en équipe : à chaque période, quelle réponse sera sélectionnée pour être la <b> réponse de l’équipe </b> ? ",
        widget=widgets.RadioSelect,
        choices=[[0, "Ma réponse sera toujours sélectionnée. "],
                 [1, "La répofnse de mon partenaire sera toujours sélectionnée. "],
                 [2, "Une de nos réponses sera sélectionnée de manière aléatoire. "]])
    test_JeuCollectif_solo = models.IntegerField(
        label="Si vous jouez seul : à chaque période, combien de points obtiendrez-vous si votre réponse est correcte ? ",
        widget=widgets.RadioSelect,
        choices=[[0, "J'obtiendrais 1 point. "],
                 [1, "Je n'obtiendrais aucun point. "]], initial=1)


    FemaleNames = models.IntegerField()
    MaleNames = models.IntegerField()
    name = models.IntegerField()
    gender=models.IntegerField()
    partner_name = models.IntegerField()
    partner_gender=models.IntegerField()
    count = models.IntegerField(label="Combien de 0s il y a t-il dans ce tableau ?")
    correct = models.BooleanField(doc="Whether the count is correct.")
    correct_Group = models.BooleanField(doc="Whether the selected count is correct.", initial=False)
    partner_selected = models.BooleanField(initial=False)
    belief_own = models.IntegerField(label="", choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal)
    belief_partner = models.IntegerField(
        label="", choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal)
    points_partie3 = models.IntegerField()
    points_beliefs1 = models.IntegerField()
    solo=models.BooleanField()



def creating_session(subsession:Subsession):
    subsession.Treatment = subsession.session.config['Treatment']


    if subsession.round_number == 1:

        if subsession.session.num_participants == 8:
            new_structure = [[1,2], [3,4], [5,6], [7,8]]
        elif subsession.session.num_participants==7:
            new_structure = [[1, 2], [3,4], [5,6], [7]]
        elif subsession.session.num_participants==6:
            new_structure = [[1, 2], [3, 4], [5, 6]]
        elif subsession.session.num_participants==5:
            new_structure = [[1, 2],[3,4], [5]]
        elif subsession.session.num_participants==4:
            new_structure = [[1, 2], [3, 4]]
        elif subsession.session.num_participants==3:
            new_structure = [[1, 2], [3]]
        elif subsession.session.num_participants==2:
            new_structure = [[1, 2]]
        elif subsession.session.num_participants==1:
            new_structure = [[1]]

        subsession.set_group_matrix(new_structure)

    else:
        subsession.group_like_round(1)


# FUNCTIONS verbose_name='',

#def creating_session(subsession: Subsession):
    #subsession.Treatment = subsession.session.config['Treatment']
    #if subsession.round_number == 1:
        #subsession.group_randomly()
    #else:
        #subsession.group_like_round(1)

def set_correct(player):
    correct_answers = [49, 42, 45, 48,49,51]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.count == correct:
            correct = True
        else:
            correct = False

    player.correct = correct


def solo(group):
    for player in group.get_players():

        player.name=player.participant.name

    all_names = [player.participant.name for player in group.get_players()]

    for player in group.get_players():
        if len(all_names)==2:
            player.solo=False
            player.participant.solo = False

        elif len(all_names)==1:
            player.solo=True
            player.participant.solo= True

    group.solo=player.solo
    group.session.solo=player.solo


    for player in group.get_players():
        if group.session.num_participants==1:
            nb_participants=1
        elif group.session.num_participants==2:
            nb_participants=2
        elif group.session.num_participants==3:
            nb_participants=3
        elif group.session.num_participants==4:
            nb_participants=4
        elif group.session.num_participants==5:
            nb_participants=5
        elif group.session.num_participants==6:
            nb_participants=6
        elif group.session.num_participants==7:
            nb_participants=7
        elif group.session.num_participants==8:
            nb_participants=8

        player.nb_participants=nb_participants
        player.participant.nb_participants=nb_participants


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
        if len(all_names)==2:
            partner_name=all_names[2-player.id_in_group]
            partner_gender = all_gender[2-player.id_in_group]
            partner_point= all_points[2-player.id_in_group]

            player.participant.partner_name= partner_name
            player.participant.partner_gender=partner_gender
            player.participant.partner_point2=partner_point


    #player.partner_gender = partner_gender
    #player.partner_name = partner_name


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

        elif len(all_names) == 1:
            pass




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


def set_correct_group(group):
    correct_answers = [49, 42, 45, 48, 49, 51]
    for group, correct in zip(group.in_all_rounds(), correct_answers):
        if group.selected_count  == correct:
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
    points3 = 0
    correct_answers = [49, 42, 45, 48, 49, 51]
    for group, correct in zip(group.in_all_rounds(), correct_answers):
        # print(p.answer, correct, p.answer == correct)
        points3 = points3 + 1 if group.selected_count==correct else points3
    group.points3 = points3

    for player in group.get_players():
        player.points_partie3 = group.points3
        player.participant.points_partie3 = player.points_partie3

def get_points_solo(player:BasePlayer):
    points_partie3 = 0
    correct_answers = [49, 42, 45, 48, 49, 51]
    for p, correct in zip(player.in_all_rounds(), correct_answers):
        # print(p.answer, correct, p.answer == correct)
        points_partie3 = points_partie3 + 1 if p.count == correct else points_partie3
    player.points_partie3 = points_partie3

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

def get_points_beliefs_solo(player):
    points_beliefs = 0
    if player.belief_own== player.participant.points_partie2:
        points_beliefs= points_beliefs +1
    else:
        points_beliefs = points_beliefs

    player.points_beliefs1=points_beliefs
    player.participant.points_beliefs1=player.points_beliefs1

# PAGES


class WaitforStart(WaitPage):


    after_all_players_arrive = solo
class Instructions_pair(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.nb_participants == 4 or player.round_number == 1 and player.participant.nb_participants == 6 or player.round_number == 1 and player.participant.nb_participants == 8


class Instructions_impair(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.nb_participants==3 or player.round_number == 1 and player.participant.nb_participants==5 or player.round_number == 1 and player.participant.nb_participants==7


class Instructions1(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.nb_participants == 1


class Instructions2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.nb_participants == 2



class WaitforInstructions2(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1



class InstructionsPos(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.nb_participants>1

class InstructionsPosSolo(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.nb_participants==3 or player.round_number == 1 and player.participant.nb_participants==5 or player.round_number == 1 and player.participant.nb_participants==7 or player.round_number == 1 and player.participant.nb_participants==1


class WaitforInstructions3(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class InstructionsNegControl(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.subsession.Treatment == 1 and player.participant.nb_participants>1


class InstructionsNegTreatment1(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.subsession.Treatment == 2 and player.participant.nb_participants>1

class InstructionsNegControlSolo(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.nb_participants == 3 or player.round_number == 1 and player.participant.nb_participants == 5 or player.round_number == 1 and player.participant.nb_participants == 7 or player.round_number == 1 and player.participant.nb_participants == 1


class WaitPage1(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class TestComprehension(Page):
    form_model = 'player'
    form_fields = [ 'test_JeuCollectif']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.nb_participants == 4  or player.round_number == 1 and player.participant.nb_participants == 2 or player.round_number == 1 and player.participant.nb_participants == 6 or player.round_number == 1 and player.participant.nb_participants == 8

class TestComprehensionImpair(Page):
    form_model = 'player'
    form_fields = [ 'test_JeuCollectif_equipe', 'test_JeuCollectif_solo']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.nb_participants == 3 or player.round_number == 1 and player.participant.nb_participants == 5 or player.round_number == 1 and player.participant.nb_participants == 7

class Comprehension_Error(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and  player.field_maybe_none("test_JeuCollectif_equipe")!=2 and  player.participant.nb_participants == 2  or  player.round_number == 1 and  player.field_maybe_none("test_JeuCollectif_equipe")!=2 and  player.participant.nb_participants == 4 or  player.round_number == 1 and  player.field_maybe_none("test_JeuCollectif_equipe")!=2 and  player.participant.nb_participants == 6 or  player.round_number == 1 and  player.field_maybe_none("test_JeuCollectif_equipe")!=2 and  player.participant.nb_participants == 8


class Comprehension_Error_Impair(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.field_maybe_none("test_JeuCollectif_equipe")!=2 and  player.participant.nb_participants == 3  or  player.round_number == 1 and  player.field_maybe_none("test_JeuCollectif_equipe")!=2 and  player.participant.nb_participants == 5 or  player.round_number == 1 and  player.field_maybe_none("test_JeuCollectif_equipe")!=2 and  player.participant.nb_participants == 7 or player.round_number == 1 and  player.field_maybe_none("test_JeuCollectif_solo")!=0 and  player.participant.nb_participants == 3  or  player.round_number == 1 and  player.field_maybe_none("test_JeuCollectif_solo")!=0 and  player.participant.nb_participants == 5 or  player.round_number == 1 and  player.field_maybe_none("test_JeuCollectif_solo")!=0 and  player.participant.nb_participants == 7





class MyWaitPage(WaitPage):
  


    after_all_players_arrive = partner_name

    @staticmethod
    def is_displayed(player: Player):
        return  player.round_number == 1

class NamePartner(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.solo==False


class NamePartnerSolo(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.solo==True





class WaitforBelief(WaitPage):

    wait_for_all_groups = True
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.nb_participants>3




class Belief(Page):
    form_model = 'player'
    form_fields = ['belief_own', 'belief_partner']

    @staticmethod
    def is_displayed(player: Player):
        return  player.round_number == 1 and player.participant.nb_participants>1 and player.participant.solo==False
    def before_next_page(player, timeout_happened):
        get_points_beliefs(player)

class BeliefSolo(Page):
    form_model = 'player'
    form_fields = ['belief_own']

    @staticmethod
    def is_displayed(player: Player):
        return  player.round_number == 1 and player.participant.nb_participants==1 or player.round_number == 1 and player.participant.solo==True
    def before_next_page(player, timeout_happened):
        get_points_beliefs_solo(player)



class WaitforFirstTable(WaitPage):


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

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.solo==False

class CountSolo(Page):

    timeout_seconds = C.TIME_PER_PROBLEM
    form_model = 'player'
    form_fields = ['count']
    timer_text = 'Temps restant pour compter ce tableau:'

    def before_next_page(player, timeout_happened):
        set_correct(player)
        get_points_solo(player)
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.solo==True


class WaitforFeedback(WaitPage):
    body_text = "En attente de votre partenaire."

    @staticmethod
    def call_functions(group):
        partner_name(group)
        select_group_answer(group)
        set_correct_group(group)
        get_points(group)




    after_all_players_arrive = call_functions

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.solo == False


class WaitforFeedbackSolo(WaitPage):


    @staticmethod
    def is_displayed(player: Player):
        return player.participant.solo == True



class FeedbackPositive(Page):

    @staticmethod
    def is_displayed(player: Player):
        return  player.correct_Group == True and player.participant.solo == False

class FeedbackPositiveSolo(Page):



    @staticmethod
    def is_displayed(player: Player):
        return player.correct == True and player.participant.solo == True


class FeedbackNegative(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected==True  and player.subsession.Treatment != 1 and player.participant.solo == False

    #@staticmethod
    #def is_displayed(player: Player):
        #return player.partner_selected == True

class FeedbackNegControl(Page):



    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False  and player.subsession.Treatment == 1  and player.participant.solo == False

class FeedbackNeg2(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected==False and player.subsession.Treatment == 2  and player.participant.solo == False

class FeedbackNegativeSolo(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct == False and player.participant.solo == True


class WaitforNextTable(WaitPage):
    body_text = "En attente de votre partenaire."

class Point(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 6
class WaitforNextRound(WaitPage):


    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 6




#page_sequence = [ Survey,WaitForNames, NameSelectionF,NameSelectionM, InstructionsRanking, WaitforInstructions2, InstructionsRanking2, WaitforInstructions3, Instructions, InstructionsTreatment2, WaitforInstructions4,InstructionsPos, WaitforInstructions5, InstructionsNegControl, InstructionsNegTreatment1, InstructionsNegTreatment2, MyWaitPage,Belief,WaitforFirstTable, Count, WaitforFeedback, FeedbackPositive, FeedbackNegControl, FeedbackNegative, FeedbackNeg2, Message, WaitforCommunication, MessageSent, MessageReceived, WaitforNextTable]
#page_sequence = [  MyWaitPage,NamePartner, WaitforBelief, Belief,WaitforFirstTable, Count, WaitforFeedback, FeedbackPositive, FeedbackNegControl, FeedbackNegative, FeedbackNeg2, Message, WaitforCommunication, MessageSent, MessageReceived, WaitforNextTable, WaitforNextRound]


page_sequence = [WaitforStart,Instructions_pair, Instructions_impair, Instructions1, Instructions2,WaitforInstructions2,InstructionsPos,InstructionsPosSolo,WaitforInstructions3,InstructionsNegControl,InstructionsNegControlSolo, InstructionsNegTreatment1, WaitPage1, TestComprehension, TestComprehensionImpair, Comprehension_Error, Comprehension_Error_Impair, MyWaitPage, NamePartner, NamePartnerSolo, WaitforBelief, Belief, BeliefSolo,WaitforFirstTable, Count, CountSolo, WaitforFeedback, WaitforFeedbackSolo, FeedbackPositive, FeedbackPositiveSolo, FeedbackNegativeSolo, FeedbackNegControl, FeedbackNegative, FeedbackNeg2, WaitforNextTable, WaitforNextRound]


#page_sequence = [ MyWaitPage, NamePartner,  WaitforFirstTable, Count, CountSolo, WaitforFeedback]
