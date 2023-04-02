from otree.api import *
import random



doc = """
Counting Task: Communication and feedback. But can't submit a new answer. 
"""

class C(BaseConstants):
    NAME_IN_URL = 'Counting_Collab_feedback'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 45
    #PAYMENT_CURRENT_PER_ITEM = cu(1)



class Subsession(BaseSubsession):
   pass

class Group(BaseGroup):
    same1 = models.BooleanField(doc="Whether players submit the same first sum as a group")
    same2 = models.BooleanField(doc="Whether players submit the same second sum as a group")


class Player(BasePlayer):
     answerA= models.IntegerField(label="How many 0s are in Sub-Table A?")
     answerB = models.IntegerField(label="How many 0s are in Sub-Table B?")
     sum1=models.IntegerField(doc="First Sum submitted (individually) ")
     sum2 = models.IntegerField(label="How many 0s are in the Table?", doc=" First Sum submitted in group ")
     sum3=models.IntegerField(label="How many 0s are in the Table?", doc="Second Sum submitted in group")
     sumE = models.IntegerField(label="How many 0s are in the Table?")
     same1_ind = models.BooleanField(doc="Whether both participants submit the same sum (first time)")
     same2_ind = models.BooleanField(doc="Whether both participants submit the same sum (second time)")
     correct = models.BooleanField( doc="Whether the first sum provided is correct.")
     correctG1=models.BooleanField( doc="Whether the first sum provided in group is correct.", default=True)
     timed_out = models.BooleanField(doc="Whether the participant submitted an answer within the allotted time.")
     correctE=models.BooleanField(default=True)
     confidence=models.IntegerField(widget=widgets.RadioSelectHorizontal,
                       choices=[1,2,3,4,5,6,7,8,9,10], label= "How confident are you that the number of 0s you just counted in the table is correct?")

def set_sum1(player):
        sum1= player.answerA + player.answerB
        player.sum1=sum1
        player.participant.sum1=player.sum1
        player.participant.answerA=player.answerA
        player.participant.answerB = player.answerB


def set_correctG1(player):
    player.participant.sum2 = player.sum2
    correct_answers = [75, 77, 71, 74, 80, 74]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.sum2 == correct:
            correctG1 = True
        else:
            correctG1 = False

    player.correctG1 = correctG1


def set_same1(group):
    for player in group.get_players():
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        if p1.sum2 == p2.sum2:
            same1 = True
        else:
            same1 = False

        group.same1 = same1
        player.same1_ind = same1

def set_same2(group):
    for player in group.get_players():
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        if p1.sum3 == p2.sum3:
            same2 = True
        else:
            same2 = False

        group.same2 = same2
        player.same2_ind = same2




def set_correct(player):
    correct_answers = [75, 77, 71, 74, 80, 74]
    for player, correct in zip(player.in_all_rounds(), correct_answers):
        if player.sum1 == correct:
            correct = True
        else:
            correct = False

    player.correct = correct

def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()

class Start(Page):

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        import time

        # remember to add 'expiry' to PARTICIPANT_FIELDS. 3 minutes to count as many correct tables.
        participant.expiry = time.time() + 6*60

    def is_displayed(player):
        return player.round_number == 1




class Count(Page):
    form_model = 'player'
    form_fields = ['answerA', 'answerB']

    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return min(C.TIME_PER_PROBLEM,participant.expiry - time.time())

    def is_displayed(player):
        return get_timeout_seconds(player) > 3

    def before_next_page(player, timeout_happened):
        # player.timed_out = True if player.timed_out else False
        # if player.round_number == C.NUM_ROUNDS:
        set_sum1(player)
        set_correct(player)



class Confidence(Page):
    form_model = 'player'
    form_fields = ['confidence']

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 3


class WaitforChat(WaitPage):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()

    def is_displayed(player):
        return get_timeout_seconds(player) > 3
class Chat(Page):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return  participant.expiry - time.time()

    form_model = 'player'
    form_fields = ['sum2']

    def is_displayed(player):
        return get_timeout_seconds(player) > 3

    def before_next_page(player, timeout_happened):
        set_correctG1(player)

class WaitforNext(WaitPage):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()

    def is_displayed(player):
        return get_timeout_seconds(player) > 3

class feedback(Page):
        @staticmethod
        def get_timeout_seconds(player):
            participant = player.participant
            import time
            return participant.expiry - time.time()

        form_model = 'player'

        def is_displayed(player):
            return player.correctG1 == True and  get_timeout_seconds(player) > 3

class feedback_neg(Page):
        @staticmethod
        def get_timeout_seconds(player):
            participant = player.participant
            import time
            return participant.expiry - time.time()

        form_model = 'player'

        def is_displayed(player):
             return player.correctG1 == False and get_timeout_seconds(player) > 3


class WaitforNext2(WaitPage):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        import time
        return participant.expiry - time.time()

    def is_displayed(player):
        return get_timeout_seconds(player) > 3







page_sequence = [Start,Count, Confidence, WaitforChat, Chat, WaitforNext,  feedback, feedback_neg, WaitforNext2]