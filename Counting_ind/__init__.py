from otree.api import *
import random



doc = """
Counting Task: No communication. Can re-submit once. 
"""

class C(BaseConstants):
    NAME_IN_URL = 'Counting_ind'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 6
    TIME_PER_PROBLEM = 45
    #PAYMENT_CURRENT_PER_ITEM = cu(1)



class Subsession(BaseSubsession):
   pass

class Group(BaseGroup):
   pass

class Player(BasePlayer):
     answerA= models.IntegerField(label="How many 0s are in Sub-Table A?")
     answerB = models.IntegerField(label="How many 0s are in Sub-Table B?")
     sum1=models.IntegerField(doc="First Sum submitted (individually) ")
     sum2 = models.IntegerField(label="How many 0s are in the Table?", doc=" First Sum submitted in group ")
     sum3=models.IntegerField(label="How many 0s are in the Table?", doc="Second Sum submitted in group")
     correct = models.BooleanField( doc="Whether the first sum provided is correct.", default=False)
     correctG1=models.BooleanField( doc="Whether the first sum provided in group is correct.")
     timed_out = models.BooleanField(doc="Whether the participant submitted an answer within the allotted time.")
     confidence=models.IntegerField(widget=widgets.RadioSelect,
                       choices=[1,2,3,4,5,6,7,8,9,10], label= "How confident are you that the number of 0s you just counted in the table is correct?")

def set_sum1(player):
        sum1= player.answerA + player.answerB
        player.sum1=sum1
        player.participant.sum1=player.sum1
        player.participant.answerA=player.answerA
        player.participant.answerB = player.answerB






def set_correct(player):
    correct_answers = [49, 52, 49, 50, 46, 53]
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
        participant.expiry = time.time() + 1*60

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

    def is_displayed(player):
        return get_timeout_seconds(player) > 3


class count2(Page):
        @staticmethod
        def get_timeout_seconds(player):
            participant = player.participant
            import time
            return participant.expiry - time.time()

        form_model = 'player'
        form_field = ['sum2']

        def is_displayed(player):
            return player.correct == False and  get_timeout_seconds(player) > 3







page_sequence = [Start,Count, Confidence, count2]