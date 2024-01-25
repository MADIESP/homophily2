from otree.api import *
import os


doc = """
3 rounds played in teams
"""


class C(BaseConstants):
    NAME_IN_URL = 'Round2_Test'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 30
    Fnames = ["Mary", "Emma", "Patricia", "Elizabeth"]
    Mnames = ["James", "David", "John", "Robert"]



class Subsession(BaseSubsession):
    Treatment = models.IntegerField()


class Group(BaseGroup):
    selected_count = models.IntegerField()
    selected_player=models.IntegerField(default=2)


class Player(BasePlayer):
    test_ranking1=models.IntegerField(label="Avez-vous <b> plus de chance </b> d’être apparié au joueur que vous avez classé en première position ou en deuxième position ? ", widget=widgets.RadioSelectHorizontal,
                                 choices=[[0, "1ère position"], [1, "2ème position"]])
    test_ranking2 = models.IntegerField(
        label="Avez-vous <b> moins de chance </b> d’être apparié au joueur que vous avez classé en troisième position ou en quatrième position ? ",
        widget=widgets.RadioSelectHorizontal,
        choices=[[0, "3ème position"], [1, "4ème position"]])
    test_JeuCollectif=models.IntegerField(label="A chaque période, quelle réponse sera sélectionnée pour être la réponse de l’équipe ? ", widget=widgets.RadioSelectHorizontal,
                                 choices=[[0, "Ma réponse sera toujours sélectionnée. "], [1, "La réponse de mon partenaire sera toujours sélectionnée. "], [2, "Une de nos réponses sera sélectionnée de manière aléatoire. "]])
    Treatment = models.IntegerField()
    gender = models.IntegerField(label="What gender do you identify with?", widget=widgets.RadioSelectHorizontal,
                                 choices=[[0, "Female"], [1, "Male"]], default=1)
    FemaleNames = models.IntegerField()
    MaleNames = models.IntegerField()
    name = models.IntegerField()
    partner_name = models.IntegerField()
    partner_gender=models.IntegerField()
    count = models.IntegerField(label="Combien de 0s il y a-t-il dans ce tableau ?")
    correct = models.BooleanField(doc="Whether the count is correct.")
    correct_Group = models.BooleanField(doc="Whether the selected count is correct.")
    partner_selected = models.BooleanField(doc="Whether the count is correct.")
    belief_own = models.IntegerField(label="", choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal, )
    belief_partner = models.IntegerField(
        label="", choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal, )
    Message = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                  choices=[[1, "No stress, this matrix can be tricky! "],
                                           [2, "Don't worry, mistakes happen!"],
                                           [3, "I know it's tough, but try to focus more. "],
                                           [4, "It's crucial to get the exact count, you should try another counting method. "]])

    chosen_nameF = models.StringField(
        choices=C.Fnames,
        label="Please select a name that will be assigned to you throughout the experiment:",
        initial="",
    )
    chosen_nameM = models.StringField(
        choices=C.Mnames,
        label="Please select a name that will be assigned to you throughout the experiment:",
        initial="",
    )


# FUNCTIONS verbose_name='',

def creating_session(subsession: Subsession):
    subsession.Treatment = subsession.session.config['Treatment']
    if subsession.round_number == 1:
        subsession.group_randomly()
    else:
        subsession.group_like_round(1)

def Fnames(player):
    if player.chosen_nameF=="Mary":
        FemaleNames=1
    elif player.chosen_nameF=="Emma":
        FemaleNames=2
    elif player.chosen_nameF=="Patricia":
        FemaleNames = 3
    elif player.chosen_nameF=="Elizabeth":
        FemaleNames = 4

    player.FemaleNames=FemaleNames


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

def set_correct(player):
    correct_answers = [47, 52, 46, 61, 54, 50]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.count == correct:
            correct = True
        else:
            correct = False

    player.correct = correct



def gender(player):
    player.participant.gender=player.gender

def Femalename(player):
    player.participant.FemaleNames=player.FemaleNames

def Malename(player):
    player.participant.MaleNames=player.MaleNames


def partner_name(group):

    for player in group.get_players():
        if player.participant.gender == 0:
            player.participant.name = player.participant.FemaleNames
        else:
            player.participant.name = player.participant.MaleNames

    all_names=[player.participant.name for player in group.get_players()]
    all_gender=[player.participant.gender for player in group.get_players()]


    #player.participant.name=player.name
    #player.participant.gender=player.gender


    #for player in group.get_players():
        #if player.id_in_group==1:
            #partner_name=all_names[1]
            #partner_gender=all_gender[1]

        #else:

            #partner_name=all_names[0]
            #partner_gender=all_gender[0]

    for player in group.get_players():
        partner_name=all_names[2-player.id_in_group]
        partner_gender = all_gender[2-player.id_in_group]

        player.participant.partner_name= partner_name
        player.participant.partner_gender=partner_gender

    #player.partner_gender = partner_gender
    #player.partner_name = partner_name


        if player.participant.partner_gender==1 and player.participant.partner_name==1:
            player.participant.name_partner_round2='James'
        elif player.participant.partner_gender==1 and player.participant.partner_name==2:
            player.participant.name_partner_round2='David'
        elif player.participant.partner_gender==1 and player.participant.partner_name==3:
            player.participant.name_partner_round2='John'
        elif player.participant.partner_gender==1 and player.participant.partner_name==4:
            player.participant.name_partner_round2='Robert'
        elif player.participant.partner_gender == 1 and player.participant.partner_name == 5:
            player.participant.name_partner_round2 = 'Liam'
        elif player.participant.partner_gender == 1 and player.participant.partner_name == 6:
            player.participant.name_partner_round2 = 'Noah'
        elif player.participant.partner_gender == 1 and player.participant.partner_name == 7:
            player.participant.name_partner_round2 = 'William'
        elif player.participant.partner_gender == 1 and player.participant.partner_name == 8:
            player.participant.name_partner_round2 = 'Henry'
        elif player.participant.partner_gender == 1 and player.participant.partner_name == 9:
            player.participant.name_partner_round2 = 'Thomas'
        elif player.participant.partner_gender == 1 and player.participant.partner_name == 10:
            player.participant.name_partner_round2 = 'Christopher'
        elif player.participant.partner_gender==0 and player.participant.partner_name==1:
            player.participant.name_partner_round2='Mary'
        elif player.participant.partner_gender==0 and player.participant.partner_name==2:
            player.participant.name_partner_round2='Emma'
        elif player.participant.partner_gender==0 and player.participant.partner_name==3:
            player.participant.name_partner_round2='Patricia'
        elif player.participant.partner_gender==0 and player.participant.partner_name==4:
            player.participant.name_partner_round2='Elizabeth'
        elif player.participant.partner_gender == 0 and player.participant.partner_name == 5:
            player.participant.name_partner_round2 = 'Charlotte'
        elif player.participant.partner_gender == 0 and player.participant.partner_name == 6:
            player.participant.name_partner_round2 = 'Lisa'
        elif player.participant.partner_gender == 0 and player.participant.partner_name == 7:
            player.participant.name_partner_round2 = 'Amelia'
        elif player.participant.partner_gender == 0 and player.participant.partner_name == 8:
            player.participant.name_partner_round2 = 'Jessica'
        elif player.participant.partner_gender == 0 and player.participant.partner_name == 9:
            player.participant.name_partner_round2 = 'Sarah'
        elif player.participant.partner_gender == 0 and player.participant.partner_name == 10:
            player.participant.name_partner_round2 = 'Karen'





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
            if player.participant.gender == 1 and player.participant.name == 1:
                player.session.name_selected = 'James'
            elif player.participant.gender == 1 and player.participant.name == 2:
                player.session.name_selected = 'David'
            elif player.participant.gender == 1 and player.participant.name == 3:
                player.session.name_selected = 'John'
            elif player.participant.gender == 1 and player.participant.name == 4:
                player.session.name_selected = 'Robert'
            elif player.participant.gender == 0 and player.participant.name == 1:
                player.session.name_selected = 'Mary'
            elif player.participant.gender == 0 and player.participant.name == 2:
                player.session.name_selected = 'Emma'
            elif player.participant.gender == 0 and player.participant.name == 3:
                player.session.name_selected = 'Patricia'
            elif player.participant.gender == 1 and player.participant.name == 4:
                player.session.name_selected = 'Elizabeth'

        else:
            player.partner_selected = False
            if player.participant.gender == 1 and player.participant.name == 1:
                player.session.name_NOTselected = 'James'
            elif player.participant.gender == 1 and player.participant.name == 2:
                player.session.name_NOTselected = 'David'
            elif player.participant.gender == 1 and player.participant.name == 3:
                player.session.name_NOTselected = 'John'
            elif player.participant.gender == 1 and player.participant.name == 4:
                player.session.name_NOTselected = 'Robert'
            elif player.participant.gender == 0 and player.participant.name == 1:
                player.session.name_NOTselected = 'Mary'
            elif player.participant.gender == 0 and player.participant.name == 2:
                player.session.name_NOTselected = 'Emma'
            elif player.participant.gender == 0 and player.participant.name == 3:
                player.session.name_NOTselected = 'Patricia'
            elif player.participant.gender == 1 and player.participant.name == 4:
                player.session.name_NOTselected = 'Elizabeth'

def message(player):
    player.participant.Message=player.Message

def send_message(group):
    for player in group.get_players():
        if player.partner_selected == False:
            if player.participant.Message == 1:
                player.session.Message_selected = '"No stress, this matrix can be tricky!"'
            elif player.participant.Message == 2:
                player.session.Message_selected = '"Don’t worry, mistakes happen!"'
            elif player.participant.Message == 3:
                player.session.Message_selected = '"I know it’s tough, but try to focus more."'
            elif player.participant.Message == 4:
                player.session.Message_selected = '"It’s crucial to get the exact count, you should try another counting method."'




def set_correct_group(group):
    correct_answers = [47, 52, 46, 61, 54, 50]
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

# PAGES




class InstructionsRanking(Page):
    form_model = 'player'
    form_fields = ['belief_own', 'belief_partner']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class WaitforInstructions2(WaitPage):
    body_text = "Veuillez attendre les autres participants."
    wait_for_all_groups = True


class InstructionsRanking2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class WaitforInstructions3(WaitPage):
    body_text = "Veuillez attendre les autres participants."
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
    body_text = "Veuillez attendre les autres participants."
    wait_for_all_groups = True


class InstructionsPos(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class WaitforInstructions5(WaitPage):
    body_text = "Veuillez attendre les autres participants."
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
    body_text = "Veuillez attendre votre partenaire."

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



#page_sequence = [ Survey,WaitForNames, NameSelectionF,NameSelectionM, InstructionsRanking, WaitforInstructions2, InstructionsRanking2, WaitforInstructions3, Instructions, InstructionsTreatment2, WaitforInstructions4,InstructionsPos, WaitforInstructions5, InstructionsNegControl, InstructionsNegTreatment1, InstructionsNegTreatment2, MyWaitPage,Belief,WaitforFirstTable, Count, WaitforFeedback, FeedbackPositive, FeedbackNegControl, FeedbackNegative, FeedbackNeg2, Message, WaitforCommunication, MessageSent, MessageReceived, WaitforNextTable]
#page_sequence = [ MyWaitPage,NamePartner, WaitforBelief, Belief,WaitforFirstTable, Count, WaitforFeedback, FeedbackPositive, FeedbackNegControl, FeedbackNegative, FeedbackNeg2, Message, WaitforCommunication, MessageSent, MessageReceived, WaitforNextTable]

page_sequence = [ MyWaitPage, NamePartner,WaitforFirstTable, Count, WaitforFeedback, FeedbackPositive, FeedbackNegControl,  WaitforNextTable]
