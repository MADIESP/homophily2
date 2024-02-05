from otree.api import *
import os


doc = """
3 rounds played in teams
"""


class C(BaseConstants):
    NAME_IN_URL = 'Round2_Surbooking'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 3


class Subsession(BaseSubsession):
    Treatment = models.IntegerField()



class Group(BaseGroup):
    selected_count = models.IntegerField()
    selected_player=models.IntegerField(default=2)


class Player(BasePlayer):
    Treatment = models.IntegerField()
    enjoy = models.IntegerField(label="", choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal,
                                initial=3)
    test_JeuCollectif = models.IntegerField(
        label="3- A chaque période, quelle réponse sera sélectionnée pour être la <b> réponse de l’équipe </b> ? ",
        widget=widgets.RadioSelect,
        choices=[[0, "Ma réponse sera toujours sélectionnée. "],
                 [1, "La réponse de mon partenaire sera toujours sélectionnée. "],
                 [2, "Une de nos réponses sera sélectionnée de manière aléatoire. "]])
    test_Belief1 = models.IntegerField(
        label="Si vous pensez avoir correctement compté 3 tableaux dans la partie 3, quelle réponse devait vous indiquer ? ",
        widget=widgets.RadioSelectHorizontal,
        choices=[0,1,2,3,4])
    test_Belief2= models.IntegerField(
        label="Si vous pensez que votre partenaire a correctement compté 3 tableaux dans la partie 3, quelle réponse devait vous indiquer ? ",
        widget=widgets.RadioSelectHorizontal,
        choices=[0, 1, 2, 3, 4])
    test_Belief3 = models.IntegerField(
        label="Que gagnerez vous si vous avez correctement estimé votre performance au début de cette partie? ",
        widget=widgets.RadioSelect,
        choices=[[0, "Je n'obtiendrais aucun point supplémentaire."],[1, "Je gagnerais un point supplémentaire."]])
    test_Belief4 = models.IntegerField(
        label="Que gagnerez vous si vous avez correctement estimé la performance de votre partenaire au début de cette partie? ",
        widget=widgets.RadioSelect,
        choices=[[0, "Je n'obtiendrais aucun point supplémentaire."], [1, "Je gagnerais un point supplémentaire."]])

    gender = models.IntegerField(label="What gender do you identify with?", widget=widgets.RadioSelectHorizontal,
                                 choices=[[0, "Female"], [1, "Male"]], default=1)
    FemaleNames = models.IntegerField()
    MaleNames = models.IntegerField()
    name = models.IntegerField()
    partner_name = models.IntegerField()
    partner_gender=models.IntegerField()
    count = models.IntegerField(label="Combien de 0s il y a t-il dans ce tableau ?")
    correct = models.BooleanField(doc="Whether the count is correct.")
    correct_Group = models.BooleanField(doc="Whether the selected count is correct.")
    partner_selected = models.BooleanField()
    belief_own = models.IntegerField(label="", choices=[0, 1, 2, 3, 4,5,6], widget=widgets.RadioSelectHorizontal, )
    belief_partner = models.IntegerField(
        label="", choices=[0, 1, 2, 3, 4,5,6 ], widget=widgets.RadioSelectHorizontal, )


# FUNCTIONS verbose_name='',

def creating_session(subsession: Subsession):
    subsession.Treatment = subsession.session.config['Treatment']
    if subsession.round_number == 1:
        subsession.group_randomly()
    else:
        subsession.group_like_round(1)

def set_correct(player):
    correct_answers = [47, 52, 46, 61, 54, 50]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.count == correct:
            correct = True
        else:
            correct = False

    player.correct = correct

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

    group.session.all_gender = str(all_gender)
    group.session.all_names = str(all_names)

    for player in group.get_players():
        partner_name = all_names[2 - player.id_in_group]
        partner_gender = all_gender[2 - player.id_in_group]

        player.participant.partner_name_round2 = partner_name
        player.participant.partner_gender_round2 = partner_gender

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


# PAGES



class Instructions(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1




class MyWaitPage(WaitPage):
  


    after_all_players_arrive = partner_name

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

class WaitforFeedback(WaitPage):
    body_text = "En attente de votre partenaire."

    @staticmethod
    def call_functions(group):
        partner_name(group)
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
        return player.correct_Group == False and player.partner_selected==True  and player.subsession.Treatment != 1

    #@staticmethod
    #def is_displayed(player: Player):
        #return player.partner_selected == True

class FeedbackNegControl(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False  and player.subsession.Treatment == 1

class WaitforNextTable(WaitPage):
    body_text = "En attente de votre partenaire."


class Enjoy(Page):
    form_model = 'player'
    form_fields = ['enjoy']

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


#page_sequence = [ Instructions,WaitforInstructions2,InstructionsPos,WaitforInstructions3,InstructionsNegControl,InstructionsNegControl, WaitPage1, TestCompréhension, Compréhension_Error, MyWaitPage, NamePartner, TestCompréhensionBeliefs, Compréhension_Belief_Error, WaitforBelief, Belief, WaitforFirstTable, Count, WaitforFeedback, FeedbackPositive, FeedbackNegControl, FeedbackNegative, WaitforNextTable, WaitforNextRound]

page_sequence = [MyWaitPage, NamePartner,WaitforBelief, Belief, WaitforFirstTable, Count, WaitforFeedback, FeedbackPositive, FeedbackNegControl, FeedbackNegative, WaitforNextTable, Enjoy, WaitforNextRound]
