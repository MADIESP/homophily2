from otree.api import *
import os


doc = """
3 rounds played in teams
"""


class C(BaseConstants):
    NAME_IN_URL = 'TestGame'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 4
    Fnames = ["Mary", "Emma", "Patricia", "Elizabeth"]
    Mnames = ["James", "David", "John", "Robert"]



class Subsession(BaseSubsession):
    Treatment = models.IntegerField()



class Group(BaseGroup):
    selected_count = models.IntegerField()
    selected_player=models.IntegerField(default=2)


class Player(BasePlayer):
    Treatment = models.IntegerField()
    gender = models.IntegerField(label="What gender do you identify with?", widget=widgets.RadioSelectHorizontal,
                                 choices=[[0, "Female"], [1, "Male"]], default=1)
    FemaleNames = models.IntegerField()
    MaleNames = models.IntegerField()
    name = models.IntegerField()
    partner_name = models.IntegerField()
    partner_gender=models.IntegerField()
    count = models.IntegerField(label="How many 0s are in the table?")
    correct = models.BooleanField(doc="Whether the count is correct.")
    correct_Group = models.BooleanField(doc="Whether the selected count is correct.")
    partner_selected = models.BooleanField(doc="Whether the count is correct.")
    Message = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                    choices=[[1, "It’s okay, this matrix is tricky."], [2, "Don't worry; mistakes happen."], [3, "You need to be more careful with these matrices."], [4, "It’s crucial to get the exact count; this was off."]])
    belief_own=models.IntegerField(label="")
    belief_partner = models.IntegerField(label="")

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
    correct_answers = [50, 52, 47, 52,46,61]
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
            player.participant.name_partner='James'
        elif player.participant.partner_gender==1 and player.participant.partner_name==2:
            player.participant.name_partner='David'
        elif player.participant.partner_gender==1 and player.participant.partner_name==3:
            player.participant.name_partner='John'
        elif player.participant.partner_gender==1 and player.participant.partner_name==4:
            player.participant.name_partner='Robert'
        elif player.participant.partner_gender==0 and player.participant.partner_name==1:
            player.participant.name_partner='Mary'
        elif player.participant.partner_gender==0 and player.participant.partner_name==2:
            player.participant.name_partner='Emma'
        elif player.participant.partner_gender==0 and player.participant.partner_name==3:
            player.participant.name_partner='Patricia'
        elif player.participant.partner_gender==0 and player.participant.partner_name==4:
            player.participant.name_partner='Elizabeth'





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
                player.session.Message_selected = '"It’s okay, this matrix is tricky."'
            elif player.participant.Message == 2:
                player.session.Message_selected = '"Don’t worry; mistakes happen."'
            elif player.participant.Message == 3:
                player.session.Message_selected = '"You need to be more careful with these matrices."'
            elif player.participant.Message == 4:
                player.session.Message_selected = '"It’s crucial to get the exact count; this was off."'




def set_correct_group(group):
    correct_answers = [50, 52, 47, 52,46,61]
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

class Survey(Page):
    form_model = 'player'
    form_fields = ['gender']

    def is_displayed(player):
        return player.round_number == 1

    def before_next_page(player, timeout_happened):
        gender(player)

class WaitForNames(WaitPage):
    pass

class NameSelectionF(Page):
    form_model = 'player'
    form_fields = ['chosen_nameF']

    def is_displayed(player):
         return player.chosen_nameF == "" and player.gender==0 and player.round_number==1

        # Show the page if the player hasn't chosen a name yet

    def error_message(self, values):
        chosen_nameF = values['chosen_nameF']
        if chosen_nameF in [p.chosen_nameF for p in self.group.get_players()]:
            return "This name was already taken. Please select another name."

    def before_next_page(player, timeout_happened):
        Fnames(player)
        Femalename(player)


class NameSelectionM(Page):
    form_model = 'player'
    form_fields = ['chosen_nameM']

    def is_displayed(player):
         return player.chosen_nameM == "" and player.gender==1 and player.round_number==1

        # Show the page if the player hasn't chosen a name yet

    def error_message(self, values):
        chosen_nameM = values['chosen_nameM']
        if chosen_nameM in [p.chosen_nameM for p in self.group.get_players()]:
            return "This name was already taken. Please select another name."

    def before_next_page(player, timeout_happened):
        Mnames(player)
        Malename(player)


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


class MyWaitPage(WaitPage):

    #@staticmethod
    #def call_functions(group):
        #partner_name(group)
        #name(group)
        #name2(group)


    after_all_players_arrive = partner_name

    @staticmethod
    def is_displayed(player: Player):
        return  player.round_number == 1





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
    timer_text = 'Time left to count this table:'

    def before_next_page(player, timeout_happened):
        set_correct(player)

class WaitforFeedback(WaitPage):
    body_text = "Waiting for your partner."

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
    body_text = "Waiting for your partner."

class MessageSent(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected != True and player.subsession.Treatment==3

class MessageReceived(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.correct_Group == False and player.partner_selected == True and player.subsession.Treatment==3


class WaitforNextTable(WaitPage):
    body_text = "Waiting for your partner."



page_sequence = [ Survey,WaitForNames, NameSelectionF,NameSelectionM, InstructionsRanking, WaitforInstructions2, InstructionsRanking2, WaitforInstructions3, Instructions, InstructionsTreatment2, WaitforInstructions4, InstructionsPos, WaitforInstructions5, InstructionsNegControl, InstructionsNegTreatment1, InstructionsNegTreatment2, MyWaitPage,Belief,WaitforFirstTable, Count, WaitforFeedback, FeedbackPositive, FeedbackNegControl, FeedbackNegative, FeedbackNeg2, Message, WaitforCommunication, MessageSent, MessageReceived, WaitforNextTable]
